import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import argparse
import csv # <--- NOVO: Importa a biblioteca para salvar CSV

# --- Argumentos de Linha de Comando ---
parser = argparse.ArgumentParser(description='Plota e Grava dados seriais do ESP32')
parser.add_argument('--port', type=str, required=True, help='Porta serial (ex: COM3)')
parser.add_argument('--baud', type=int, default=115200, help='Baud rate')
# --- NOVO ARGUMENTO PARA SALVAR ---
parser.add_argument(
    '-o', '--output', 
    type=str, 
    help='(Opcional) Nome do arquivo .csv para salvar os dados (ex: paciente_01.csv)'
)
args = parser.parse_args()

# --- Configurações ---
PORT = args.port
BAUD = args.baud
FILENAME = args.output
FS = 100
WINDOW_SIZE = FS * 5 # Janela de 5 segundos (500 amostras)

# --- Buffers de Dados ---
emg_data = deque([0.0] * WINDOW_SIZE, maxlen=WINDOW_SIZE)
ecg_data = deque([0.0] * WINDOW_SIZE, maxlen=WINDOW_SIZE)
angle_data = deque([0.0] * WINDOW_SIZE, maxlen=WINDOW_SIZE)

# --- Setup do Arquivo CSV (Se o nome foi fornecido) ---
csv_file = None
csv_writer = None
if FILENAME:
    try:
        # 'newline=""' é importante para arquivos CSV
        csv_file = open(FILENAME, 'w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file)
        # Escreve o Cabeçalho (Header)
        csv_writer.writerow(['timestamp_ms', 'emg_quad', 'ecg_isquio', 'angulo_relativo'])
        print(f"Salvando dados em: {FILENAME}")
    except Exception as e:
        print(f"Erro ao abrir o arquivo CSV: {e}")
        print("Continuando sem salvar.")
        csv_file = None
        csv_writer = None

# --- Conexão Serial ---
try:
    ser = serial.Serial(PORT, BAUD, timeout=0.01)
    print(f"Conectado a {PORT} em {BAUD} baud.")
except serial.SerialException as e:
    print(f"Erro ao abrir a porta serial {PORT}: {e}")
    if csv_file:
        csv_file.close()
    exit()

time.sleep(1.0)
ser.flushInput()
start_time = time.time() # Pega o tempo inicial

# --- Configuração do Gráfico (Mesma de antes) ---
fig, ax = plt.subplots(2, 1, figsize=(10, 7), constrained_layout=True)
fig.suptitle(f"Debug dos Sensores da Perna (Porta: {PORT})", fontsize=16)
x_axis = np.arange(0, WINDOW_SIZE)

ln_emg, = ax[0].plot(x_axis, [0]*WINDOW_SIZE, lw=1, color='blue', label='EMG (Quad)')
ln_ecg, = ax[0].plot(x_axis, [0]*WINDOW_SIZE, lw=1, color='red', label='ECG (Isquio)')
ax[0].set_title('Músculos Agonista vs. Antagonista')
ax[0].set_ylim(0, 4096)
ax[0].legend(loc='upper left')

ln_angle, = ax[1].plot(x_axis, [0]*WINDOW_SIZE, lw=1, color='green', label='Ângulo Relativo (IMU1 - IMU2)')
ax[1].set_title('Ângulo Relativo (Quadril vs. Coxa)')
ax[1].set_ylim(0, 180) 
ax[1].legend(loc='upper left')
ax[1].grid(True)

# --- Função de Atualização (com lógica de salvar) ---
def update_plot(frame):
    
    while ser.in_waiting > 0:
        try:
            line = ser.readline()
            if not line:
                continue
            
            # Pega o timestamp o mais cedo possível
            current_time_ms = int((time.time() - start_time) * 1000)
            
            line_str = line.decode('utf-8').strip()
            
            parts = line_str.split(',')
            if len(parts) != 3:
                continue 

            val_emg = int(parts[0].split(':')[1])
            val_ecg = int(parts[1].split(':')[1])
            val_angle = float(parts[2].split(':')[1])

            emg_data.append(val_emg)
            ecg_data.append(val_ecg)
            angle_data.append(val_angle)

            # --- LÓGICA DE SALVAR ---
            if csv_writer:
                csv_writer.writerow([current_time_ms, val_emg, val_ecg, val_angle])

        except (UnicodeDecodeError, ValueError, IndexError):
            continue
            
    # Atualiza os gráficos (mesma lógica de antes)
    ln_emg.set_ydata(emg_data)
    ln_ecg.set_ydata(ecg_data)
    ln_angle.set_ydata(angle_data)

    min_val = min(np.min(emg_data), np.min(ecg_data))
    max_val = max(np.max(emg_data), np.max(ecg_data))
    ax[0].set_ylim(min_val * 0.9, max_val * 1.1)
    
    return ln_emg, ln_ecg, ln_angle

# --- Inicia a Animação ---
ani = animation.FuncAnimation(fig, update_plot, 
                              interval=10, 
                              blit=True, 
                              cache_frame_data=False)

try:
    plt.show()
except KeyboardInterrupt:
    print("\nFinalizado pelo usuário.")
finally:
    ser.close()
    if csv_file: # <--- NOVO: Fecha o arquivo CSV
        csv_file.close()
        print(f"Dados salvos com sucesso em {FILENAME}")
    print("Porta serial fechada.")
