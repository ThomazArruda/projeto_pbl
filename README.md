# NeuroPasso 🧠🦵

**NeuroPasso** é uma aplicação web completa para monitoramento e reabilitação de pacientes com deficiências motoras. O sistema visualiza dados em tempo real de sensores (Ângulo, EMG, ECG) conectados a microcontroladores ESP32, permitindo que fisioterapeutas acompanhem a evolução do tratamento e utilizem biofeedback visual.

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

## 📖 Como Usar o NeuroPasso

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

## 📂 Estrutura do Projeto

*   `backend/`: Código do servidor (Python/FastAPI) e Banco de Dados (`clinic.db`).
*   `frontend/`: Código da interface visual (React/Vite).
*   `hardware/`: Códigos para os microcontroladores ESP32.

---

**Desenvolvido para o Projeto PBL - Engenharia Biomédica**
