# app.py
import streamlit as st
import streamlit_authenticator as stauth

# --- CREAR HASH DE CONTRASEÑA (una sola vez) ---
# Puedes usar esto para generar contraseñas hasheadas
# Pero en este caso, lo hacemos directamente en credentials

credentials = {
    "usernames": {
        "admin": {
            "name": "Usuario Admin",
            "password": stauth.Hasher(["password11"]).generate()[0]
        }
    }
}

# --- CONFIGURACIÓN DEL AUTENTICADOR ---
#authenticator = stauth.Authenticate(
#    credentials=credentials,
#    cookie_name="mi_app_cookie",           # Nombre de la cookie de sesión
#    cookie_key="llave_aleatoria_unica_123", # ¡Cámbialo por algo secreto!#    cookie_expiry_days=1
#)

authenticator = stauth.Authenticate(
    credentials,
    "my_cookie_name",
    "my_signature_key",
    cookie_expiry_days=30
)


# --- PANTALLA DE LOGIN ---
st.title("🔐 Inicio de Sesión")

# Mostrar formulario de login
name, authentication_status, username = authenticator.login("Iniciar sesión", "main")

if authentication_status:
    # ✅ Autenticado
    st.success(f"¡Bienvenido, {name}!")
    st.write("Línea 1: ¡Hola desde la VPS!")
    st.write("Línea 2: Esta app tiene login seguro.")
    st.write("Línea 3: 🚀 Todo funcionando perfecto.")

elif authentication_status is False:
    # ❌ Credenciales incorrectas
    st.error("Usuario o contraseña incorrectos")

elif authentication_status is None:
    # ⚠️ Aún no se ha iniciado sesión
    st.info("Por favor, ingresa tus credenciales para acceder.")