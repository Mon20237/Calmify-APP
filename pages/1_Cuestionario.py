import streamlit as st

st.title("🧠 Cuestionario Diario")

st.write("¿Cómo te sientes hoy?")
estado = st.radio("Selecciona una opción:", [
    "😊 Me siento bien",
    "😐 Me siento neutro",
    "😟 Me siento estresado/a",
    "😢 Me siento ansioso/a sin razón aparente",
    "😴 Me cuesta dormir",
    "🤯 Tengo dificultad para concentrarme"
])

if st.button("Ver resultados"):
    st.success("Gracias por compartir cómo te sientes 💜")
