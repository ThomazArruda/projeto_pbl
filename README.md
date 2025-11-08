Projeto PBL – Plataforma de Reabilitação Pós-AVCRepositório base para o protótipo que integra captura de sinais EMG/ECG com umainterface clínica construída em Streamlit. O objetivo é apoiar equipes médicas naavaliação contínua de pacientes pós-AVC.
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
│   └── clinic.db               # Banco de dados SQLite (ignorado pelo .gitignore)
├── .gitignore
├── README.md
└── requirements.txt
Pré-requisitosPython 3.10 ou superior.Pip ou outro gerenciador de pacotes compatível.(Opcional) Arduino IDE para gravar o firmware na ESP32.Instale as dependências Python com:pip install -r requirements.txt
(Assumindo que requirements.txt contém streamlit, pandas, plotly, numpy, pyserial, scipy)Firmware ESP32Abra o arquivo hardware/esp32/esp32_emg_ecg.ino na Arduino IDE.Ajuste os pinos ECG_PIN e EMG_PIN conforme seu circuito.Faça o upload para a placa ESP32 com a taxa de transmissão em 115200 baud.As leituras são enviadas em linhas no formato ECG: <valor>, EMG: <valor> para aporta serial.Captura e Visualização dos Sinais (Debug)O script software/data_capture/serial_plotter.pyé uma ferramenta de debug opcional. Ele lê o monitor serial e plota os sinais brutos em tempo real.# Para testar o hardware sem o dashboard
python software/data_capture/serial_plotter.py --port COM3
Painel Clínico StreamlitO painel principal é o software/dashboard/app.py.Ele simula o acompanhamento de sessões, guarda o histórico de cada pacienteem um banco SQLite (data/clinic.db) e exibe métricas de desempenho.Para executar o painel (em modo simulado):streamlit run software/dashboard/app.py
Ao abrir o painel, você pode cadastrar novos pacientes através do formulário nabarra lateral. As sessões simuladas coletadas são associadas aopaciente selecionado e salvas automaticamente no banco de dados.<!--NOTA PARA VOCÊ: Removi todo o texto sobre arquivos .json.Agora está claro que o clinic.db é o único método.-->Estrutura do Banco de DadosO arquivo data/clinic.db contém duas tabelas:patients(id, name) – Lista dos pacientes cadastrados na clínica.sessions(id, patient_id, collected_at, payload_json) – Histórico das sessõesde monitoramento, com os dados da sessão (time, le_quad, etc.) armazenados em JSON.Para inspecionar o banco fora do Streamlit, utilize qualquer ferramenta SQLite.Próximos Passos[X] Garantir que o app.py (simulado) salve e carregue sessões perfeitamente do database.py.[ ] Integrar os sinais reais (leitura da serial e filtros) diretamente no app.py, substituindo o loop de simulação.[ ] Adicionar os sensores de IMU (angulação do quadril) ao firmware e ao app.py.[ ] Documentar protocolos de avaliação clínica e métricas utilizadas.
