import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import argparse

# --- Argumentos de Linha de Comando ---
parser = argparse.ArgumentParser(description='Plota dados seriais do ESP32 (EMG, ECG, 2x IMU)')
parser.add_argument(
    '--port', 
    type=str, 
    required=True, 
    help='Porta serial (ex: COM3 no Windows, /dev/ttyUSB0 no Linux)'
)
parser.add_argument(
    '--baud', 
    type=int, 
    default=115200, 
    help='Baud rate (padrão: 115200)'
)
args = parser.parse_args()

# --- Configurações ---
BAUD = args.baud
PORT = args.port
FS = 100  # Taxa de amostragem esperada (Hz)
N_CHANNELS = 14 # Número de canais que o Arduino está enviando
WINDOW_SIZE = FS * 5 # Janela de 5 segundos

# --- Buffers de Dados (um deque para cada canal) ---
# Vamos armazenar todos os 14 canais, mesmo que só plotemos 4
data_buffers = [deque([0.0] * WINDOW_SIZE, maxlen=WINDOW_SIZE) for _ in range(N_CHANNELS)]

# --- Configuração do Gráfico (4 subplots) ---
plt.ion()
fig, ax = plt.subplots(4, 1, figsize=(10, 8), constrained_layout=True)
fig.suptitle(f"Debug dos Sensores da Perna (Porta: {PORT})", fontsize=16)
x_axis = np.arange(0, WINDOW_SIZE)

# Nomes dos gráficos (vamos plotar 4 dos 14)
plot_indices = [0, 1, 2, 8] # [EMG, ECG, IMU1_Ax, IMU2_Ax]
plot_titles = [
    'Canal 0: EMG (Quadríceps)',
    'Canal 1: ECG (Isquiotibial)',
    'Canal 2: IMU 1 - Acel. X (Quadril)',
    'Canal 8: IMU 2 - Acel. X (Coxa)'
]

# Criar as linhas do gráfico
lines = []
for i in range(4):
    idx = plot_indices[i]
    ln, = ax[i].plot(x_axis, data_buffers[idx], lw=1)
    ax[i].set_title(plot_titles[i])
    ax[i].set_ylim(0, 4096) # Limite padrão para analógicos
    lines.append(ln)

# Ajustar os limites Y dos IMUs
ax[2].set_ylim(-20, 20) # Acelerômetro (em m/s^2)
ax[3].set_ylim(-20, 20) # Acelerômetro (em m/s^2)

t_last_draw = time.time()

# --- Conexão Serial ---
try:
    ser = serial.Serial(PORT, BAUD, timeout=0.1)
    print(f"Conectado a {PORT} em {BAUD} baud.")
except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial {PORT}: {e}")
    exit()

time.sleep(1.0) # Espera o ESP32 resetar
ser.flushInput()

# --- Loop Principal de Leitura e Plot ---
try:
    while True:
        line = ser.readline()
        if not line:
            continue
        
        try:
            # Decodifica a linha (bytes -> string) e remove espaços em branco
            line_str = line.decode('utf-8').strip()
            
            # Divide a string CSV em uma lista de valores
            values_str = line_str.split(',')
            
            # Verifica se recebemos o número correto de canais
            if len(values_str) != N_CHANNELS:
                print(f"Linha mal formatada (esperava {N_CHANNELS}, recebeu {len(values_str)}): {line_str}")
                continue

            # Converte todos os valores de string para float
            values_float = [float(v) for v in values_str]

            # Adiciona cada valor ao seu respectivo buffer
            for i in range(N_CHANNELS):
                data_buffers[i].append(values_float[i])
        
        except (UnicodeDecodeError, ValueError) as e:
            print(f"Erro no parsing: {e} | Linha: {line_str}")
            continue
        
        # --- Atualização do Gráfico (a ~30Hz para economizar CPU) ---
        if time.time() - t_last_draw > (1/30):
            t_last_draw = time.time()
            
            # Atualiza os dados das 4 linhas que estamos plotando
            for i in range(4):
                idx = plot_indices[i]
                lines[i].set_ydata(data_buffers[idx])
            
            # Reajusta os limites Y dos analógicos (EMG/ECG)
            min_emg = np.min(data_buffers[0])
            max_emg = np.max(data_buffers[0])
            ax[0].set_ylim(min_emg * 0.9, max_emg * 1.1)
            
            min_ecg = np.min(data_buffers[1])
            max_ecg = np.max(data_buffers[1])
            ax[1].set_ylim(min_ecg * 0.9, max_ecg * 1.1)

            # Redesenha o gráfico
            plt.pause(0.001)

except KeyboardInterrupt:
    print("\nFinalizado pelo usuário.")
finally:
    ser.close()
    plt.ioff()
    plt.show() # Mostra o gráfico final estático
    print("Porta serial fechada.")
