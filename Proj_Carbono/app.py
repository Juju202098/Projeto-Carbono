import streamlit as st
import home
import login

# Inicializa o estado da página
if "page" not in st.session_state:
    st.session_state.page = "home"

# Renderiza conforme estado
if st.session_state.page == "home":
    home.show()
elif st.session_state.page == "login":
    login.show()