/*
 * FIRMWARE MESTRE (PERNA 1)
 * - Baseado no V7 (que funcionou).
 * - Lê seus 3 sensores (EMG, ECG, Ângulo Relativo).
 * - Recebe os 3 sensores do Escravo via ESP-NOW.
 * - Envia todos os 6 valores para o PC via Bluetooth Serial.
 */

#include <esp_now.h>
#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include "BluetoothSerial.h" // Importa a biblioteca Bluetooth

// --- Configuração do Bluetooth ---
// Se der erro aqui, talvez você precise ativar o Bluetooth no menu 'Tools'
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth não está ativado! Por favor, ative-o no menu 'Tools'.
#endif
BluetoothSerial SerialBT; // Cria o objeto Bluetooth Serial

// --- Estrutura dos Dados ---
// Deve ser IDÊNTICA no Mestre e no Escravo.
typedef struct struct_message {
    int emg_val;
    int ecg_val;
    float angle_val;
} struct_message;

// Variáveis para guardar os dados
struct_message dadosPerna1; // Dados da Perna 1 (NÓS MESMOS)
struct_message dadosPerna2; // Dados da Perna 2 (recebidos do Escravo)

// --- Pinos e Sensores (Igual ao V7) ---
#define EMG_PIN 34
#define ECG_PIN 35
Adafruit_MPU6050 mpu1;
// A biblioteca Wire do ESP32 já define 'Wire1' automaticamente.
Adafruit_MPU6050 mpu2;
#define I2C_BUS1_SDA 32
#define I2C_BUS1_SCL 33
float pitch1 = 0, pitch2 = 0;
unsigned long last_time;
const float COMPL_FILTER_ALPHA = 0.98;
const unsigned long SENSOR_PERIOD = 10; // Envia dados a 100Hz
unsigned long last_sensor_time = 0;

// --- Setup do Hardware ---
void setup_hardware() {
  Serial.begin(115200); // Usado apenas para debug no Mestre
  pinMode(EMG_PIN, INPUT);
  pinMode(ECG_PIN, INPUT);
  
  Wire.begin(); 
  if (!mpu1.begin(0x68, &Wire)) { 
    Serial.println("MESTRE: Falha MPU-1 (barramento 0)");
    while(1) delay(10);
  }
  Wire1.begin(I2C_BUS1_SDA, I2C_BUS1_SCL);
  if (!mpu2.begin(0x68, &Wire1)) {
    Serial.println("MESTRE: Falha MPU-2 (barramento 1)");
    while(1) delay(10);
  }
  mpu1.setAccelerometerRange(MPU6050_RANGE_8_G); mpu1.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu2.setAccelerometerRange(MPU6050_RANGE_8_G); mpu2.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.println("MESTRE: Hardware pronto.");
}

// --- Callback: O que fazer quando o Escravo mandar dados ---
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  // Apenas copiamos os dados recebidos para a nossa variável global
  memcpy(&dadosPerna2, incomingData, sizeof(dadosPerna2));
  
  /*
  // Descomente para debug no Monitor Serial
  Serial.print("Recebido do Escravo: ");
  Serial.print(dadosPerna2.emg_val); Serial.print(", ");
  Serial.print(dadosPerna2.ecg_val); Serial.print(", ");
  Serial.println(dadosPerna2.angle_val);
  */
}
 
// --- Setup do ESP-NOW ---
void setup_espnow() {
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) {
    Serial.println("MESTRE: Erro ao inicializar ESP-NOW");
    return;
  }
  // Define o Mestre como "receptor"
  esp_now_register_recv_cb(OnDataRecv);
  Serial.println("MESTRE: ESP-NOW pronto. Aguardando dados do Escravo.");
}

void setup() {
  setup_hardware();
  setup_espnow();
  
  // Inicia o Bluetooth Serial com um nome público
  SerialBT.begin("ESP32_Pernas_Reab"); 
  Serial.println("MESTRE: Bluetooth iniciado. PC pode conectar.");
  
  last_time = millis();
  last_sensor_time = millis();
}

// --- Loop de Leitura e Envio ---
void loop() {
  unsigned long current_time = millis();

  // --- Loop de Cálculo (Roda o mais rápido possível) ---
  float delta_time = (current_time - last_time) / 1000.0;
  sensors_event_t a1, g1, temp1; mpu1.getEvent(&a1, &g1, &temp1);
  sensors_event_t a2, g2, temp2; mpu2.getEvent(&a2, &g2, &temp2);
  float pitch1_acc = atan2(a1.acceleration.y, a1.acceleration.z) * RAD_TO_DEG;
  float pitch2_acc = atan2(a2.acceleration.y, a2.acceleration.z) * RAD_TO_DEG;
  pitch1 = COMPL_FILTER_ALPHA * (pitch1 + g1.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitch1_acc;
  pitch2 = COMPL_FILTER_ALPHA * (pitch2 + g2.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitch2_acc;
  last_time = current_time;

  // --- Loop de Envio (Roda a 100Hz) ---
  if (current_time - last_sensor_time >= SENSOR_PERIOD) {
    last_sensor_time = current_time;

    // 1. Colhe os dados da Perna 1 (este ESP32)
    dadosPerna1.emg_val = analogRead(EMG_PIN);
    dadosPerna1.ecg_val = analogRead(ECG_PIN);
    dadosPerna1.angle_val = fabs(pitch1 - pitch2);
    
    // 2. Envia TUDO (Perna 1 + Perna 2) via Bluetooth
    // Formato: E1:val,C1:val,A1:val,E2:val,C2:val,A2:val
    SerialBT.printf("E1:%d,C1:%d,A1:%.2f,E2:%d,C2:%d,A2:%.2f\n",
      dadosPerna1.emg_val,
      dadosPerna1.ecg_val,
      dadosPerna1.angle_val,
      dadosPerna2.emg_val,  // Este valor vem do Escravo
      dadosPerna2.ecg_val,  // Este valor vem do Escravo
      dadosPerna2.angle_val // Este valor vem do Escravo
    );

    // 3. (OPCIONAL) Imprime no Monitor Serial (USB) para debug
    Serial.printf("E1:%d,C1:%d,A1:%.2f,E2:%d,C2:%d,A2:%.2f\n",
      dadosPerna1.emg_val,
      dadosPerna1.ecg_val,
      dadosPerna1.angle_val,
      dadosPerna2.emg_val,
      dadosPerna2.ecg_val,
      dadosPerna2.angle_val
    );
  }
}
