import socket
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import argparse
import csv
from scipy.signal import butter, filtfilt

# --- Configurações ---
UDP_IP = "0.0.0.0"
UDP_PORT = 4210
FS = 100 # Frequência de Amostragem estimada (Hz)
WINDOW_SIZE = FS * 5 

# --- Configuração dos Filtros ---
# Filtro Passa-Baixa de 4Hz (Envelope)
def create_lowpass_filter(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Coeficientes do filtro (4Hz corte, para FS=100)
b_low, a_low = create_lowpass_filter(4, FS, order=4)

# --- Função de Processamento (O Segredo do "Clean") ---
def process_signal(raw_data):
    # Converte para numpy para ser rápido
    sig = np.array(raw_data)
    
    # 1. Remover Offset (Centralizar no zero)
    # Subtrai a média da janela para remover o componente DC
    sig = sig - np.mean(sig)
    
    # 2. Retificação (Valor Absoluto)
    sig = np.abs(sig)
    
    # 3. Envelope (Filtro Passa-Baixa 4Hz)
    # Usamos filtfilt para não ter atraso de fase (lag) no filtro
    if len(sig) > 15: # Precisa de dados mínimos para filtrar
        try:
            sig = filtfilt(b_low, a_low, sig)
        except: pass # Se der erro no filtro (muito curto), retorna o retificado
        
    return sig

# --- Argumentos ---
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, help='Nome do arquivo .csv')
args = parser.parse_args()

# --- Buffers ---
# Guardamos o dado BRUTO. O processamento é feito apenas na hora de plotar.
data_store = {
    "ESQ": { "angle": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "emg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "ecg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "last_seen": 0.0, "count": 0 },
    "DIR": { "angle": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "emg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "ecg": deque([0.0]*WINDOW_SIZE, maxlen=WINDOW_SIZE), "last_seen": 0.0, "count": 0 }
}

# --- Rede ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)
print(f"--- Monitor DSP Iniciado ---")
print(f"Frequência Alvo: {FS}Hz | Filtro Envelope: 4Hz")

# --- CSV ---
csv_file = None; csv_writer = None
if args.output:
    try:
        csv_file = open(args.output, 'w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(['timestamp', 'ID', 'Angle', 'EMG_Raw', 'ECG_Raw'])
        print(f"Gravando brutos em: {args.output}")
    except Exception as e: print(f"Erro CSV: {e}")

start_time = time.time()
last_fps_check = time.time()

# --- Configuração dos 6 Gráficos ---
fig, axs = plt.subplots(3, 2, figsize=(12, 9), constrained_layout=True)
x = np.arange(0, WINDOW_SIZE)

# Estilo
titles = ["ÂNGULO (Graus)", "EMG (Envelope 4Hz)", "ECG (Envelope 4Hz)"]
colors = ['green', 'blue', 'red']
ylims = [(0, 180), (0, 2000), (0, 2000)] # Ajuste os limites do EMG/ECG conforme a força

lines = {} # Dicionário para guardar as linhas do gráfico

for row in range(3):
    # Coluna Esquerda
    axs[row, 0].set_title(f"ESQ - {titles[row]}", fontsize=10, fontweight='bold')
    ln_esq, = axs[row, 0].plot(x, [0]*WINDOW_SIZE, color=colors[row], lw=1.5)
    axs[row, 0].set_ylim(ylims[row]); axs[row, 0].grid(alpha=0.3)
    lines[f"ESQ_{row}"] = ln_esq
    
    # Coluna Direita
    axs[row, 1].set_title(f"DIR - {titles[row]}", fontsize=10, fontweight='bold')
    ln_dir, = axs[row, 1].plot(x, [0]*WINDOW_SIZE, color=colors[row], lw=1.5)
    axs[row, 1].set_ylim(ylims[row]); axs[row, 1].grid(alpha=0.3)
    lines[f"DIR_{row}"] = ln_dir

# Texto de FPS no topo
txt_fps = fig.text(0.5, 0.98, "Aguardando dados...", ha='center', fontsize=10)

def update(frame):
    global last_fps_check
    
    # 1. Ler Rede
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
                    data_store[dev_id]["count"] += 1
                    
                    if csv_writer:
                        t = round(time.time() - start_time, 4)
                        csv_writer.writerow([t, dev_id, angle, emg, ecg])
        except BlockingIOError: break
        except: continue

    # 2. Calcular FPS Real (Diagnóstico)
    if time.time() - last_fps_check > 1.0:
        fps_esq = data_store["ESQ"]["count"]
        fps_dir = data_store["DIR"]["count"]
        data_store["ESQ"]["count"] = 0
        data_store["DIR"]["count"] = 0
        last_fps_check = time.time()
        txt_fps.set_text(f"Taxa Real: ESQ={fps_esq}Hz | DIR={fps_dir}Hz")
        # Alerta se a taxa estiver muito baixa
        if fps_esq < 10 or fps_dir < 10: txt_fps.set_color('red')
        else: txt_fps.set_color('black')

    # 3. Processar e Atualizar Gráficos
    # Ângulos (Não precisam de filtro pesado)
    lines["ESQ_0"].set_ydata(data_store["ESQ"]["angle"])
    lines["DIR_0"].set_ydata(data_store["DIR"]["angle"])

    # EMG (Pipeline: Remove DC -> Abs -> Filtro 4Hz)
    proc_emg_esq = process_signal(data_store["ESQ"]["emg"])
    lines["ESQ_1"].set_ydata(proc_emg_esq)
    
    proc_emg_dir = process_signal(data_store["DIR"]["emg"])
    lines["DIR_1"].set_ydata(proc_emg_dir)

    # ECG (Pipeline: Remove DC -> Abs -> Filtro 4Hz)
    proc_ecg_esq = process_signal(data_store["ESQ"]["ecg"])
    lines["ESQ_2"].set_ydata(proc_ecg_esq)
    
    proc_ecg_dir = process_signal(data_store["DIR"]["ecg"])
    lines["DIR_2"].set_ydata(proc_ecg_dir)

    # Auto-Scale suave para EMG/ECG (para não ficar estourado ou pequeno)
    # Pega o máximo dos últimos dados processados para ajustar a escala
    if len(proc_emg_esq) > 0:
        max_val = max(np.max(proc_emg_esq), np.max(proc_emg_dir), 100) # Mínimo 100 para não dar zoom no ruído
        axs[1, 0].set_ylim(0, max_val * 1.2)
        axs[1, 1].set_ylim(0, max_val * 1.2)

    if len(proc_ecg_esq) > 0:
        max_val = max(np.max(proc_ecg_esq), np.max(proc_ecg_dir), 100)
        axs[2, 0].set_ylim(0, max_val * 1.2)
        axs[2, 1].set_ylim(0, max_val * 1.2)

    return list(lines.values()) + [txt_fps]

ani = animation.FuncAnimation(fig, update, interval=30, blit=True, cache_frame_data=False)
plt.show()
if csv_file: csv_file.close()
