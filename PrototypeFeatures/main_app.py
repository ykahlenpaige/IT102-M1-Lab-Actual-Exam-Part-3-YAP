import streamlit as st
import os
import base64

import game_registration_login
import main_menu
import start_game
import save_files
import scene_2
import scene_3
import scene_4


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="OverIndulgent",
    page_icon="☠️",
    layout="centered"
)


# --------------------------------------------------
# LOAD BACKGROUND IMAGE
# --------------------------------------------------

image_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "title_screen.jpg"
)

if os.path.exists(image_path):

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>

        /* ============================= */
        /* FULL BACKGROUND IMAGE          */
        /* ============================= */

        .stApp {{
            background: transparent !important;
        }}

        [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.35),
                    rgba(0, 0, 0, 0.35)
                ),
                url("data:image/jpeg;base64,{image_data}");

            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;

            min-height: 100vh;
        }}

        [data-testid="stAppViewContainer"] > .main {{
            background: transparent !important;
        }}

        [data-testid="stMain"] {{
            background: transparent !important;
        }}

        [data-testid="stHeader"] {{
            background: transparent !important;
        }}


        /* ============================= */
        /* FONT                           */
        /* ============================= */

        @import url(
            'https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&display=swap'
        );

        html,
        body,
        [class*="css"] {{
            font-family: 'Cinzel', serif;
        }}

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


        /* ============================= */
        /* CONTENT SPACING                */
        /* ============================= */

        .block-container {{
            padding-top: 4rem;
            padding-bottom: 4rem;
        }}


        /* ============================= */
        /* INPUT BOXES                    */
        /* ============================= */

        input {{
            font-family: 'Cinzel', serif !important;
        }}


        /* ============================= */
        /* BUTTONS                        */
        /* ============================= */

        .stButton > button {{
            font-family: 'Cinzel', serif !important;
            font-weight: 600 !important;
            letter-spacing: 1px;
        }}


        /* ============================= */
        /* TABS                           */
        /* ============================= */

        button[data-baseweb="tab"] {{
            font-family: 'Cinzel', serif !important;
            font-weight: 600 !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.warning(
        "title_screen.jpg was not found. "
        "Please place it in the same folder as main_app.py."
    )


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "page" not in st.session_state:
    st.session_state.page = "login"

if "progress" not in st.session_state:
    st.session_state.progress = 1

if "scene_choice" not in st.session_state:
    st.session_state.scene_choice = ""


# --------------------------------------------------
# LOGIN / REGISTER SCREEN
# --------------------------------------------------

if not st.session_state.logged_in:

    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">

        <h1>
        —=OVERINDULGENT=—
        </h1>

        <p style="
            color: #aaaaaa;
            font-size: 15px;
            letter-spacing: 1px;
        ">
        SURVIVAL HORROR PROTOTYPE
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    login_tab, register_tab = st.tabs(
        ["LOGIN", "REGISTER"]
    )


    # --------------------------------------------------
    # LOGIN
    # --------------------------------------------------

    with login_tab:

        st.subheader("WELCOME BACK")

        username = st.text_input(
            "USERNAME",
            key="login_username"
        )

        password = st.text_input(
            "PASSWORD",
            type="password",
            key="login_password"
        )

        if st.button(
            "LOGIN",
            use_container_width=True
        ):

            success, message = (
                game_registration_login.login(
                    username,
                    password
                )
            )

            if success:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.page = "menu"

                saved_game = save_files.get_save(username)

                if saved_game:
                    st.session_state.progress = saved_game.get(
                        "progress",
                        1
                    )
                else:
                    st.session_state.progress = 1

                st.rerun()

            else:
                st.error(message)


    # --------------------------------------------------
    # REGISTER
    # --------------------------------------------------

    with register_tab:

        st.subheader("CREATE ACCOUNT")

        new_username = st.text_input(
            "USERNAME",
            key="register_username"
        )

        new_password = st.text_input(
            "PASSWORD",
            type="password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "CONFIRM PASSWORD",
            type="password",
            key="confirm_password"
        )

        if st.button(
            "REGISTER",
            use_container_width=True
        ):

            if new_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                success, message = (
                    game_registration_login.register(
                        new_username,
                        new_password
                    )
                )

                if success:

                    st.success(message)

                    st.info(
                        "You can now log in using your account."
                    )

                else:

                    st.error(message)


# --------------------------------------------------
# LOGGED-IN GAME
# --------------------------------------------------

else:

    # ----------------------------------------------
    # SIDEBAR
    # ----------------------------------------------

    with st.sidebar:

        st.title("☠️ OVERINDULGENT")

        st.write(
            "Logged in as:",
            st.session_state.username
        )

        st.divider()

        if st.button(
            "MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"
            st.rerun()

        if st.button(
            "START GAME",
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

        st.divider()

        if st.button(
            "LOG OUT",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.page = "login"

            st.rerun()


    # ----------------------------------------------
    # MAIN MENU
    # ----------------------------------------------

    if st.session_state.page == "menu":

        main_menu.show_menu()


    # ----------------------------------------------
    # START GAME
    # ----------------------------------------------

    elif st.session_state.page == "start":

        start_game.show_game(
            st.session_state.username
        )


    # ----------------------------------------------
    # SCENE 2
    # ----------------------------------------------

    elif st.session_state.page == "scene2":

        scene_2.show_scene(
            st.session_state.username
        )


    # ----------------------------------------------
    # SCENE 3
    # ----------------------------------------------

    elif st.session_state.page == "scene3":

        scene_3.show_scene(
            st.session_state.username
        )


    # ----------------------------------------------
    # SCENE 4
    # ----------------------------------------------

    elif st.session_state.page == "scene4":

        scene_4.show_scene(
            st.session_state.username
        )


    # ----------------------------------------------
    # TO BE CONTINUED
    # ----------------------------------------------

    elif st.session_state.page == "ending":

        st.markdown(
            """
            <div style="
                text-align: center;
                margin-top: 150px;
            ">

            <h1 style="
                font-size: 55px !important;
                letter-spacing: 6px;
            ">
            TO BE CONTINUED...
            </h1>

            <p style="
                color: #aaaaaa;
                font-size: 18px;
                letter-spacing: 2px;
            ">
            THE TRUTH HAS ONLY JUST BEGUN.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.write(
            "You uncovered something the factory never wanted "
            "anyone to see."
        )

        st.write(
            "But the deeper truth is still waiting..."
        )

        st.write(
            "Will you survive long enough to expose it?"
        )

        st.divider()

        if st.button(
            "BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"
            st.rerun()

        if st.button(
            "EXIT",
            use_container_width=True
        ):

            st.session_state.page = "exit"
            st.rerun()
            
    # ----------------------------------------------
    # CONTINUE GAME
    # ----------------------------------------------

    elif st.session_state.page == "continue":

        st.title("CONTINUE")

        saved_game = save_files.get_save(
            st.session_state.username
        )

        if saved_game:

            st.write(
                "Saved progress found."
            )

            st.write(
                "Progress:",
                saved_game.get("progress", 1)
            )

            st.write(
                "Last choice:",
                saved_game.get("choice", "None")
            )

            if st.button(
                "CONTINUE GAME",
                use_container_width=True
            ):

                progress = saved_game.get(
                    "progress",
                    1
                )

                if progress == 2:
                    st.session_state.page = "scene2"

                elif progress == 3:
                    st.session_state.page = "scene3"

                elif progress == 4:
                    st.session_state.page = "scene4"

                else:
                    st.session_state.page = "start"

                st.rerun()

        else:

            st.info(
                "No saved game found."
            )

            if st.button(
                "START NEW GAME",
                use_container_width=True
            ):

                st.session_state.page = "start"
                st.rerun()

        st.divider()

        if st.button(
            "← BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"
            st.rerun()


    # ----------------------------------------------
    # ABOUT GAME
    # ----------------------------------------------

    elif st.session_state.page == "about":

        st.title("ABOUT OVERINDULGENT")

        st.write(
            """
            OverIndulgent is a narrative-driven survival
            horror game about overconsumption, greed,
            beauty, and social inequality.
            """
        )

        st.write(
            """
            You play as a factory worker who secretly
            consumes a reality altering pill that is meant only
            for the wealthy to escape the harsh truth and expectations of society.
            """
        )

        st.write(
            """
            After being discovered, you must escape the
            factory, uncover the truth behind the pills,
            and survive what waits inside.
            """
        )

        st.divider()

        st.write(
            """
            THIS IS ONLY A PROTOTYPE HUHU :'> made by Kahlen Yap for OOP m1 Exam
            I lowk put a solid amount of love into this and drew all the scenes using IbisPaintX 
            but the title screen. All scenes for the prototype and choices are by moi! :3
            """
        )

        st.divider()

        if st.button(
            "← BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"
            st.rerun()


    # ----------------------------------------------
    # EXIT
    # ----------------------------------------------

    elif st.session_state.page == "exit":

        st.title("THANK YOU FOR PLAYING")

        st.write(
            "You have exited OverIndulgent."
        )

        if st.button(
            "BACK TO MAIN MENU",
            use_container_width=True
        ):

            st.session_state.page = "menu"
            st.rerun()