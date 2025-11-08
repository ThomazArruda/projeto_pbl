import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time
import database  # Importa seu database.py
import datetime

# Inicializa o banco de dados local e garante pacientes de demonstração
database.init_db()
database.seed_patients(["Paciente_A", "Paciente_B", "Paciente_C"])

# --- Configuração da Página ---
st.set_page_config(
    page_title="Reabilitação Pós-AVC",
    page_icon="🦵",
    layout="wide"
)

# --- Constantes e CSS ---
MUSCLE_MAP = {
    "le_quad": "Quadríceps Esquerdo",
    "le_isq": "Isquiotibiais Esquerdo",
    "ri_quad": "Quadríceps Direito",
    "ri_isq": "Isquiotibiais Direito"
}
METRIC_CSS = """
<style>
.metric-box {
    border: 2px solid {border_color};
    background-color: {bg_color};
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    text-align: center;
    color: {text_color};
}
.metric-title {
    font-size: 1.1em;
    font-weight: bold;
}
.metric-value {
    font-size: 1.5em;
    font-weight: 600;
}
</style>
"""
st.markdown(METRIC_CSS, unsafe_allow_html=True)

# --- Funções Auxiliares ---

def get_metric_colors(value):
    if value > 0.7: return "#E6F7EB", "#28A745", "#222222"
    elif value > 0.4: return "#FFFBE6", "#FFC107", "#222222"
    else: return "#FFF0F1", "#DC3545", "#222222"

def render_metric_box(title, value):
    val_percent = f"{value*100:.1f}%"
    bg, border, text = get_metric_colors(value)
    html = f"""
    <div class="metric-box" style="background-color: {bg}; border-color: {border}; color: {text};">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{val_percent}</div>
    </div>
    """
    return html

def get_status_indicator(value):
    if value > 0.7: return "🟢"
    elif value > 0.4: return "🟡"
    else: return "🔴"

def ensure_patient_state():
    """Garante que um paciente válido esteja carregado no estado."""
    patients = database.list_patients()
    if not patients:
        return None, []
    
    if "current_patient_id" not in st.session_state:
        st.session_state.current_patient_id = patients[0]["id"]
        
    valid_ids = {p["id"] for p in patients}
    if st.session_state.current_patient_id not in valid_ids:
        st.session_state.current_patient_id = patients[0]["id"]
        
    return st.session_state.current_patient_id, patients

# --- Inicialização do Estado ---
if 'session_data' not in st.session_state:
    st.session_state.session_data = {
        "time": [], "le_quad": [], "le_isq": [],
        "ri_quad": [], "ri_isq": [], "hip_angle": []
    }
if 'is_running' not in st.session_state:
    st.session_state.is_running = False

current_patient_id, patients = ensure_patient_state()

if current_patient_id is None:
    st.error("Nenhum paciente cadastrado. Adicione um paciente para começar.")
    st.stop()

patient_lookup = {p["name"]: p["id"] for p in patients}
current_patient_name = next(
    (p["name"] for p in patients if p["id"] == current_patient_id),
    "Paciente"
)

# =============================================================================
# --- LÓGICA DE CALLBACKS (A CORREÇÃO DOS "TRANCOS E BARRANCOS") ---
# =============================================================================

def on_patient_select():
    """Chamado quando o seletor de paciente muda."""
    st.session_state.current_patient_id = patient_lookup[st.session_state.patient_selector]
    st.session_state.selected_session_label = "Sessão Atual (Ao Vivo)"
    st.session_state.is_running = False # Para a sessão se trocar de paciente

def on_patient_add():
    """Chamado ao adicionar um novo paciente."""
    new_name = st.session_state.new_patient_name
    if new_name:
        new_id = database.add_patient(new_name)
        if new_id:
            st.success(f"Paciente '{new_name}' cadastrado!")
            st.session_state.current_patient_id = new_id
            st.session_state.new_patient_name = "" # Limpa a caixa
        else:
            st.warning("Nome já existe ou é inválido.")
    else:
        st.warning("Informe um nome.")

