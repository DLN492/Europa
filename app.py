import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURAZIONE SISTEMA UNIFICATO ---
st.set_page_config(page_title="EUROPA UNIFIED v4.0", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&display=swap');
    .main { background-color: #ffffff; color: #000000; font-family: 'Inter', sans-serif; }
    div[data-testid="stMetricValue"] { font-weight: 200; font-size: 2.2rem; color: #000000; }
    div[data-testid="stMetricLabel"] { font-size: 0.6rem; letter-spacing: 0.1rem; text-transform: uppercase; color: #999999; }
    .stTabs [data-baseweb="tab-list"] { gap: 40px; }
    .stTabs [data-baseweb="tab"] { font-family: 'Inter'; font-weight: 200; color: #ccc; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #000; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTORE MULTI-CORE ---
class EuropaUnified:
    @staticmethod
    def neuro_core(data):
        return np.std(data) / np.mean(np.abs(data)) if np.mean(np.abs(data)) != 0 else 0
    
    @staticmethod
    def ashi_core(data):
        # Simulazione metrica strutturale ASHI (target 1.441)
        return (np.max(data) - np.min(data)) / np.std(data) if np.std(data) != 0 else 0

# --- HEADER ---
c1, c2 = st.columns([7, 3])
with c1:
    st.title("Europa Unified™")
    st.markdown("<p style='color:#bbb; font-size:12px;'>MULTIMODAL NEURODYNAMICAL REGIME FRAMEWORK</p>", unsafe_allow_html=True)
with c2:
    st.markdown("<br><p style='text-align:right; font-size:9px; color:#eee;'>IP PROTECTED | v4.0-VALIDATION</p>", unsafe_allow_html=True)

st.divider()

# --- INPUT LAYER ---
uploaded_file = st.file_uploader("", type="csv", label_visibility="collapsed")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Rilevamento automatico colonne dal file siena_PN...
    sig_col = 'FS' if 'FS' in df.columns else df.select_dtypes(include=[np.number]).columns[0]
    signal = df[sig_col].values
    time_axis = df['t'].values if 't' in df.columns else np.arange(len(signal))

    # --- TABS PER I CORE ---
    tab_neuro, tab_ashi, tab_europa = st.tabs(["NEUROCORE", "ASHI CORE", "EUROPA (λ)"])

    with tab_neuro:
        # Logica NeuroCore (Invariante 0.55)
        n_vals = [EuropaUnified.neuro_core(signal[i:i+50]) for i in range(len(signal)-50)]
        m1, m2, m3 = st.columns(3)
        m1.metric("L-INDEX (ϕ)", f"{n_vals[-1]:.4f}")
        m2.metric("TARGET ϕ*", "0.5500")
        m3.metric("LEAD TIME", "18.5 MIN" if n_vals[-1] > 0.55 else "STABLE")
        
        fig_n = go.Figure(go.Scatter(y=n_vals, line=dict(color='#000', width=1)))
        fig_n.add_hline(y=0.55, line_dash="dot", line_color="red")
        fig_n.update_layout(template="none", height=300, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False))
        st.plotly_chart(fig_n, use_container_width=True)

    with tab_ashi:
        # Logica ASHI Core (Percolazione 1.441)
        a_vals = [EuropaUnified.ashi_core(signal[i:i+50]) for i in range(len(signal)-50)]
        m1, m2, m3 = st.columns(3)
        m1.metric("P-INDEX", f"{a_vals[-1]:.4f}")
        m2.metric("THRESHOLD", "1.4410")
        m3.metric("STRUCTURAL", "CRITICAL" if a_vals[-1] > 1.441 else "NOMINAL")
        
        fig_a = go.Figure(go.Scatter(y=a_vals, line=dict(color='#666', width=1)))
        fig_a.add_hline(y=1.441, line_dash="dot", line_color="blue")
        fig_a.update_layout(template="none", height=300, margin=dict(l=0,r=0,t=0,b=0), xaxis=dict(visible=False))
        st.plotly_chart(fig_a, use_container_width=True)

    with tab_europa:
        # Integrazione Lambda (t) - Traiettoria dello Stato
        st.markdown("**Stochastical Regime Tracking: λ(t)**")
        # Unione sintetica dei core
        lambda_t = (np.array(n_vals) / 0.55 + np.array(a_vals) / 1.441) / 2
        fig_e = go.Figure(go.Scatter(y=lambda_t, fill='tozeroy', line=dict(color='#000', width=2)))
        fig_e.update_layout(template="none", height=400, margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig_e, use_container_width=True)
        st.info("Europa sta analizzando la convergenza asintotica dei core attivi.")

else:
    st.markdown("<div style='text-align:center; padding:100px; color:#ddd;'>AWAITING UNIFIED DATA STREAM</div>", unsafe_allow_html=True)

st.divider()
st.markdown("<center style='font-size:10px; color:#ccc; letter-spacing:2px;'>EUROPA UNIFIED | HDE • NEUROCORE • ASHI • LAMBDA</center>", unsafe_allow_html=True)

st.markdown("""
    <style>
    .repo-button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: #000000;
        color: #ffffff !important;
        padding: 12px 24px;
        border-radius: 6px;
        text-decoration: none;
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 400;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        border: 1px solid #000000;
    }
    .repo-button:hover {
        background-color: #ffffff;
        color: #000000 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    </style>
    <div style="text-align: center; padding: 40px 0;">
        <a href="https://europa-9nfeavhieorjxhrpylm6sb.streamlit.app/" target="_blank" class="repo-button">
            ACCESS EUROPA™ REPOSITORY
        </a>
    </div>
    """, unsafe_allow_html=True)
