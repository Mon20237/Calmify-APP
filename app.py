import streamlit as st

st.set_page_config(page_title="Calmify+", layout="wide")

st.markdown("""
    <style>
    .title { font-size: 36px; font-weight: bold; text-align: center; }
    .subtitle { font-size: 20px; text-align: center; margin-bottom: 20px; }
    .card {
        background-color: #eef1ff;
        padding: 20px;
        border-radius: 20px;
        margin: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌿 Calmify+</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Encuentra tu calma en un solo clic</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧠 Cuestionario Diario")
    st.write("¿Cómo te sientes hoy?")
    st.radio("Estado emocional:", ["😊 Bien", "😐 Neutro", "😟 Estresado/a", "😢 Ansioso/a"])
    st.button("Ver resultados")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧘 Caja de Calma")
    st.button("Respiración guiada")
    st.button("Meditación rápida")
    st.button("Diario emocional")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📆 Mapa Emocional")
    st.write("Seguimiento de tu estado emocional cada semana.")
    st.image("https://i.imgur.com/Z6y8Vqn.png", caption="Tu evolución", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
