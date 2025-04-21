import streamlit as st
import calendar
from datetime import datetime

st.title("🗺️ Mapa Emocional")

st.write("Registra tu estado emocional día a día.")

days = ["L", "M", "M", "J", "V", "S", "D"]
colors = {
    "😊": "green",
    "😐": "gray",
    "😟": "orange",
    "😢": "red"
}

st.write("Abril")
cols = st.columns(7)

for i in range(7):
    with cols[i]:
        st.markdown(f"**{days[i]}**")
        st.button("😊", key=f"{i}")
        
st.success("¡Vamos bien esta semana!")
