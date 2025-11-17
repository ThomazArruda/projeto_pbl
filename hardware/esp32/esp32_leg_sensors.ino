/*
 * FIRMWARE V4 (ALTA PERFORMANCE)
 *
 * O que ele faz:
 * 1. Remove todos os `delay()` do loop principal.
 * 2. Lê EMG (D34) e ECG (D35).
 * 3. Lê os dois IMUs (MPU-6050) em seus barramentos I2C separados.
 * 4. Aplica um Filtro Complementar em cada IMU para fundir Acelerômetro e
 * Giroscópio, obtendo um ângulo estável (Pitch) para cada um.
 * 5. Calcula o Ângulo Relativo (Angulo1 - Angulo2).
 * 6. Envia apenas 3 valores pela serial em um formato rápido: "E:valor,C:valor,A:valor"
 */

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// --- Pinos Analógicos (Corrigidos) ---
#define EMG_PIN 34   // GPIO34 para EMG (Quadríceps)
#define ECG_PIN 35   // GPIO35 para ECG (Isquiotibial)

// --- Barramento I2C nº 1 (Padrão, para IMU_C) ---
Adafruit_MPU6050 mpu1;

// --- Barramento I2C nº 2 (Customizado, para IMU_P) ---
TwoWire Wire1 = TwoWire(1);
Adafruit_MPU6050 mpu2;
#define I2C_BUS1_SDA 32
#define I2C_BUS1_SCL 33

// --- Variáveis do Filtro Complementar ---
float pitch1 = 0; // Ângulo (Pitch) do IMU 1
float pitch2 = 0; // Ângulo (Pitch) do IMU 2
unsigned long last_time; // Tempo da última leitura

// --- Constantes do Filtro ---
const float RAD_TO_DEG = 180.0 / M_PI;
const float COMPL_FILTER_ALPHA = 0.98; // 98% Giroscópio, 2% Acelerômetro

// --- Constantes de Loop (Sem Delay) ---
const unsigned long SERIAL_PERIOD = 10; // Envia dados a cada 10ms (100Hz)
unsigned long last_serial_time = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);
  Serial.println("--- Firmware V4 (Ângulo Relativo) ---");

  pinMode(EMG_PIN, INPUT);
  pinMode(ECG_PIN, INPUT);

  // Inicializa I2C 0 (Padrão D21/D22)
  Wire.begin(); 
  if (!mpu1.begin(0x68, &Wire)) { 
    Serial.println("Falha ao encontrar MPU-6050 (IMU 1) no barramento 0");
    while (1) delay(10);
  }
  Serial.println("IMU 1 (IMU_C) conectado!");
  mpu1.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu1.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu1.setFilterBandwidth(MPU6050_BAND_21_HZ);

  // Inicializa I2C 1 (Custom D32/D33)
  Wire1.begin(I2C_BUS1_SDA, I2C_BUS1_SCL);
  if (!mpu2.begin(0x68, &Wire1)) {
    Serial.println("Falha ao encontrar MPU-6050 (IMU 2) no barramento 1");
    while (1) delay(10);
  }
  Serial.println("IMU 2 (IMU_P) conectado!");
  mpu2.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu2.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu2.setFilterBandwidth(MPU6050_BAND_21_HZ);
  
  delay(100);
  last_time = millis(); // Inicia o timer do filtro
  last_serial_time = millis(); // Inicia o timer da serial
}

void loop() {
  // --- Loop de Cálculo (Roda o mais rápido possível) ---

  unsigned long current_time = millis();
  float delta_time = (current_time - last_time) / 1000.0; // Delta T em segundos

  // 1. Ler dados brutos dos IMUs
  sensors_event_t a1, g1, temp1;
  mpu1.getEvent(&a1, &g1, &temp1);
  sensors_event_t a2, g2, temp2;
  mpu2.getEvent(&a2, &g2, &temp2);

  // 2. Calcular o ângulo do Acelerômetro (Pitch) para cada IMU
  // (Esta é a parte "barulhenta" do filtro)
  float pitch1_acc = atan2(a1.acceleration.y, a1.acceleration.z) * RAD_TO_DEG;
  float pitch2_acc = atan2(a2.acceleration.y, a2.acceleration.z) * RAD_TO_DEG;

  // 3. Calcular o ângulo do Giroscópio (Pitch) para cada IMU
  // (Esta é a parte "suave" do filtro, que "drifta")
  // g1.gyro.x é a rotação no eixo X, que corresponde ao Pitch
  pitch1 = COMPL_FILTER_ALPHA * (pitch1 + g1.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitch1_acc;
  pitch2 = COMPL_FILTER_ALPHA * (pitch2 + g2.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitch2_acc;
  
  last_time = current_time; // Salva o tempo para o próximo cálculo

  // --- Loop de Envio (Roda a 100Hz) ---
  if (current_time - last_serial_time >= SERIAL_PERIOD) {
    last_serial_time = current_time;

    // 1. Ler Sensores Analógicos (só quando for enviar)
    int valor_emg = analogRead(EMG_PIN);
    int valor_ecg = analogRead(ECG_PIN);

    // 2. Calcular Ângulo Relativo
    float angulo_relativo = pitch1 - pitch2;

    // 3. Enviar dados no formato otimizado
    // Formato: E:valor,C:valor,A:valor_float
    Serial.printf("E:%d,C:%d,A:%.2f\n", valor_emg, valor_ecg, angulo_relativo);
  }
}