def on_start_click():
    """Chamado ao clicar em 'Iniciar Sessão'."""
    st.session_state.is_running = True
    st.session_state.session_data = {
        "time": [], "le_quad": [], "le_isq": [],
        "ri_quad": [], "ri_isq": [], "hip_angle": []
    }
    st.session_state.selected_session_label = "Sessão Atual (Ao Vivo)"

def on_stop_click():
    """Chamado ao clicar em 'Parar e Salvar'."""
    st.session_state.is_running = False
    if st.session_state.session_data["time"]:
        database.add_session(current_patient_id, st.session_state.session_data)
        st.success("Sessão salva com sucesso!")
        
        # Atualiza a lista de sessões para que possamos selecioná-la
        sessions = database.get_sessions(current_patient_id)
        if sessions:
            # Define a sessão salva como a selecionada
            st.session_state.selected_session_label = sessions[0]["date"]
    else:
        st.warning("Nenhum dado coletado para salvar.")

# --- Barra Lateral (Sidebar) ---
with st.sidebar:
    st.title("Controle da Sessão")

    # --- SELETOR DE PACIENTE ---
    patient_names = list(patient_lookup.keys())
    current_index = patient_names.index(current_patient_name)
    
    st.selectbox(
        "Selecionar Paciente",
        patient_names,
        index=current_index,
        key="patient_selector", # A chave que o callback usa
        on_change=on_patient_select # <--- USA O CALLBACK
    )
    
    # --- CADASTRO DE PACIENTE ---
    st.subheader("Cadastrar novo paciente")
    st.text_input("Nome completo", key="new_patient_name")
    
    st.button(
        "Adicionar Paciente", 
        use_container_width=True, 
        key="add_patient_button",
        on_click=on_patient_add # <--- USA O CALLBACK
    )
    
    st.caption("Os dados ficam salvos em data/clinic.db")
    st.divider()

    # --- SELETOR DE SESSÃO ---
    sessions = database.get_sessions(current_patient_id)
    session_dates = ["Sessão Atual (Ao Vivo)"] + [s["date"] for s in sessions]

    if "selected_session_label" not in st.session_state or st.session_state.selected_session_label not in session_dates:
        st.session_state.selected_session_label = session_dates[0]

    selected_session = st.selectbox(
        "Selecionar Sessão",
        session_dates,
        key="selected_session_label",
    )
    st.divider()

    # --- BOTÕES DE CONTROLE ---
    col1, col2 = st.columns(2)
    
    col1.button(
        "▶️ Iniciar Nova Sessão", 
        use_container_width=True, 
        disabled=st.session_state.is_running, 
        key="start_session",
        on_click=on_start_click # <--- USA O CALLBACK
    )

    col2.button(
        "⏹️ Parar e Salvar", 
        use_container_width=True, 
        disabled=not st.session_state.is_running, 
        key="stop_session",
        on_click=on_stop_click # <--- USA O CALLBACK
    )

# --- Título Principal ---
st.title(f"Plataforma de Reabilitação - {current_patient_name}")
st.caption(f"Visualizando: {selected_session}")

# --- Lógica de Exibição ---

