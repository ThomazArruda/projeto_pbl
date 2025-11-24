#include <WiFi.h>
#include <WiFiUdp.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// --- [CONFIGURAÇÕES DE REDE] ---
const char* ssid = "Lara Beatriz";    // Wi-Fi do grupo
const char* password = "12345678"; // Senha do Wi-Fi 
const char* host_ip = " 192.168.249.15";  // IP do computador
const int udp_port = 4210; 

// --- [CONFIGURAÇÕES GERAIS] ---
const char* ID_DISPOSITIVO = "DIR"; // ID ÚNICO para o computador
WiFiUDP udp;

// --- [HARDWARE] ---
#define EMG_PIN 34 
#define ECG_PIN 35 

// MPU (Sensores de Angulo) - Usando pinos padrões do projeto anterior
Adafruit_MPU6050 mpuQuadril; 
Adafruit_MPU6050 mpuCoxa;    
#define I2C_BUS2_SDA 32 // Para o MPU Coxa
#define I2C_BUS2_SCL 33

float pitchQuadril = 0, pitchCoxa = 0;
unsigned long last_time;
const float COMPL_FILTER_ALPHA = 0.98;
const unsigned long SENSOR_PERIOD = 10; // 10ms (100 Hz)

void setup() {
    Serial.begin(115200);
    delay(2000); 

    // --- Inicialização I2C ---
    Wire.begin(); // Padrão 21/22 (Quadril)
    Wire1.begin(I2C_BUS2_SDA, I2C_BUS2_SCL); // 32/33 (Coxa)

    // Inicializa MPU 1 (Quadril)
    if (!mpuQuadril.begin(0x68, &Wire)) {
        Serial.println("ESCRAVA: Falha MPU Quadril. Verifique a conexao!");
    } else {
        Serial.println("ESCRAVA: MPU Quadril OK.");
    }
    
    // Inicializa MPU 2 (Coxa)
    if (!mpuCoxa.begin(0x68, &Wire1)) {
        Serial.println("ESCRAVA: Falha MPU Coxa.");
    } else {
        Serial.println("ESCRAVA: MPU Coxa OK.");
    }

    // --- Conexão Wi-Fi ---
    Serial.print("Conectando a ");
    Serial.println(ssid);
    
    WiFi.begin(ssid, password);
    
    int tentativas = 0;
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
        tentativas++;
        if (tentativas > 20) {
            Serial.println("\nFalha ao conectar ao Wi-Fi. Reiniciando...");
            ESP.restart();
        }
    }

    Serial.println("\nWi-Fi conectado!");
    Serial.print("IP da Escrava: ");
    Serial.println(WiFi.localIP());
    udp.begin(udp_port); // Inicia UDP para envio

    last_time = millis();
}

void loop() {
    unsigned long current_time = millis();
    float delta_time = (current_time - last_time) / 1000.0;

    // --- LEITURA DO ANGULO ---
    sensors_event_t a1, g1, temp1; mpuQuadril.getEvent(&a1, &g1, &temp1);
    sensors_event_t a2, g2, temp2; mpuCoxa.getEvent(&a2, &g2, &temp2);

    float pitchQuadril_acc = atan2(a1.acceleration.y, a1.acceleration.z) * 57.2958;
    float pitchCoxa_acc = atan2(a2.acceleration.y, a2.acceleration.z) * 57.2958;

    pitchQuadril = COMPL_FILTER_ALPHA * (pitchQuadril + g1.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitchQuadril_acc;
    pitchCoxa = COMPL_FILTER_ALPHA * (pitchCoxa + g2.gyro.x * delta_time) + (1.0 - COMPL_FILTER_ALPHA) * pitchCoxa_acc;
    last_time = current_time;

    // --- LEITURA ANALÓGICA ---
    int emg_val = analogRead(EMG_PIN);
    int ecg_val = analogRead(ECG_PIN);
    float final_angle = fabs(pitchQuadril - pitchCoxa); 

    // --- ENVIAR DADOS VIA UDP ---
    // Formato: "ID,ANGULO,EMG,ECG"
    char buffer_dados[100];
    sprintf(buffer_dados, "%s,%.2f,%d,%d",
        ID_DISPOSITIVO,
        final_angle,
        emg_val,
        ecg_val
    );

    // Envio
    udp.beginPacket(host_ip, udp_port);
    udp.print(buffer_dados); 
    udp.endPacket();
    
    // Print para debug (Serial USB)
    Serial.println(buffer_dados);

    // Alta Frequência
    delay(1); 
}