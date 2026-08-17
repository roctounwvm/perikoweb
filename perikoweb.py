    if respuesta2 == "yupi":
        st.image("yupi.jfif")

    # ANUNCIO AL FINAL DE LA PÁGINA
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    .arcade-text {
        font-family: 'Press Start 2P', monospace;
        font-size: 24px;
        color: #00ffff;
        text-align: center;
        text-shadow: 4px 4px #ff00ff;
        margin: 50px 0 25px 0;
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
