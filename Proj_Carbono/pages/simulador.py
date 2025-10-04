import streamlit as st

st.set_page_config(page_title="Simulador", layout="wide")

# ------------------------------
# Logo no topo
# ------------------------------
col1, col2 = st.columns([8, 2])

with col1:
    st.image("images/logo.png", width=220)

with col2:
    st.markdown(
        """
        <a href="/carteira" style="text-decoration:none;">
            <button style="
                background-color: #31572c;
                color: white;
                border: none;
                padding: 12px 0;          
                width: 160px;            
                border-radius: 6px;
                cursor: pointer;
                font-weight: 600;
                display: flex;
                align-items: center;      
                justify-content: center;  
                margin-top: 20px;        
            ">Minha Carteira</button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.title("Calcule sua pegada de carbono")

st.write("Preencha os dados abaixo para simular seu impacto ambiental:")

with st.form("simulador_form"):
    km = st.number_input("Quilômetros rodados por ano:", min_value=0.0, step=0.1, value=12000.0)
    kWh = st.number_input("kWh consumidos por ano:", min_value=0.0, step=0.1, value=3500.0)
    residuos = st.number_input("Kg de resíduos por ano:", min_value=0.0, step=0.1, value=150.0)
    submitted = st.form_submit_button("Calcular impacto")

if submitted:
    # Fórmulas simples de cálculo (ajuste os fatores conforme precisar)
    transporte = km * 0.0002   # cada km gera 0.0002 tCO₂e
    energia = kWh * 0.0005     # cada kWh gera 0.0005 tCO₂e
    res = residuos * 0.001     # cada kg de resíduo = 0.001 tCO₂e
    total = transporte + energia + res

    st.success("Cálculo realizado com sucesso!")
    st.metric("Transporte (tCO₂e)", f"{transporte:.2f}")
    st.metric("Energia (tCO₂e)", f"{energia:.2f}")
    st.metric("Resíduos (tCO₂e)", f"{res:.2f}")
    st.metric("Total anual (tCO₂e)", f"{total:.2f}")
