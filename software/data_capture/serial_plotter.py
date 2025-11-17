import serial
import time
# ... (código existente inalterado) ...
import csv # <--- NOVO: Importa a biblioteca para salvar CSV

# --- Argumentos de Linha de Comando ---
# ... (código existente inalterado) ...
# --- Setup do Arquivo CSV (Se o nome foi fornecido) ---
csv_file = None
csv_writer = None
if FILENAME:
    try:
        # 'newline=""' é importante para arquivos CSV
        csv_file = open(FILENAME, 'w', newline='', encoding='utf-8')
        
        # --- CORREÇÃO 1: Mudar o delimitador para PONTO E VÍRGULA ---
        # Isso faz o Excel abrir o arquivo corretamente em colunas separadas
        csv_writer = csv.writer(csv_file, delimiter=';') 
        
        # --- CORREÇÃO 2: Cabeçalho formatado com unidades ---
        csv_writer.writerow(['timestamp (ms)', 'EMG_Quadriceps (raw)', 'ECG_Isquiotibiais (raw)', 'Angulo_Relativo (graus)'])
        
        print(f"Salvando dados em: {FILENAME}")
    except Exception as e:
# ... (código existente inalterado) ...
# --- Conexão Serial ---
try:
    ser = serial.Serial(PORT, BAUD, timeout=0.01)
# ... (código existente inalterado) ...
# --- Função de Atualização (com lógica de salvar) ---
def update_plot(frame):
    
    while ser.in_waiting > 0:
# ... (código existente inalterado) ...
            val_ecg = int(parts[1].split(':')[1])
            val_angle = float(parts[2].split(':')[1])

            emg_data.append(val_emg)
# ... (código existente inalterado) ...
            # --- LÓGICA DE SALVAR ---
            if csv_writer:
                csv_writer.writerow([current_time_ms, val_emg, val_ecg, val_angle])

        except (UnicodeDecodeError, ValueError, IndexError):
# ... (código existente inalterado) ...
# --- Inicia a Animação ---
ani = animation.FuncAnimation(fig, update_plot, 
                              interval=10, 
# ... (código existente inalterado) ...
finally:
    ser.close()
    if csv_file: # <--- NOVO: Fecha o arquivo CSV
# ... (código existente inalterado) ...
