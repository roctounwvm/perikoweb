import streamlit as st

espacio=st.empty()

contraseña="pablocolorcarton"

respuesta=espacio.text_input("contraseña", type="password")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

.arcade-text {
    font-family: 'Press Start 2P', monospace;
    font-size: 24px;
    color: #00ffff;
    text-align: center;
    text-shadow: 4px 4px #ff00ff;
    margin: 30px 0;
}
</style>

<div class="arcade-text">
    PRUEBA EL NUEVO PERIKOS BET ARCADE
</div>
""", unsafe_allow_html=True)

st.link_button(
    "🎮 ENTRAR AL ARCADE 🎮",
    "https://perikos-arcade.onrender.com/"
)

if respuesta == contraseña:
    espacio.empty()
    st.title ("bienvenido a la perikoweb")
    st.text("en esta web encontraras cosas ramdom que encontre en mi galeria")

    if st.button("perro perroso"):
        st.image("perrofino.jpg") #cambiar despues

    if st.button("oso ososo"):
        st.image("5fdfa37ae6bd8.jpeg")

    if st.button("gato abogadoso"):
        st.image("gato.jfif")
    
    if st.button("gato huevoso"):
        st.image("gato huevoso.jpeg")

    if st.button("hmmm jejejhhh auuhhhhhhhh"):
            st.image("hmmm.jpeg")

    if st.button("peraperosa"):
         st.image("peraperosa.jfif")

    respuesta2=st.text_input("escribe algo")

    if respuesta2=="bimbo":
         st.image("bimbo.jfif")

    if respuesta2=="ivan":         
        st.image("ivan.jfif")

    if respuesta2=="perikoclasico":
         st.image("perikoclasico.jfif")

    if respuesta2=="recinosavion":
         st.image("recinosavion.jfif")

    if respuesta2=="yupi":
         st.image("yupi.jfif")

    
