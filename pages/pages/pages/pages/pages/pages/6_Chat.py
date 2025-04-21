import streamlit as st

st.title("🤖 Chat con IA")

st.write("Habla con Calmify Bot, tu asistente emocional:")

user_input = st.text_input("Escribe algo...")

if user_input:
    st.markdown(f"**Tú:** {user_input}")
    st.markdown("**Calmify Bot:** Gracias por compartir. Estoy aquí para ti 💜")
