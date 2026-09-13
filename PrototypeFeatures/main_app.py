import streamlit as st
import os
import base64

import game_registration_login
import main_menu
import start_game
import save_files


# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="OverIndulgent",
    page_icon="☠️",
    layout="centered"
)


# -----------------------------
# BACKGROUND IMAGE
# -----------------------------

image_path = os.path.join(
    os.path.dirname(__file__),
    "title_screen.jpg"
)

with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(
        image_file.read()
    ).decode()


# -----------------------------
# FONT AND BACKGROUND STYLE
# -----------------------------

st.markdown(
    f"""
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&display=swap'
    );


    /* BACKGROUND */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.50),
                rgba(0, 0, 0, 0.50)
            ),
            url("data:image/jpeg;base64,{image_data}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        min-height: 100vh;
    }}


    /* FONT */

    html,
    body,
    [class*="css"] {{
        font-family: 'Cinzel', serif;
    }}


    /* TITLE */

    h1 {{
        font-family: 'Cinzel', serif;
        font-size: 45px !important;
        font-weight: 700;
        text-align: center;
        letter-spacing: 4px;
    }}


    h2,
    h3 {{
        font-family: 'Cinzel', serif;
        font-weight: 600;
        letter-spacing: 2px;
    }}


    p {{
        font-family: 'Cinzel', serif;
        font-size: 16px;
    }}


    /* CENTER LOGIN CONTENT */

    .block-container {{
        padding-top: 5rem;
        padding-bottom: 5rem;
    }}


    /* LOGIN BOX */

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(0, 0, 0, 0.60);
        border-radius: 12px;
        padding: 20px;
    }}


    /* BUTTONS */

    .stButton > button {{
        font-family: 'Cinzel', serif;
        font-weight: 600;
        letter-spacing: 1px;
    }}


    /* TABS */

    button[data-baseweb="tab"] {{
        font-family: 'Cinzel', serif;
        font-weight: 600;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


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


# =====================================================
# LOGIN / REGISTER SCREEN
# =====================================================

if not st.session_state.logged_in:

    st.title("☠️ OVERINDULGENT")

    st.caption("SURVIVAL HORROR PROTOTYPE")

    st.divider()


    # -----------------------------
    # LOGIN / REGISTER TABS
    # -----------------------------

    login_tab, register_tab = st.tabs(
        [
            "LOGIN",
            "REGISTER"
        ]
    )


    # =================================================
    # LOGIN
    # =================================================

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


    # =================================================
    # REGISTER
    # =================================================

    with register_tab:

        st.subheader("CREATE AN ACCOUNT")

        username = st.text_input(
            "New Username",
            key="register_username"
        )

        password = st.text_input(
            "Password",
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


# =====================================================
# AFTER LOGIN
# =====================================================

else:

    username = st.session_state.username


    # -----------------------------
    # SIDEBAR
    # -----------------------------

    st.sidebar.title("☠️ OVERINDULGENT")

    st.sidebar.write(
        "Logged in as:"
    )

    st.sidebar.write(
        f"**{username}**"
    )

    st.sidebar.divider()


    # -----------------------------
    # LOGOUT
    # -----------------------------

    if st.sidebar.button(
        "LOGOUT",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.username = ""

        st.session_state.page = "login"

        st.rerun()


    # =================================================
    # MAIN MENU
    # =================================================

    if st.session_state.page == "menu":

        main_menu.show_menu()


    # =================================================
    # START GAME
    # =================================================

    elif st.session_state.page == "start":

        start_game.show_game(username)


    # =================================================
    # CONTINUE
    # =================================================

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


    # =================================================
    # ABOUT GAME
    # =================================================

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


        # -----------------------------
        # USER JOURNEY
        # -----------------------------

        st.subheader("USER JOURNEY")

        st.write("1. Register or log in.")

        st.write("2. Start the game.")

        st.write("3. Take or reject the beauty pill.")

        st.write("4. Escape the factory and monsters.")

        st.write("5. Discover the truth about the pills.")

        st.write("6. Make choices that affect the ending.")

        st.write("7. Finish the game or return to the menu.")


        st.divider()


        if st.button(
            "← BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()


    # =================================================
    # EXIT
    # =================================================

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