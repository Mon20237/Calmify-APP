import streamlit as st

st.title("🧘‍♀️ Tu Caja de Calma")

st.subheader("Estado actual: Moderado")

col1, col2 = st.columns(2)

with col1:
    st.button("🌬️ Respiración Guiada")
    st.button("🧘 Meditación Fópida")

with col2:
    st.button("📓 Diario Emocional")
    st.button("💡 Ver más recomendaciones")
