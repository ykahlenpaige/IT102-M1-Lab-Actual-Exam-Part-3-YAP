import streamlit as st

import game_registration_login
import main_menu
import start_game
import save_files


# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="—=𝖮𝖵𝖤𝖱𝖨𝖭𝖣𝖴𝖫𝖤𝖦𝖤𝖭𝖳=—",
    page_icon="💊",
    layout="centered"
)


# -----------------------------
# CUSTOM FONT AND TEXT STYLE
# -----------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cinzel', serif;
}

h1 {
    font-family: 'Cinzel', serif;
    font-size: 45px !important;
    font-weight: 700;
    text-align: center;
    letter-spacing: 3px;
}

h2 {
    font-family: 'Cinzel', serif;
    font-weight: 600;
    letter-spacing: 2px;
}

h3 {
    font-family: 'Cinzel', serif;
    font-weight: 600;
    letter-spacing: 1px;
}

p {
    font-family: 'Cinzel', serif;
    font-size: 16px;
}

.stCaption {
    text-align: center;
    font-family: 'Cinzel', serif;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "page" not in st.session_state:
    st.session_state.page = "login"

if "progress" not in st.session_state:
    st.session_state.progress = 1


# -----------------------------
# LOGIN / REGISTER
# -----------------------------

if not st.session_state.logged_in:

    st.title("—=𝖮𝖵𝖤𝖱𝖨𝖭𝖣𝖴𝖫𝖤𝖦𝖤𝖭𝖳=—")

    st.caption("SURVIVAL HORROR PROTOTYPE")

    st.divider()

    login_tab, register_tab = st.tabs(
        [
            "LOGIN",
            "REGISTER"
        ]
    )


    # -------------------------
    # LOGIN
    # -------------------------

    with login_tab:

        st.subheader("WELCOME BACK")

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )


        if st.button(
            "LOGIN",
            use_container_width=True
        ):

            success, message = game_registration_login.login(
                username,
                password
            )


            if success:

                st.session_state.logged_in = True

                st.session_state.username = username

                saved_game = save_files.get_save(username)


                if saved_game:

                    st.session_state.progress = saved_game.get(
                        "progress",
                        1
                    )

                else:

                    st.session_state.progress = 1


                st.session_state.page = "menu"

                st.rerun()


            else:

                st.error(message)


    # -------------------------
    # REGISTER
    # -------------------------

    with register_tab:

        st.subheader("CREATE AN ACCOUNT")

        username = st.text_input(
            "New Username",
            key="register_username"
        )

        password = st.text_input(
            "New Password",
            type="password",
            key="register_password"
        )


        if st.button(
            "REGISTER",
            use_container_width=True
        ):

            success, message = game_registration_login.register(
                username,
                password
            )


            if success:

                st.success(message)

                st.info(
                    "You can now log in."
                )

            else:

                st.error(message)


# -----------------------------
# AFTER LOGIN
# -----------------------------

else:

    username = st.session_state.username


    # -------------------------
    # SIDEBAR
    # -------------------------

    st.sidebar.title("—=𝖮𝖵𝖤𝖱𝖨𝖭𝖣𝖴𝖫𝖤𝖦𝖤𝖭𝖳=—")

    st.sidebar.write(
        "Logged in as:"
    )

    st.sidebar.write(
        f"**{username}**"
    )

    st.sidebar.divider()


    if st.sidebar.button(
        "LOGOUT",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.username = ""

        st.session_state.page = "login"

        st.rerun()


    # -----------------------------
    # MAIN MENU
    # -----------------------------

    if st.session_state.page == "menu":

        main_menu.show_menu()


    # -----------------------------
    # START GAME
    # -----------------------------

    elif st.session_state.page == "start":

        start_game.show_game(username)


    # -----------------------------
    # CONTINUE
    # -----------------------------

    elif st.session_state.page == "continue":

        st.title("CONTINUE")

        st.subheader("YOUR SAVED GAME")

        progress = st.session_state.progress


        if progress == 1:

            st.info(
                "You have not started the game yet."
            )

        else:

            st.success(
                "Your saved game was found!"
            )

            st.write(
                f"Current progress: Chapter {progress}"
            )

            st.write(
                "The continuation section will "
                "be added as the game is developed."
            )


        st.divider()


        if st.button(
            "← BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()


    # -----------------------------
    # ABOUT GAME
    # -----------------------------

    elif st.session_state.page == "about":

        st.title("ABOUT OVERINDULGENT")

        st.subheader("SURVIVAL HORROR")

        st.write(
            "OverIndulgent is a narrative-driven "
            "survival horror game about overconsumption, "
            "greed, beauty, and social inequality."
        )

        st.write(
            "The game follows a factory worker who "
            "secretly consumes a beauty pill and "
            "becomes the target of the factory."
        )


        st.subheader("GAME GOAL")

        st.write(
            "The game encourages players to think about "
            "instant gratification, status, beauty, "
            "and the effects of overconsumption."
        )


        st.divider()


        st.subheader("USER JOURNEY")

        st.write(
            "1. Register or log in."
        )

        st.write(
            "2. Start the game."
        )

        st.write(
            "3. Take or reject the beauty pill."
        )

        st.write(
            "4. Escape the factory and monsters."
        )

        st.write(
            "5. Discover the truth about the pills."
        )

        st.write(
            "6. Make choices that affect the ending."
        )

        st.write(
            "7. Finish the game or return to the menu."
        )


        st.divider()


        if st.button(
            "← BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()


    # -----------------------------
    # EXIT
    # -----------------------------

    elif st.session_state.page == "exit":

        st.title("EXIT GAME")

        st.subheader("THANK YOU FOR PLAYING")

        st.write(
            "You may close the browser tab to exit."
        )


        st.divider()


        if st.button(
            "← BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()