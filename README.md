# Projeto PBL – Plataforma de Reabilitação Pós-AVC

Repositório base para o protótipo que integra captura de sinais EMG/ECG e IMUs com uma
interface clínica em Streamlit. O objetivo é apoiar equipes médicas na avaliação
contínua de pacientes pós-AVC, desde a coleta no hardware até o painel de
acompanhamento.

## Estrutura do Repositório

```
projeto_pbl/
├── hardware/
│   └── esp32/
│       ├── esp32_leg_sensors.ino      # Leitura básica de EMG/ECG/IMU
│       ├── firmware_direita/
│       │   └── firmware_direita.ino    # Código perna direita
│       └── firmware_esquerdo/
│           └── firmware_esquerdo.ino   # Código perna esquerda
├── software/
│   ├── __init__.py
│   ├── data_capture/
│   │   └── udp_plotter.py          # Debug de sinais via wifi
│   └── dashboard/
│       ├── __init__.py
│       ├── app.py                     # Aplicação Streamlit
│       └── database.py                # Camada de persistência (SQLite)
├── data/
│   └── README.md                      # Orientações sobre `clinic.db` e exports
├── requirements.txt                   # Dependências do painel
└── README.md
```

- **hardware/** contém todos os firmwares para ESP32. Conectamos ambas as esps no mesmo hot spot
  que o computador.
- **software/** traz os componentes em Python. Use o `serial_plotter.py` para
  inspecionar o hardware antes do painel, e o diretório `dashboard` para a
  aplicação Streamlit com banco SQLite.
- **data/** guarda o banco `clinic.db` (ignorado pelo Git) e exportações geradas
  pelo app. Consulte `data/README.md` para os detalhes de uso e políticas de
  versionamento.

## Pré-requisitos

- Python 3.10 ou superior.
- Pip ou outro gerenciador de pacotes compatível.
- (Opcional) Arduino IDE para gravar o firmware na ESP32.

Instale as dependências Python com:

```bash
pip install -r requirements.txt
```

> **Nota:** O arquivo `requirements.txt` inclui `streamlit`, `pandas`, `plotly`,
> `numpy`, `pyserial` e `scipy`.

## Firmware ESP32

1. Abra o arquivo desejado em `hardware/esp32/` na Arduino IDE.
2. Ajuste os pinos dos sensores conforme seu circuito.
3. Faça o upload para a placa ESP32 com a taxa de transmissão em 115200 baud.

As leituras são enviadas no formato `ECG: <valor>, EMG: <valor>` para a porta
serial (firmwares mestre/escravo seguem o mesmo padrão, apenas dividindo os
sensores por placa).

## Captura e Visualização dos Sinais (Debug)

O script `software/data_capture/serial_plotter.py` é uma ferramenta de debug
opcional. Ele lê o monitor serial e plota os sinais brutos em tempo real.

```bash
python software/data_capture/serial_plotter.py --port COM3
```

## Painel Clínico Streamlit

O painel principal é o `software/dashboard/app.py`. Ele simula o acompanhamento de
sessões, guarda o histórico de cada paciente em um banco SQLite (`data/clinic.db`)
e exibe métricas de desempenho.

```bash
streamlit run software/dashboard/app.py
```

Ao abrir o painel, cadastre novos pacientes pelo formulário lateral. As sessões
simuladas coletadas são associadas ao paciente selecionado e salvas
automaticamente no banco de dados via `database.py`.

## Estrutura do Banco de Dados

O arquivo `data/clinic.db` contém duas tabelas:

- `patients(id, name)` – Lista dos pacientes cadastrados.
- `sessions(id, patient_id, collected_at, payload_json)` – Histórico das sessões,
  com os dados da sessão (time, le_quad, etc.) armazenados em JSON.

Para inspecionar o banco fora do Streamlit, utilize qualquer ferramenta SQLite.

## Próximos Passos

- [x] Garantir que o `app.py` salve e carregue sessões corretamente via `database.py`.
- [ ] Integrar os sinais reais (leitura da serial e filtros) diretamente no `app.py`.
- [ ] Adicionar sensores de IMU ao firmware e ao painel.
- [ ] Documentar protocolos de avaliação clínica e métricas utilizadas.
