# HipTech 🧠🦵

**HipTech** é uma aplicação web completa para monitoramento e reabilitação de pacientes com deficiências motoras. O sistema visualiza dados em tempo real de sensores (Ângulo, EMG, ECG) conectados a microcontroladores ESP32, permitindo que fisioterapeutas acompanhem a evolução do tratamento e utilizem biofeedback visual.

---

## 📋 Pré-requisitos

Para rodar este projeto do zero, você precisará instalar os seguintes programas no seu computador:

1.  **Node.js** (Versão 18 ou superior): Necessário para o Frontend (React).
    *   [Baixar Node.js](https://nodejs.org/)
2.  **Python** (Versão 3.10 ou superior): Necessário para o Backend (FastAPI).
    *   [Baixar Python](https://www.python.org/downloads/)
    *   *Nota: Durante a instalação, marque a opção "Add Python to PATH".*
3.  **Arduino IDE**: Para carregar os códigos nos microcontroladores ESP32.
    *   [Baixar Arduino IDE](https://www.arduino.cc/en/software)
4.  **Git** (Opcional, mas recomendado): Para baixar este repositório.
    *   [Baixar Git](https://git-scm.com/)

---

## 🛠️ Configuração do Hardware (ESP32)

O sistema utiliza dois módulos ESP32, um para cada perna (Direita e Esquerda).

1.  **Abra o Arduino IDE**.
2.  Instale as bibliotecas necessárias (se houver) e o suporte à placa ESP32 no gerenciador de placas.
3.  **Configurar IP do Servidor:**
    *   Descubra o endereço IP do seu computador (no Windows, abra o terminal e digite `ipconfig`. Procure por "Endereço IPv4", ex: `192.168.1.15`).
    *   Abra os arquivos de firmware localizados na pasta `hardware/`:
        *   `hardware/esp32/firmware_direita/firmware_direita.ino`
        *   `hardware/esp32/firmware_esquerda/firmware_esquerda.ino`
    *   No código, procure pela linha que define o `host` ou `server IP` e altere para o IP do seu computador.
    *   Atualize também o `SSID` e `PASSWORD` com o nome e senha da sua rede Wi-Fi.
4.  **Carregar o Código:**
    *   Conecte o ESP32 da perna **Direita** via USB, selecione a porta correta no Arduino IDE e clique em "Carregar" (Seta para direita).
    *   Repita o processo para o ESP32 da perna **Esquerda** usando o arquivo correspondente.

---

## 🚀 Instalação e Execução do Software

Você precisará de dois terminais abertos: um para o Backend (Servidor) e outro para o Frontend (Site).

### Passo 1: Configurar o Backend (Servidor)

1.  Abra um terminal (PowerShell ou CMD).
2.  Navegue até a pasta `backend` do projeto:
    ```bash
    cd caminho/para/projeto_pbl/backend
    ```
3.  Crie um ambiente virtual (para isolar as bibliotecas):
    ```bash
    python -m venv venv
    ```
4.  Ative o ambiente virtual:
    *   **Windows:** `.\venv\Scripts\activate`
    *   **Mac/Linux:** `source venv/bin/activate`
5.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6.  Inicie o servidor:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    *   *Se aparecer uma mensagem de firewall, permita o acesso.*
    *   O servidor estará rodando e pronto para receber dados dos ESP32 via UDP e conexões do site.

### Passo 2: Configurar o Frontend (Site)

1.  Abra um **novo** terminal.
2.  Navegue até a pasta `frontend` do projeto:
    ```bash
    cd caminho/para/projeto_pbl/frontend
    ```
3.  Instale as dependências do projeto:
    ```bash
    npm install
    ```
4.  Inicie o site:
    ```bash
    npm run dev
    ```
5.  O terminal mostrará um link (geralmente `http://localhost:5173`). Segure `Ctrl` e clique no link para abrir no navegador.

---

## 📖 Como Usar o HipTech

1.  **Tela Inicial (Home):**
    *   Você verá a lista de pacientes cadastrados.
    *   Para adicionar um novo, digite o nome no campo "Nome do Paciente" e clique em **"Cadastrar Novo Paciente"**.
    *   Clique no cartão de um paciente para ver seus detalhes.

2.  **Detalhes do Paciente:**
    *   Aqui você vê o histórico de evolução do paciente.
    *   **Gráfico de Amplitude:** Mostra o ângulo máximo alcançado em cada sessão.
        *   🟢 Verde: Perna Controle (Direita).
        *   🔴 Vermelho (Tracejado): Perna em Tratamento (Esquerda).
    *   **Gráfico de Ativação:** Mostra a média de ativação muscular (EMG).
    *   Clique em **"Iniciar Nova Sessão"** para ir ao Dashboard em tempo real.

3.  **Dashboard (Sessão em Tempo Real):**
    *   Ligue os ESP32. Se configurados corretamente, os indicadores "Wifi" ficarão verdes e os gráficos começarão a se mover.
    *   Acompanhe os gráficos de Ângulo, EMG e ECG em tempo real.
    *   **Biofeedback:** Os números mudam de cor (Verde/Amarelo/Vermelho) dependendo da intensidade.
    *   Quando terminar o exercício, clique em **"Parar Sessão"**.
    *   Clique em **"Salvar"** para registrar os dados no histórico do paciente ou **"Reiniciar"** para descartar e começar de novo.

---

### Passo 3: Análise de Dados (Relatório Científico) 📊

Para gerar gráficos de alta resolução para relatórios, utilizamos um ambiente isolado com Jupyter Notebook e scripts Python.

1.  Abra um terminal e navegue até a pasta `analysis`:
    ```bash
    cd caminho/para/projeto_pbl/analysis
    ```
2.  Crie e ative um ambiente virtual específico para análise:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Instale as dependências de ciência de dados:
    ```bash
    pip install -r requirements.txt
    ```

**Scripts de Análise Estatística:**

Os seguintes scripts Python executam análises estatísticas completas e geram relatórios:

- **`statistical_analysis.py`** - Análise angular com Shapiro-Wilk
  ```bash
  python statistical_analysis.py
  ```
  Gera: `analise_angular_*.xlsx`, `analise_angular_*.csv`, `boxplot_deltas_angulares_*.png`

- **`emg_analysis.py`** - Análise de eletromiografia (EMG)
  ```bash
  python emg_analysis.py
  ```
  Gera: `analise_emg_*.xlsx`, `analise_emg_*.csv`, `boxplot_deltas_emg_*.png`

- **`ecg_analysis.py`** - Análise de eletrocardiografia (ECG)
  ```bash
  python ecg_analysis.py
  ```
  Gera: `analise_ecg_*.xlsx`, `analise_ecg_*.csv`, `boxplot_deltas_ecg_*.png`

- **`ttest_pareado.py`** - Teste T pareado bilateral
  ```bash
  python ttest_pareado.py
  ```
  Gera: `ttest_pareado_*.xlsx`, `ttest_pareado_*.csv`, `README_TEST_T.txt`

**Relatório Interativo - Jupyter Notebook:**

Para análise interativa com visualizações de alta resolução:

4.  Abra o VS Code nesta pasta ou inicie o Jupyter:
    *   Recomendado: Abra o arquivo `scientific_report.ipynb` no VS Code.
    *   Certifique-se de selecionar o Kernel `analysis/venv`.

**Funcionalidades do Notebook:**
*   **Alta Resolução:** Plota 100% dos pontos coletados (sem arredondamentos de tempo).
*   **Comparação Bilateral:** Suporta dados das duas pernas simultaneamente (Direita=Sólida, Esquerda=Tracejada).
*   **Dados Brutos:** Visualização de ângulo, EMG e ECG em tempo real.
*   **Filtro Butterworth:** Aplica filtros digitais para limpar o ruído do EMG e mostrar a envoltória de ativação muscular.
*   **Filtro de Kalman:** Suavização avançada de trajetória de ângulo para cinemática profissional.

**Documentação Científica:**

A pasta `analysis/` inclui READMEs abrangentes em português:

- **`README.txt`** - Metodologia Shapiro-Wilk com explicação didática
- **`README_EMG.txt`** - Análise completa de eletromiografia
- **`README_ECG.txt`** - Análise completa de sinais cardiovasculares
- **`README_TEST_T.txt`** - Metodologia de t-test pareado com resultados clínicos
- **`README_TEST_T_PT-BR.txt`** - Versão em português brasileiro
- **`README_FINAL.txt`** - Resumo executivo de todas as análises
- **`INDICE_ANALISES.txt`** - Índice navegável de todas as análises

**Análise Estatística Realizada:**

- ✓ Teste de Normalidade (Shapiro-Wilk): Valida se dados seguem distribuição normal
- ✓ T-Test Pareado: Compara medidas bilaterais (perna parética vs controle)
- ✓ Tamanho de Efeito (Cohen's d): Calcula magnitude prática da diferença
- ✓ Intervalo de Confiança 95%: Estimativa do intervalo de confiança
- ✓ Estatísticas Descritivas: Média, mediana, desvio padrão, quartis, CV

---

## 📚 Documentação Técnica

**Arquivo: `METODOLOGIA_SOFTWARE.txt`** - Guia completo de arquitetura, tecnologias e metodologia

Este arquivo, localizado na raiz do projeto, documenta:
- Visão geral da arquitetura completa
- Stack tecnológico detalhado (Backend FastAPI, Frontend React, Hardware ESP32)
- Fluxo de dados de ponta a ponta
- Metodologia estatística implementada (Shapiro-Wilk, t-test pareado, Cohen's d)
- Roteiro completo de execução com troubleshooting

---

## 📂 Estrutura do Projeto

*   `backend/`: Código do servidor (Python/FastAPI) e Banco de Dados (`clinic.db`).
*   `frontend/`: Código da interface visual (React/Vite).
*   `hardware/`: Códigos para os microcontroladores ESP32.
*   `analysis/`: Scripts e Notebooks para geração de gráficos científicos.

---

**Desenvolvido para o Projeto PBL - Engenharia Biomédica**