if selected_session == "Sessão Atual (Ao Vivo)":
    # MODO AO VIVO
    st.header("Monitoramento em Tempo Real")
    
    metrics_col_left, metrics_col_center, metrics_col_right, metrics_col_history = st.columns([1, 2, 1, 1])

    with metrics_col_left:
        st.subheader("Perna Esquerda (Parética)")
        metric_le_quad = st.empty()
        metric_le_isq = st.empty()

    with metrics_col_center:
        st.image("https://placehold.co/400x500/F0F0F0/333?text=Diagrama+Anat%C3%B4mico", use_column_width=True)

    with metrics_col_right:
        st.subheader("Perna Direita (Não Parética)")
        metric_ri_quad = st.empty()
        metric_ri_isq = st.empty()

    with metrics_col_history:
        st.subheader("Histórico Recente")
        history_lines = []
        for s in sessions[:5]: 
            try:
                avg_le_q = np.mean(s["data"]["le_quad"]) if s["data"].get("le_quad") else 0
                avg_ri_q = np.mean(s["data"]["ri_quad"]) if s["data"].get("ri_quad") else 0
            except (KeyError, TypeError):
                avg_le_q = 0; avg_ri_q = 0
            indicator_le = get_status_indicator(avg_le_q)
            indicator_ri = get_status_indicator(avg_ri_q)
            history_lines.append(f"`{s['date']}` {indicator_le} | {indicator_ri}")
        st.markdown("\n".join(history_lines) or "Nenhuma sessão anterior.")

    # --- LOOP DE SIMULAÇÃO ---
    if st.session_state.is_running:
        start_time = time.time()
        le_quad_quality = 0.1
        le_isq_quality = 0.2
        ri_quad_quality = 0.8
        ri_isq_quality = 0.7

        # =========================================================================
        # --- CORREÇÃO DO GRÁFICO (Sem pisca-pisca e sem DuplicateId) ---
        # =========================================================================
        
        # 1. Criar os gráficos vazios ANTES do loop
        st.subheader("Ângulo do Quadril (IMU) - Tempo Real")
        # Criar colunas 'time' e 'hip_angle' e definir 'time' como índice
        df_imu_placeholder = pd.DataFrame(columns=["time", "hip_angle"]).set_index("time")
        chart_imu = st.line_chart(df_imu_placeholder)

        st.subheader("Ativação Muscular (EMG) - Tempo Real")
        # Criar colunas 'time' e todas as colunas de músculo
        df_emg_placeholder = pd.DataFrame(columns=["time"] + list(MUSCLE_MAP.keys())).set_index("time")
        chart_emg = st.line_chart(df_emg_placeholder)

        while st.session_state.is_running:
            # 1. SIMULAR DADOS
            current_time = time.time() - start_time
            le_quad_quality = min(le_quad_quality + 0.001, 1.0)
            le_isq_quality = min(le_isq_quality + 0.002, 1.0)
            le_quad_val = np.clip(np.random.normal(le_quad_quality, 0.1), 0, 1)
            le_isq_val = np.clip(np.random.normal(le_isq_quality, 0.1), 0, 1)
            ri_quad_val = np.clip(np.random.normal(ri_quad_quality, 0.05), 0, 1)
            ri_isq_val = np.clip(np.random.normal(ri_isq_quality, 0.05), 0, 1)
            hip_angle_val = 20 * np.sin(current_time * 2) + 5 * np.random.rand()
            
            # 2. ADICIONAR DADOS NA SESSÃO
            data = st.session_state.session_data
            data["time"].append(current_time)
            data["le_quad"].append(le_quad_val)
            data["le_isq"].append(le_isq_val)
            data["ri_quad"].append(ri_quad_val)
            data["ri_isq"].append(ri_isq_val)
            data["hip_angle"].append(hip_angle_val)
            
            # 3. ATUALIZAR MÉTRICAS (Semáforos)
            metric_le_quad.markdown(render_metric_box(MUSCLE_MAP["le_quad"], le_quad_val), unsafe_allow_html=True)
            metric_le_isq.markdown(render_metric_box(MUSCLE_MAP["le_isq"], le_isq_val), unsafe_allow_html=True)
            metric_ri_quad.markdown(render_metric_box(MUSCLE_MAP["ri_quad"], ri_quad_val), unsafe_allow_html=True)
            metric_ri_isq.markdown(render_metric_box(MUSCLE_MAP["ri_isq"], ri_isq_val), unsafe_allow_html=True)

            # 4. PREPARAR NOVOS DADOS PARA OS GRÁFICOS
            # (Usamos o tempo como índice para o add_rows)
            current_pd_time = pd.to_datetime(current_time, unit='s')

            new_imu_data = pd.DataFrame(
                {"hip_angle": [hip_angle_val]},
                index=[current_pd_time]
            )
            
            new_emg_data = pd.DataFrame(
                {
                    "le_quad": [le_quad_val],
                    "le_isq": [le_isq_val],
                    "ri_quad": [ri_quad_val],
                    "ri_isq": [ri_isq_val]
                },
                index=[current_pd_time]
            )

            # 5. ATUALIZAR GRÁFICOS com .add_rows()
            chart_imu.add_rows(new_imu_data)
            chart_emg.add_rows(new_emg_data)

            # 6. PAUSA DA SIMULAÇÃO
            time.sleep(0.05) # 50ms (20 FPS)
    else:
        st.info("Pressione 'Iniciar Nova Sessão' para começar o monitoramento ao vivo.")

