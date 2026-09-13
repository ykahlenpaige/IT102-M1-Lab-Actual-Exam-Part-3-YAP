import streamlit as st


def show_menu():

    # -----------------------------
    # CUSTOM FONT
    # -----------------------------

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cinzel', serif;
    }

    h1 {
        font-family: 'Cinzel', serif;
        font-size: 50px !important;
        font-weight: 700;
        text-align: center;
        letter-spacing: 4px;
    }

    h2, h3 {
        font-family: 'Cinzel', serif;
        text-align: center;
        letter-spacing: 2px;
    }

    p {
        font-family: 'Cinzel', serif;
        font-size: 16px;
    }

    </style>
    """, unsafe_allow_html=True)


    # -----------------------------
    # TITLE
    # -----------------------------

    st.title("—=𝖮𝖵𝖤𝖱𝖨𝖭𝖣𝖴𝖫𝖤𝖦𝖤𝖭𝖳=—")

    st.subheader("MAIN MENU")

    st.write(
        "Welcome to the factory."
    )

    st.write(
        "Living is a privilege. "
        "Just how much are you willing to pay?"
    )

    st.divider()


    # -----------------------------
    # MENU BUTTONS
    # -----------------------------

    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "▶ START GAME",
            use_container_width=True
        ):

            st.session_state.page = "start"

            st.rerun()


        if st.button(
            "CONTINUE",
            use_container_width=True
        ):

            st.session_state.page = "continue"

            st.rerun()


    with col2:

        if st.button(
            "ABOUT GAME",
            use_container_width=True
        ):

            st.session_state.page = "about"

            st.rerun()


        if st.button(
            "EXIT",
            use_container_width=True
        ):

            st.session_state.page = "exit"

            st.rerun()