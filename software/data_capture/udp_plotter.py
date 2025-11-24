import socket
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import argparse
import csv

# --- Configurações ---
UDP_IP = "0.0.0.0"
UDP_PORT = 4210
FS = 200 # Tentativa de aumentar frequência no buffer
WINDOW_SIZE = FS * 5 

# --- Argumentos ---
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, help='Nome do arquivo .csv')
args = parser.parse_args()

# --- Buffers ---
data_store = {
    "ESQ": { "angle": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "emg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "ecg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "last_seen": 0.0 },
    "DIR": { "angle": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "emg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "ecg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "last_seen": 0.0 }
}

# --- Rede ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)
print(f"--- Monitor V3 (6 Gráficos) ---")
print(f"Escutando na porta {UDP_PORT}...")

# --- CSV ---
csv_file = None; csv_writer = None
if args.output:
    try:
        csv_file = open(args.output, 'w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(['timestamp', 'ID', 'Angle', 'EMG', 'ECG'])
        print(f"Gravando em: {args.output}")
    except Exception as e: print(f"Erro CSV: {e}")

start_time = time.time()

# --- Configuração dos 6 Gráficos (3 linhas, 2 colunas) ---
# Coluna 0 = Esquerda, Coluna 1 = Direita
fig, axs = plt.subplots(3, 2, figsize=(14, 8), constrained_layout=True)
x = np.arange(0, WINDOW_SIZE)

# Títulos das Colunas
axs[0, 0].set_title("PERNA ESQUERDA - Ângulo", fontsize=10, color='blue')
axs[0, 1].set_title("PERNA DIREITA - Ângulo", fontsize=10, color='red')

# Configuração Linha 0: Ângulo
ln_ang_esq, = axs[0, 0].plot(x, [0]*WINDOW_SIZE, 'b', lw=1.5)
axs[0, 0].set_ylim(0, 180); axs[0, 0].grid(alpha=0.3)

ln_ang_dir, = axs[0, 1].plot(x, [0]*WINDOW_SIZE, 'r', lw=1.5)
axs[0, 1].set_ylim(0, 180); axs[0, 1].grid(alpha=0.3)

# Configuração Linha 1: EMG
axs[1, 0].set_title("EMG (Quadríceps)", fontsize=9)
ln_emg_esq, = axs[1, 0].plot(x, [0]*WINDOW_SIZE, 'b', lw=1)
axs[1, 0].set_ylim(0, 4096); axs[1, 0].grid(alpha=0.3)

axs[1, 1].set_title("EMG (Quadríceps)", fontsize=9)
ln_emg_dir, = axs[1, 1].plot(x, [0]*WINDOW_SIZE, 'r', lw=1)
axs[1, 1].set_ylim(0, 4096); axs[1, 1].grid(alpha=0.3)

# Configuração Linha 2: ECG
axs[2, 0].set_title("ECG (Isquiotibiais)", fontsize=9)
ln_ecg_esq, = axs[2, 0].plot(x, [0]*WINDOW_SIZE, 'b', lw=1)
axs[2, 0].set_ylim(0, 4096); axs[2, 0].grid(alpha=0.3)

axs[2, 1].set_title("ECG (Isquiotibiais)", fontsize=9)
ln_ecg_dir, = axs[2, 1].plot(x, [0]*WINDOW_SIZE, 'r', lw=1)
axs[2, 1].set_ylim(0, 4096); axs[2, 1].grid(alpha=0.3)

# Status Text
txt_status_esq = axs[0, 0].text(0.05, 0.85, "OFF", transform=axs[0, 0].transAxes, fontweight='bold', color='gray')
txt_status_dir = axs[0, 1].text(0.05, 0.85, "OFF", transform=axs[0, 1].transAxes, fontweight='bold', color='gray')

def update(frame):
    # Lê TUDO do buffer de rede
    while True:
        try:
            data, _ = sock.recvfrom(1024) 
            parts = data.decode('utf-8').strip().split(',')
            
            if len(parts) == 4:
                dev_id, angle, emg, ecg = parts[0], float(parts[1]), int(parts[2]), int(parts[3])
                
                if dev_id in data_store:
                    data_store[dev_id]["angle"].append(angle)
                    data_store[dev_id]["emg"].append(emg)
                    data_store[dev_id]["ecg"].append(ecg)
                    data_store[dev_id]["last_seen"] = time.time()
                    
                    if csv_writer:
                        t = round(time.time() - start_time, 4)
                        csv_writer.writerow([t, dev_id, angle, emg, ecg])
        except BlockingIOError: break
        except: continue

    # Atualiza Linhas
    ln_ang_esq.set_ydata(data_store["ESQ"]["angle"])
    ln_emg_esq.set_ydata(data_store["ESQ"]["emg"])
    ln_ecg_esq.set_ydata(data_store["ESQ"]["ecg"])

    ln_ang_dir.set_ydata(data_store["DIR"]["angle"])
    ln_emg_dir.set_ydata(data_store["DIR"]["emg"])
    ln_ecg_dir.set_ydata(data_store["DIR"]["ecg"])

    # Atualiza Status
    now = time.time()
    # Status Esq
    if now - data_store["ESQ"]["last_seen"] < 1.0:
        txt_status_esq.set_text("CONECTADO")
        txt_status_esq.set_color("green")
    else:
        txt_status_esq.set_text("DESCONECTADO")
        txt_status_esq.set_color("red")
    
    # Status Dir
    if now - data_store["DIR"]["last_seen"] < 1.0:
        txt_status_dir.set_text("CONECTADO")
        txt_status_dir.set_color("green")
    else:
        txt_status_dir.set_text("DESCONECTADO")
        txt_status_dir.set_color("red")

    return ln_ang_esq, ln_emg_esq, ln_ecg_esq, ln_ang_dir, ln_emg_dir, ln_ecg_dir, txt_status_esq, txt_status_dir

ani = animation.FuncAnimation(fig, update, interval=20, blit=True, cache_frame_data=False)
plt.show()
if csv_file: csv_file.close()
