# Projeto PBL – Plataforma de Reabilitação Pós-AVC

Repositório base para o protótipo que integra captura de sinais EMG/ECG com uma
interface clínica construída em Streamlit. O objetivo é apoiar equipes médicas na
avaliação contínua de pacientes pós-AVC, começando com uma prova de conceito que
simula os dados reais.

## Visão Geral

O projeto é composto por três partes principais:

1. **Firmware ESP32** – Código Arduino responsável por ler sensores de EMG/ECG e
   transmitir as amostras via serial.
2. **Ferramenta de Captura** – Script Python que recebe os dados pela porta serial
   (ou gera dados simulados) e exibe dois gráficos em tempo real para depuração.
3. **Painel Clínico** – Aplicação Streamlit que apresenta visualmente os dados do
   paciente e simula o acompanhamento de sessões de reabilitação.

```
projeto_pbl/
├── hardware/
│   └── esp32/
│       └── esp32_emg_ecg.ino     # Firmware para o microcontrolador
├── software/
│   ├── data_capture/
│   │   └── serial_plotter.py     # Leitor/plotter dos dados via serial
│   └── dashboard/
│       ├── __init__.py           # Marca o diretório como pacote Python
│       ├── app.py                # Aplicação Streamlit com dashboards
│       └── database.py           # Camada de persistência (SQLite)
│       └── app.py                # Aplicação Streamlit com dashboards
├── data/
│   └── README.md                 # Orientações sobre arquivos de sessão
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

## Firmware ESP32

1. Abra o arquivo [`hardware/esp32/esp32_emg_ecg.ino`](hardware/esp32/esp32_emg_ecg.ino) na Arduino IDE.
2. Ajuste os pinos `ECG_PIN` e `EMG_PIN` conforme seu circuito.
3. Faça o upload para a placa ESP32 com a taxa de transmissão em 115200 baud.

As leituras são enviadas em linhas no formato `ECG: <valor>, EMG: <valor>` para a
porta serial, prontas para consumo pelo script Python.

## Captura e Visualização dos Sinais

O script [`software/data_capture/serial_plotter.py`](software/data_capture/serial_plotter.py)
lê o monitor serial e plota os sinais EMG/ECG em tempo real. Execute-o com:

```bash
python software/data_capture/serial_plotter.py --port COM3 --baud 115200
```

Substitua `COM3` pela porta correspondente no seu sistema (por exemplo,
`/dev/ttyUSB0` no Linux). Caso não tenha o hardware conectado, utilize o modo de
demonstração para visualizar dados sintéticos:

```bash
python software/data_capture/serial_plotter.py --demo
```

## Painel Clínico Streamlit

O painel simula o acompanhamento de sessões, guarda o histórico de cada paciente
em um banco SQLite (`data/clinic.db`) e exibe métricas de desempenho. Para
executar:
na pasta `data/` e exibe métricas de desempenho. Para executar:

```bash
streamlit run software/dashboard/app.py
```

Ao abrir o painel você pode cadastrar novos pacientes através do formulário na
barra lateral. As sessões coletadas (mesmo em modo simulado) são associadas ao
paciente selecionado e salvas automaticamente no banco de dados. O arquivo é
ignorado pelo Git para que informações clínicas reais não sejam versionadas.

### Estrutura do Banco de Dados

O arquivo `data/clinic.db` contém duas tabelas:

- `patients(id, name)` – Lista dos pacientes cadastrados na clínica.
- `sessions(id, patient_id, collected_at, payload_json)` – Histórico das sessões
  de monitoramento, com os dados da sessão armazenados em JSON.

Para inspecionar o banco fora do Streamlit, utilize qualquer ferramenta SQLite,
por exemplo:

```bash
sqlite3 data/clinic.db ".tables"
```

Ou exporte os dados para CSV:

```bash
sqlite3 -header -csv data/clinic.db "SELECT * FROM sessions;" > data/sessions.csv
```
Por padrão os arquivos de sessão são salvos como `data/Paciente_A.json`,
`data/Paciente_B.json`, etc. Esses arquivos são ignorados pelo Git para evitar que
dados sensíveis sejam versionados.

## Próximos Passos

- Integrar os sinais reais provenientes do `serial_plotter.py` diretamente no painel
  Streamlit.
- Definir pipeline de processamento dos sinais (filtros, normalização, métricas).
- Documentar protocolos de avaliação clínica e métricas utilizadas.

Sinta-se à vontade para abrir issues ou PRs com melhorias e sugestões!
