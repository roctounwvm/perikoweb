import streamlit as st

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

st.set_page_config(
    page_title="Perikoweb",
    page_icon="🐶",
    layout="centered"
)

# -----------------------------
# ESTILO
# -----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f7f7f7, #e9eef5);
    color: black;
}

/* Todo el texto negro */
h1, h2, h3, h4, h5, h6,
p, label, div, span {
    color: black;
}

/* Título */
.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    margin-bottom: 5px;
    color: black;
}

/* Subtítulo */
.subtitle {
    text-align: center;
    color: black;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Tarjetas */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin: 20px 0;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    color: black;
}

/* Títulos de sección */
.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 15px;
    color: black;
}

/* Botones */
button {
    color: black !important;
}

/* Pie de página */
.footer {
    text-align: center;
    color: black;
    margin-top: 50px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# ENCABEZADO
# -----------------------------

st.markdown(
    '<div class="main-title">🐶 Perikoweb 🐱</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Un lugar donde guardo cosas random que encuentro en mi galería.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# GALERÍA
# -----------------------------

st.markdown("""
<div class="card">
    <div class="section-title">📸 Galería random</div>
</div>
""", unsafe_allow_html=True)


if st.button("🐶 Perro perroso", use_container_width=True):
    st.image("perrofino.jpg")


if st.button("🐻 Oso ososo", use_container_width=True):
    st.image("5fdfa37ae6bd8.jpeg")


if st.button("🐱 Gato abogadoso", use_container_width=True):
    st.image("gato.jfif")


if st.button("🥚 Gato huevoso", use_container_width=True):
    st.image("gato huevoso.jpeg")


if st.button("🤨 Hmmm jejejhhh auuhhhhhhhh", use_container_width=True):
    st.image("hmmm.jpeg")


if st.button("🍐 Peraperosa", use_container_width=True):
    st.image("peraperosa.jfif")


# -----------------------------
# BUSCADOR
# -----------------------------

st.markdown("""
<div class="card">
    <div class="section-title">🔎 Busca algo</div>
</div>
""", unsafe_allow_html=True)

respuesta2 = st.text_input(
    "Escribe una palabra",
    placeholder="Prueba con alguna palabra..."
)


if respuesta2.lower() == "bimbo":
    st.image("bimbo.jfif")

elif respuesta2.lower() == "ivan":
    st.image("ivan.jfif")

elif respuesta2.lower() == "perikoclasico":
    st.image("perikoclasico.jfif")

elif respuesta2.lower() == "recinosavion":
    st.image("recinosavion.jfif")

elif respuesta2.lower() == "yupi":
    st.image("yupi.jfif")


# -----------------------------
# PERIKOS BET ARCADE
# -----------------------------

st.markdown("""
<div class="card" style="text-align:center;">

<h2>🎮 Perikos Bet Arcade</h2>

<p>
¿Te aburriste de la Perikoweb?
<br>
Prueba ahora el nuevo Perikos Bet Arcade.
</p>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "🎮 Entrar al Perikos Bet Arcade",
    "https://perikos-arcade.onrender.com/",
    use_container_width=True
)


# -----------------------------
# PIE DE PÁGINA
# -----------------------------

st.markdown("""
<div class="footer">
    🐾 Perikoweb 🐾
    <br><br>
    <small>Una web completamente innecesaria pero necesaria.</small>
</div>
""", unsafe_allow_html=True)
