/*
 * FIRMWARE PARA UMA PERNA COMPLETA
 * * Este firmware lê:
 * 1. Um sensor EMG (Analógico)
 * 2. Um sensor ECG (Analógico, usado como EMG)
 * 3. Dois sensores IMU (MPU-6050) via I2C
 * * Requerimento de Hardware (IMPORTANTE):
 * Para ler 2 MPU-6050, você DEVE configurar os endereços I2C:
 * 1. IMU 1 (Quadril): Ligar o pino AD0 do MPU-6050 no GND (Endereço 0x68)
 * 2. IMU 2 (Coxa): Ligar o pino AD0 do MPU-6050 no 3.3V (Endereço 0x69)
 * * Requerimento de Software:
 * Instale as bibliotecas "Adafruit MPU6050" e "Adafruit Unified Sensor"
 * pela Gerenciador de Bibliotecas da Arduino IDE.
 */

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// --- Pinos Analógicos ---
#define ECG_PIN 34   // GPIO34 para Isquiotibial ("ECG")
#define EMG_PIN 32   // GPIO32 para Quadríceps ("EMG")

// --- Sensores I2C (IMU) ---
Adafruit_MPU6050 mpu1; // IMU 1 (Quadril, Endereço 0x68)
Adafruit_MPU6050 mpu2; // IMU 2 (Coxa, Endereço 0x69)

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(10); // Esperar a porta serial conectar
  }

  Serial.println("--- Firmware Perna Completa (EMG, ECG, 2x IMU) ---");

  // Configura os pinos analógicos
  pinMode(ECG_PIN, INPUT);
  pinMode(EMG_PIN, INPUT);

  // Inicializa o I2C
  Wire.begin();

  // Inicializa o IMU 1 (Endereço padrão 0x68)
  if (!mpu1.begin()) {
    Serial.println("Falha ao encontrar MPU-6050 (IMU 1) no endereço 0x68");
    while (1) {
      delay(10);
    }
  }
  Serial.println("IMU 1 (Quadril) conectado!");
  mpu1.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu1.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu1.setFilterBandwidth(MPU6050_BAND_21_HZ);

  // Inicializa o IMU 2 (Endereço 0x69)
  if (!mpu2.begin(0x69)) {
    Serial.println("Falha ao encontrar MPU-6050 (IMU 2) no endereço 0x69");
    Serial.println("VERIFIQUE SE O PINO AD0 DO IMU 2 ESTÁ EM 3.3V!");
    while (1) {
      delay(10);
    }
  }
  Serial.println("IMU 2 (Coxa) conectado!");
  mpu2.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu2.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu2.setFilterBandwidth(MPU6050_BAND_21_HZ);
  
  delay(100);
}

void loop() {
  // 1. Ler Sensores Analógicos
  int valor_emg = analogRead(EMG_PIN);
  int valor_ecg = analogRead(ECG_PIN);

  // 2. Ler Sensores IMU
  sensors_event_t a1, g1, temp1;
  mpu1.getEvent(&a1, &g1, &temp1);
  
  sensors_event_t a2, g2, temp2;
  mpu2.getEvent(&a2, &g2, &temp2);

  // 3. Enviar todos os 14 dados em uma única linha CSV
  // Formato: EMG,ECG,A1x,A1y,A1z,G1x,G1y,G1z,A2x,A2y,A2z,G2x,G2y,G2z

  Serial.print(valor_emg); Serial.print(",");
  Serial.print(valor_ecg); Serial.print(",");

  Serial.print(a1.acceleration.x, 4); Serial.print(",");
  Serial.print(a1.acceleration.y, 4); Serial.print(",");
  Serial.print(a1.acceleration.z, 4); Serial.print(",");
  Serial.print(g1.gyro.x, 4); Serial.print(",");
  Serial.print(g1.gyro.y, 4); Serial.print(",");
  Serial.print(g1.gyro.z, 4); Serial.print(",");

  Serial.print(a2.acceleration.x, 4); Serial.print(",");
  Serial.print(a2.acceleration.y, 4); Serial.print(",");
  Serial.print(a2.acceleration.z, 4); Serial.print(",");
  Serial.print(g2.gyro.x, 4); Serial.print(",");
  Serial.print(g2.gyro.y, 4); Serial.print(",");
  Serial.println(g2.gyro.z, 4); // Use println no último valor

  delay(10); // Tenta manter ~100Hz (a leitura do IMU pode atrasar um pouco)
}


