# Projeto PBL – Plataforma de Reabilitação Pós-AVC

Repositório base para o protótipo que integra captura de sinais EMG/ECG com uma
interface clínica construída em Streamlit. O objetivo é apoiar equipes médicas na
avaliação contínua de pacientes pós-AVC.

```
projeto_pbl/
Projeto PBL – Plataforma de Reabilitação Pós-AVCRepositório base para o protótipo que integra captura de sinais EMG/ECG com umainterface clínica construída em Streamlit. O objetivo é apoiar equipes médicas naavaliação contínua de pacientes pós-AVC.projeto_pbl/
├── hardware/
│   └── esp32/
│       └── esp32_emg_ecg.ino     # Firmware para o microcontrolador
├── software/
│   ├── data_capture/
│   │   └── serial_plotter.py     # (Opcional) Leitor de debug via serial
│   └── dashboard/
│       ├── __init__.py           # Marca o diretório como pacote Python
│       ├── app.py                # Aplicação Streamlit com dashboards
│       └── database.py           # Camada de persistência (SQLite)
├── data/
│   └── clinic.db                 # Banco de dados SQLite (ignorado pelo .gitignore)
├── .gitignore
├── README.md
└── requirements.txt
```

## Pré-requisitos

- Python 3.10 ou superior.
- Pip ou outro gerenciador de pacotes compatível.
- (Opcional) Arduino IDE para gravar o firmware na ESP32.

Instale as dependências Python com:

```bash
pip install -r requirements.txt
```

> **Nota:** Assumindo que `requirements.txt` contém `streamlit`, `pandas`, `plotly`,
> `numpy`, `pyserial` e `scipy`.

## Firmware ESP32

1. Abra o arquivo `hardware/esp32/esp32_emg_ecg.ino` na Arduino IDE.
2. Ajuste os pinos `ECG_PIN` e `EMG_PIN` conforme seu circuito.
3. Faça o upload para a placa ESP32 com a taxa de transmissão em 115200 baud.

As leituras são enviadas em linhas no formato `ECG: <valor>, EMG: <valor>` para a
porta serial.

## Captura e Visualização dos Sinais (Debug)

O script `software/data_capture/serial_plotter.py` é uma ferramenta de debug opcional.
Ele lê o monitor serial e plota os sinais brutos em tempo real.

```bash
# Para testar o hardware sem o dashboard
python software/data_capture/serial_plotter.py --port COM3
```

## Painel Clínico Streamlit

O painel principal é o `software/dashboard/app.py`. Ele simula o acompanhamento de
sessões, guarda o histórico de cada paciente em um banco SQLite (`data/clinic.db`) e
exibe métricas de desempenho.

```bash
streamlit run software/dashboard/app.py
```

Ao abrir o painel, você pode cadastrar novos pacientes através do formulário na barra
lateral. As sessões simuladas coletadas são associadas ao paciente selecionado e
salvas automaticamente no banco de dados.

## Estrutura do Banco de Dados

O arquivo `data/clinic.db` contém duas tabelas:

- `patients(id, name)` – Lista dos pacientes cadastrados na clínica.
- `sessions(id, patient_id, collected_at, payload_json)` – Histórico das sessões de
  monitoramento, com os dados da sessão (time, le_quad, etc.) armazenados em JSON.

Para inspecionar o banco fora do Streamlit, utilize qualquer ferramenta SQLite.

## Próximos Passos

- [x] Garantir que o `app.py` (simulado) salve e carregue sessões perfeitamente do `database.py`.
- [ ] Integrar os sinais reais (leitura da serial e filtros) diretamente no `app.py`,
      substituindo o loop de simulação.
- [ ] Adicionar os sensores de IMU (angulação do quadril) ao firmware e ao `app.py`.
- [ ] Documentar protocolos de avaliação clínica e métricas utilizadas.
