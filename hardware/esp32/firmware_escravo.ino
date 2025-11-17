/*
 * FIRMWARE ESCRAVO (PERNA 2)
 * - Baseado no V7 (que funcionou).
 * - Lê seus 3 sensores (EMG, ECG, Ângulo Relativo).
 * - Envia os 3 valores para o Mestre via ESP-NOW.
 */

#include <esp_now.h>
#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// ======================================================================
// !!! PASSO MAIS IMPORTANTE !!!
// !!!   COLE O ENDEREÇO MAC DO SEU MESTRE AQUI     !!!
// ======================================================================
// Substitua os 00s pelo endereço que você anotou.
// Ex: uint8_t mac_mestre[] = {0xA0, 0xB1, 0xC2, 0xD3, 0xE4, 0xF5};
uint8_t mac_mestre[] = {0xEC, 0x64, 0xC9, 0x86, 0x4D, 0x08};
// ======================================================================


// --- Estrutura dos Dados ---
// Este é o "pacote" de dados que vamos enviar.
// Deve ser IDÊNTICO no Mestre e no Escravo.
typedef struct struct_message {
    int emg_val;
    int ecg_val;
    float angle_val;
} struct_message;

struct_message dadosPerna2; // Variável para guardar nossos dados

// --- Pinos e Sensores (Igual ao V7, assumindo a MESMA fiação da Perna 1) ---
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
const unsigned long SENSOR_PERIOD = 10; // Lê sensores a 100Hz
unsigned long last_sensor_time = 0;

// --- Setup do Hardware (Baseado no V7) ---
void setup_hardware() {
  Serial.begin(115200); // Usado apenas para debug no Escravo
  pinMode(EMG_PIN, INPUT);
  pinMode(ECG_PIN, INPUT);
  
  Wire.begin(); 
  if (!mpu1.begin(0x68, &Wire)) { 
    Serial.println("ESCRAVO: Falha MPU-1 (barramento 0)");
    while(1) delay(10);
  }
  Wire1.begin(I2C_BUS1_SDA, I2C_BUS1_SCL);
  if (!mpu2.begin(0x68, &Wire1)) {
    Serial.println("ESCRAVO: Falha MPU-2 (barramento 1)");
    while(1) delay(10);
  }
  mpu1.setAccelerometerRange(MPU6050_RANGE_8_G); mpu1.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu2.setAccelerometerRange(MPU6050_RANGE_8_G); mpu2.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.println("ESCRAVO: Hardware pronto.");
}

// --- Setup do ESP-NOW ---
void setup_espnow() {
  WiFi.mode(WIFI_STA); // Coloca o Wi-Fi em modo "Estação"
  if (esp_now_init() != ESP_OK) {
    Serial.println("ESCRAVO: Erro ao inicializar ESP-NOW");
    return;
  }
  
  // Registra o Mestre como "parceiro" de envio
  esp_now_peer_info_t peerInfo;
  memcpy(peerInfo.peer_addr, mac_mestre, 6);
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;
  
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("ESCRAVO: Falha ao adicionar Mestre");
    return;
  }
  Serial.println("ESCRAVO: ESP-NOW pronto. Pareado com Mestre.");
}

void setup() {
  setup_hardware();
  setup_espnow();
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

    // Colhe os 3 dados
    dadosPerna2.emg_val = analogRead(EMG_PIN);
    dadosPerna2.ecg_val = analogRead(ECG_PIN);
    dadosPerna2.angle_val = fabs(pitch1 - pitch2);
    
    // Envia o pacote de dados para o Mestre
    esp_err_t result = esp_now_send(mac_mestre, (uint8_t *) &dadosPerna2, sizeof(dadosPerna2));

    
    // Descomente esta seção para ver no Monitor Serial do ESCRAVO se ele está enviando
    /*
    if (result == ESP_OK) {
      Serial.println("ESCRAVO: Pacote enviado com sucesso");
    } else {
      Serial.println("ESCRAVO: Erro ao enviar pacote");
    }
    */
  }
}
