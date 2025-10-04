import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wallet - GreenCharge", layout="wide")

# -------------------------
# Header com logo e botão de usuário
# -------------------------
col1, col2 = st.columns([9, 1])

with col1:
    st.image("images/logo.png", width=220)

with col2:
    if "username" in st.session_state and st.session_state.username:
        st.markdown(
            f"""
            <style>
            .user-dropdown {{
                position: relative;
                display: inline-block;
                width: 100%;
            }}
            .user-btn {{
                background-color: #2ECC71;
                color: white;
                padding: 10px 15px;
                width: 100%;
                border: none;
                border-radius: 8px;
                font-weight: 600;
                cursor: pointer;
                text-align: center;
            }}
            .user-content {{
                display: none;
                position: absolute;
                right: 0;
                background-color: #f9f9f9;
                min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                border-radius: 8px;
                overflow: hidden;
            }}
            .user-content button {{
                width: 100%;
                padding: 12px;
                border: none;
                background: white;
                cursor: pointer;
                text-align: left;
            }}
            .user-content button:hover {{
                background-color: #f0f0f0;
            }}
            </style>

            <div class="user-dropdown">
                <button class="user-btn" onclick="document.getElementById('dropdown-menu').style.display = (document.getElementById('dropdown-menu').style.display == 'block' ? 'none' : 'block')">
                    {st.session_state.username} ▼
                </button>
                <div class="user-content" id="dropdown-menu">
                    <button onclick="window.location.href='/'">Deslogar</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------
# Conteúdo da carteira
# -------------------------
st.title("Sua Carteira de Créditos de Carbono")

# Saldo e métricas principais
st.markdown("### Resumo da Carteira")
saldo_total = 1250.00
creditos = 250
meta = 500
progresso = (creditos / meta) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Saldo total", f"R$ {saldo_total:,.2f}")
col2.metric("Créditos de carbono", f"{creditos}")
col3.metric("CO₂ evitado", "1,2 ton")

st.markdown("---")

# Gráfico de evolução
st.markdown("### Evolução dos créditos")
df = pd.DataFrame({
    "Mes": ["Ago", "Set", "Out", "Nov", "Dez"],
    "Créditos acumulados": [120, 180, 250, 300, 400]
})

fig, ax = plt.subplots(figsize=(3.5, 2.0))
ax.plot(df["Mes"], df["Créditos acumulados"], marker="o", color="#2E86C1")
ax.set_xlabel("Mês", fontsize=8)
ax.set_ylabel("Créditos", fontsize=8)
ax.tick_params(axis="both", labelsize=8)
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# Progresso da meta mensal
st.markdown("### Progresso da meta mensal")
st.write(f"Você já conquistou **{creditos}** de **{meta}** créditos")
st.progress(progresso / 100)

st.markdown("---")

# Histórico de transações
st.markdown("### Histórico de transações")
historico = pd.DataFrame({
    "Data": ["15/09/25", "10/09/25"],
    "Tipo": ["Geração", "Venda"],
    "Quantidade": ["50 créditos", "30 créditos"],
    "Valor": ["R$ 25,00", "R$ 15,00"]
})
st.table(historico)

st.markdown("---")

# -------------------------
# Ações rápidas
# -------------------------
st.markdown("### Ações rápidas")
st.markdown(
    """
    <style>
    .action-btn {
        display: inline-block;
        width: 100%;
        padding: 12px;
        border-radius: 8px;
        font-weight: 600;
        text-align: center;
        border: none;
        cursor: pointer;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .green { background-color: #2ECC71; color: white; }
    .orange { background-color: #E67E22; color: white; }
    .blue { background-color: #3498DB; color: white; }
    .purple { background-color: #8E44AD; color: white; }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Botão Encerrar Sessão (redireciona para login/home)
    st.markdown(
        '<a href="/" target="_self">'
        '<button class="action-btn green">Encerrar Sessão</button>'
        '</a>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown('<button class="action-btn orange">Vender créditos</button>', unsafe_allow_html=True)
with col3:
    st.markdown('<button class="action-btn blue">Ver NFT</button>', unsafe_allow_html=True)
with col4:
    # Botão Simulador (redireciona para página de simulador)
    st.markdown(
        '<a href="/simulador" target="_self">'
        '<button class="action-btn purple">Simulador</button>'
        '</a>',
        unsafe_allow_html=True
    )