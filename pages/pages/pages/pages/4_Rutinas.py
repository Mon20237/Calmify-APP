import streamlit as st

st.title("🕒 Rutinas Personalizadas")

st.write("Elige una rutina breve para tu día:")

tiempo = st.selectbox("Duración:", ["5 minutos", "10 minutos", "15 minutos"])

st.write("Sonidos disponibles:")
cols = st.columns(4)
with cols[0]: st.button("🌧️ Rain")
with cols[1]: st.button("💨 Wind")
with cols[2]: st.button("🌲 Forest")
with cols[3]: st.button("☕ Café")

if st.button("Iniciar Rutina"):
    st.success("Tu rutina ha comenzado, respira profundo 💜")
