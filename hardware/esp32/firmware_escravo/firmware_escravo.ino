/*
 * FIRMWARE ESCRAVO (PERNA 2)
 *
 * Versão de 6 valores (3 por perna):
 * - Lê 4 sensores (EMG, ECG, 2x IMU).
 * - Calcula o ÂNGULO RELATIVO (fabs(pitch1 - pitch2)).
 * - Envia 3 valores (EMG, ECG, Ângulo) para o Mestre.
 */

#include <esp_now.h>
#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// ======================================================================
// !!!   MAC ADDRESS DO MESTRE   !!!
// O seu MAC (EC:64:C9:86:4D:08) está aqui:
// ======================================================================
uint8_t mac_mestre[] = {0xEC, 0x64, 0xC9, 0x86, 0x4D, 0x08};
// ======================================================================


// --- Estrutura dos Dados (AGORA COM 3 VALORES) ---
typedef struct struct_message {
    int emg_val;
    int ecg_val;
    float angle_val; // <--- APENAS O ÂNGULO RELATIVO
} struct_message;

struct_message dadosPerna2; // Variável para guardar nossos dados

// --- Pinos e Sensores (Sem alteração) ---
#define EMG_PIN 34
#define ECG_PIN 35
Adafruit_MPU6050 mpu1;
Adafruit_MPU6050 mpu2;
#define I2C_BUS1_SDA 32
#define I2C_BUS1_SCL 33
float pitch1 = 0, pitch2 = 0;
unsigned long last_time;
const float COMPL_FILTER_ALPHA = 0.98;
const unsigned long SENSOR_PERIOD = 10; // Lê sensores a 100Hz
unsigned long last_sensor_time = 0;

// --- Setup do Hardware (Sem alteração) ---
void setup_hardware() {
  Serial.begin(115200);
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

// --- Setup do ESP-NOW (Sem alteração) ---
void setup_espnow() {
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) {
    Serial.println("ESCRAVO: Erro ao inicializar ESP-NOW");
    return;
  }
  
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

  // --- Loop de Cálculo (Sem alteração) ---
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

    // <<< CORREÇÃO AQUI: Preenche os 3 valores >>>
    dadosPerna2.emg_val = analogRead(EMG_PIN);
    dadosPerna2.ecg_val = analogRead(ECG_PIN);
    dadosPerna2.angle_val = fabs(pitch1 - pitch2); // Calcula o ângulo relativo
    
    // Envia o pacote de dados (agora com 3 valores) para o Mestre
    esp_err_t result = esp_now_send(mac_mestre, (uint8_t *) &dadosPerna2, sizeof(dadosPerna2));

    /*
    // Descomente para debug no Monitor Serial do ESCRAVO
    if (result == ESP_OK) {
      Serial.printf("ESCRAVO: Enviado E:%d, C:%d, A:%.2f\n", 
        dadosPerna2.emg_val, dadosPerna2.ecg_val, dadosPerna2.angle_val);
    } else {
      Serial.println("ESCRAVO: Erro ao enviar pacote");
    }
    */
  }
}
