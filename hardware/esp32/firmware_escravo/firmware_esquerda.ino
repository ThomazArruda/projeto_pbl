/*
 * FIRMWARE PERNA ESQUERDA (Wi-Fi UDP)
 * ID: ESQ
 * Envia: ID, ANGULO, EMG, ECG
 */
#include <WiFi.h>
#include <WiFiUdp.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// --- [CONFIGURAÇÕES DE REDE] ---
const char* ssid = "Lara Beatriz";     
const char* password = "12345678"; 
// !!! COLOQUE O IP DO SEU COMPUTADOR AQUI !!!
const char* host_ip = "192.168.XXX.XXX";  
const int udp_port = 4210; 

const char* ID_DISPOSITIVO = "ESQ"; 
WiFiUDP udp;

// --- [HARDWARE] ---
#define EMG_PIN 34 
#define ECG_PIN 35 

Adafruit_MPU6050 mpuQuadril; 
Adafruit_MPU6050 mpuCoxa;    
#define I2C_BUS2_SDA 32 
#define I2C_BUS2_SCL 33

float pitchQuadril = 0, pitchCoxa = 0;
unsigned long last_time;
const float COMPL_FILTER_ALPHA = 0.98;

void setup() {
    Serial.begin(115200);
    // Partição Huge APP recomendada
    
    Wire.begin(); 
    Wire1.begin(I2C_BUS2_SDA, I2C_BUS2_SCL); 

    if (!mpuQuadril.begin(0x68, &Wire)) Serial.println("Falha MPU Quadril");
    mpuQuadril.setAccelerometerRange(MPU6050_RANGE_8_G);
    mpuQuadril.setGyroRange(MPU6050_RANGE_500_DEG);

    if (!mpuCoxa.begin(0x68, &Wire1)) Serial.println("Falha MPU Coxa");
    mpuCoxa.setAccelerometerRange(MPU6050_RANGE_8_G);
    mpuCoxa.setGyroRange(MPU6050_RANGE_500_DEG);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWi-Fi Conectado (ESQ)!");
    udp.begin(udp_port);
    last_time = millis();
}

void loop() {
    unsigned long current_time = millis();
    float delta_time = (current_time - last_time) / 1000.0;
    last_time = current_time;

    sensors_event_t a1, g1, temp1; mpuQuadril.getEvent(&a1, &g1, &temp1);
    sensors_event_t a2, g2, temp2; mpuCoxa.getEvent(&a2, &g2, &temp2);

    float pitchQ_acc = atan2(a1.acceleration.y, a1.acceleration.z) * 57.2958;
    float pitchC_acc = atan2(a2.acceleration.y, a2.acceleration.z) * 57.2958;

    pitchQuadril = COMPL_FILTER_ALPHA * (pitchQuadril + g1.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitchQ_acc;
    pitchCoxa = COMPL_FILTER_ALPHA * (pitchCoxa + g2.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitchC_acc;

    int emg_val = analogRead(EMG_PIN);
    int ecg_val = analogRead(ECG_PIN);
    float final_angle = fabs(pitchQuadril - pitchCoxa); 

    char buffer_dados[64];
    // Formato CSV simples: ESQ,ANGULO,EMG,ECG
    sprintf(buffer_dados, "%s,%.2f,%d,%d", ID_DISPOSITIVO, final_angle, emg_val, ecg_val);

    udp.beginPacket(host_ip, udp_port);
    udp.print(buffer_dados); 
    udp.endPacket();
    
    delay(10); // ~100Hz
}