else:
    # --- MODO HISTÓRICO (Lendo 100% do database.py) ---
    st.header(f"Análise da Sessão: {selected_session}")
    session_to_display = next((s for s in sessions if s["date"] == selected_session), None)

    if session_to_display:
        data = session_to_display["data"]
        df_hist = pd.DataFrame(data)

        metrics_col_left, metrics_col_center, metrics_col_right, metrics_col_history = st.columns([1, 2, 1, 1])
        
        avg_le_q = np.mean(data["le_quad"]) if data.get("le_quad") else 0
        avg_le_i = np.mean(data["le_isq"]) if data.get("le_isq") else 0
        avg_ri_q = np.mean(data["ri_quad"]) if data.get("ri_quad") else 0
        avg_ri_i = np.mean(data["ri_isq"]) if data.get("ri_isq") else 0

        with metrics_col_left:
            st.subheader("Perna Esquerda (Parética)")
            st.markdown(render_metric_box(f"{MUSCLE_MAP['le_quad']} (Média)", avg_le_q), unsafe_allow_html=True)
            st.markdown(render_metric_box(f"{MUSCLE_MAP['le_isq']} (Média)", avg_le_i), unsafe_allow_html=True)
        with metrics_col_center:
            st.image("https://placehold.co/400x500/F0F0F0/333?text=Diagrama+Anat%C3%B4mico", use_column_width=True)
        with metrics_col_right:
            st.subheader("Perna Direita (Não Parética)")
            st.markdown(render_metric_box(f"{MUSCLE_MAP['ri_quad']} (Média)", avg_ri_q), unsafe_allow_html=True)
            st.markdown(render_metric_box(f"{MUSCLE_MAP['ri_isq']} (Média)", avg_ri_i), unsafe_allow_html=True)
        
        with metrics_col_history:
            st.subheader("Evolução (Todas Sessões)")
            evolution_data = []
            for s in reversed(sessions):
                avg_val = np.mean(s["data"]["le_quad"]) if s["data"].get("le_quad") else 0
                evolution_data.append({"date": s["date"], "progress": avg_val})
            if evolution_data:
                df_evo = pd.DataFrame(evolution_data)
                df_evo["date"] = pd.to_datetime(df_evo["date"])
                fig_evo = px.line(df_evo, x="date", y="progress",
                                  title="Progresso - Quadríceps Esquerdo (Média)", markers=True)
                fig_evo.update_layout(yaxis_title="Qualidade Média", yaxis_range=[0,1])
                st.plotly_chart(fig_evo, use_container_width=True)

        st.divider()
        st.subheader("Gráficos Completos da Sessão")
        
        if df_hist.empty or not data.get("time"):
            st.warning("Sessão não contém dados de séries temporais para exibir.")
        else:
            st.write("#### Ângulo do Quadril (IMU)")
            fig_imu_hist = px.line(df_hist, x="time", y="hip_angle", title="Ângulo do Quadril (°)")
            fig_imu_hist.update_layout(yaxis_title="Ângulo (°)")
            st.plotly_chart(fig_imu_hist, use_container_width=True)

            st.write("#### Ativação Muscular (EMG)")
            df_melted_hist = df_hist.melt(id_vars=["time"], value_vars=list(MUSCLE_MAP.keys()),
                                     var_name="Músculo", value_name="Ativação")
            df_melted_hist["Músculo"] = df_melted_hist["Músculo"].map(MUSCLE_MAP)
            fig_emg_hist = px.line(df_melted_hist, x="time", y="Ativação", color="Músculo",
                               title="Ativação Muscular (Qualitativo)")
            st.plotly_chart(fig_emg_hist, use_container_width=True)
    else:
        st.error("Não foi possível carregar os dados da sessão selecionada.")
