import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import argparse
import re
import csv

# --- Argumentos de Linha de Comando ---
parser = argparse.ArgumentParser(description='Plota e Grava 6 canais via Bluetooth')
parser.add_argument('--port', type=str, required=True, help='Porta serial Bluetooth (ex: COM5)')
parser.add_argument('--baud', type=int, default=115200, help='Baud rate')
parser.add_argument('-o', '--output', type=str, help='Nome do arquivo .csv para salvar (opcional)')
args = parser.parse_args()

# --- Configurações ---
PORT = args.port
BAUD = args.baud
FILENAME = args.output
FS = 100
WINDOW_SIZE = FS * 5 

# --- Buffers (6 canais) ---
emg1_data = deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE)
ecg1_data = deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE)
angle1_data = deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE)
emg2_data = deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE)
ecg2_data = deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE)
angle2_data = deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE)

# --- Setup do CSV ---
csv_file = None; csv_writer = None
if FILENAME:
    try:
        csv_file = open(FILENAME, 'w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(['timestamp_ms', 'EMG1', 'ECG1', 'Angle1', 'EMG2', 'ECG2', 'Angle2'])
        print(f"Salvando em: {FILENAME}")
    except Exception as e:
        print(f"Erro CSV: {e}"); csv_file = None

# --- Conexão Bluetooth ---
try:
    ser = serial.Serial(PORT, BAUD, timeout=0.01)
    print(f"Conectado a {PORT}")
except serial.SerialException as e:
    print(f"Erro na porta {PORT}: {e}"); exit()

time.sleep(1.0); ser.flushInput(); start_time = time.time()

# --- Gráficos ---
fig, ax = plt.subplots(3, 1, figsize=(10, 9), constrained_layout=True)
x = np.arange(0, WINDOW_SIZE)

ln_e1, = ax[0].plot(x, [0]*WINDOW_SIZE, 'b', label='EMG Perna 1')
ln_e2, = ax[0].plot(x, [0]*WINDOW_SIZE, 'c', label='EMG Perna 2')
ax[0].set_title('EMG (Quadríceps)'); ax[0].set_ylim(0, 4096); ax[0].legend(loc='upper left')

ln_c1, = ax[1].plot(x, [0]*WINDOW_SIZE, 'r', label='ECG Perna 1')
ln_c2, = ax[1].plot(x, [0]*WINDOW_SIZE, 'm', label='ECG Perna 2')
ax[1].set_title('ECG (Isquiotibiais)'); ax[1].set_ylim(0, 4096); ax[1].legend(loc='upper left')

ln_a1, = ax[2].plot(x, [0]*WINDOW_SIZE, 'g', label='Ângulo Perna 1')
ln_a2, = ax[2].plot(x, [0]*WINDOW_SIZE, 'lime', label='Ângulo Perna 2')
ax[2].set_title('Ângulo Relativo'); ax[2].set_ylim(0, 180); ax[2].legend(loc='upper left')

# Regex: E1:val,C1:val,A1:val,E2:val,C2:val,A2:val
regex = re.compile(r"E1:(\d+),C1:(\d+),A1:([\d\.]+),E2:(\d+),C2:(\d+),A2:([\d\.]+)")

def update(frame):
    while ser.in_waiting > 0:
        try:
            line = ser.readline()
            if not line: continue
            txt = line.decode('utf-8').strip()
            m = regex.match(txt)
            if not m: continue
            
            e1, c1, a1, e2, c2, a2 = m.groups()
            e1, c1, a1 = int(e1), int(c1), float(a1)
            e2, c2, a2 = int(e2), int(c2), float(a2)
            
            emg1_data.append(e1); ecg1_data.append(c1); angle1_data.append(a1)
            emg2_data.append(e2); ecg2_data.append(c2); angle2_data.append(a2)
            
            if csv_writer:
                t_ms = int((time.time()-start_time)*1000)
                csv_writer.writerow([t_ms, e1, c1, a1, e2, c2, a2])
                
        except Exception: continue

    ln_e1.set_ydata(emg1_data); ln_e2.set_ydata(emg2_data)
    ln_c1.set_ydata(ecg1_data); ln_c2.set_ydata(ecg2_data)
    ln_a1.set_ydata(angle1_data); ln_a2.set_ydata(angle2_data)
    
    # Auto-scale Y para EMG/ECG
    all_emg = list(emg1_data) + list(emg2_data)
    if all_emg: ax[0].set_ylim(min(all_emg)*0.9, max(all_emg)*1.1)
    
    all_ecg = list(ecg1_data) + list(ecg2_data)
    if all_ecg: ax[1].set_ylim(min(all_ecg)*0.9, max(all_ecg)*1.1)

    return ln_e1, ln_e2, ln_c1, ln_c2, ln_a1, ln_a2

ani = animation.FuncAnimation(fig, update, interval=10, blit=True, cache_frame_data=False)
try: plt.show()
except: pass
finally: 
    ser.close()
    if csv_file: csv_file.close()