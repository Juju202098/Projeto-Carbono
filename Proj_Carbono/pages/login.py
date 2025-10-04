import streamlit as st
import sqlite3
import hashlib

# -----------------------------
# Configuração da página
# -----------------------------
st.set_page_config(page_title="Login / Cadastro", layout="wide")

# -----------------------------
# Logo no topo
# -----------------------------
st.image("images/logo.png", width=220) 

# -----------------------------
# Banco de dados SQLite
# -----------------------------
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Criar tabela de usuários se não existir
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')
conn.commit()

# -----------------------------
# Funções auxiliares
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result and result[0] == hash_password(password):
        return True
    return False

def register_user(username, password):
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# -----------------------------
# Página principal
# -----------------------------
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# Para controlar navegação
if "page" not in st.session_state:
    st.session_state.page = "login"  # default

# Se o usuário está logado, vai direto para carteira
if st.session_state.get("logged_in"):
    st.experimental_rerun()  # força atualização e redirecionamento

# -----------------------------
# Login / Cadastro
# -----------------------------
if not st.session_state.show_signup:
    with st.form("login_form"):
        st.subheader("Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            if check_login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Usuário ou senha incorretos.")

    if st.button("Não possui cadastro? Clique aqui para se cadastrar"):
        st.session_state.show_signup = True

else:
    # cadastro (igual ao seu código)
    ...

# -----------------------------
# Redirecionamento para carteira
# -----------------------------
if st.session_state.get("logged_in"):
    # mostra página de carteira diretamente
    st.write(f"Bem-vindo à sua carteira, {st.session_state.username}!")
    # aqui você coloca o código da página de carteira