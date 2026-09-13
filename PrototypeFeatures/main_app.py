import streamlit as st

import game_registration_login
import main_menu
import start_game
import save_files


st.set_page_config(
    page_title="OverIndulgent",
    page_icon="☠️"
)


# SESSION VARIABLES

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "username" not in st.session_state:

    st.session_state.username = ""


if "page" not in st.session_state:

    st.session_state.page = "login"


if "progress" not in st.session_state:

    st.session_state.progress = 1


# LOGIN / REGISTER

if not st.session_state.logged_in:

    st.title("☠️ OVERINDULGENT")

    st.caption("Survival Horror Prototype")

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )


    # LOGIN

    with login_tab:

        st.subheader("Welcome Back")

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
            "Login",
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

                saved_game = save_files.get_save(
                    username
                )

                if saved_game:

                    st.session_state.progress = (
                        saved_game.get(
                            "progress",
                            1
                        )
                    )

                else:

                    st.session_state.progress = 1

                st.session_state.page = "menu"

                st.rerun()

            else:

                st.error(message)


    # REGISTER

    with register_tab:

        st.subheader("Create an Account")

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
            "Register",
            use_container_width=True
        ):

            success, message = (
                game_registration_login.register(
                    username,
                    password
                )
            )

            if success:

                st.success(message)

                st.info(
                    "You can now log in."
                )

            else:

                st.error(message)


# AFTER LOGIN

else:

    username = st.session_state.username


    # LOGOUT BUTTON

    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.username = ""

        st.session_state.page = "login"

        st.rerun()


    # MAIN MENU

    if st.session_state.page == "menu":

        main_menu.show_menu()


    # START GAME

    elif st.session_state.page == "start":

        start_game.show_game(username)


    # CONTINUE

    elif st.session_state.page == "continue":

        st.title("CONTINUE")

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
                "Current progress:",
                progress
            )

            st.write(
                "The continuation section will "
                "be added as the game is developed."
            )

        st.divider()

        if st.button(
            "← Back to Main Menu",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()


    # ABOUT

    elif st.session_state.page == "about":

        st.title("ABOUT OVERINDULGENT")

        st.subheader("Survival Horror")

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

        st.subheader("Game Goal")

        st.write(
            "The game encourages players to think about "
            "instant gratification, status, beauty, "
            "and the effects of overconsumption."
        )

        st.divider()

        st.subheader("User Journey")

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
            "← Back to Main Menu",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()


    # EXIT

    elif st.session_state.page == "exit":

        st.title("EXIT GAME")

        st.write(
            "Thank you for playing OverIndulgent."
        )

        st.write(
            "You may close the browser tab to exit."
        )

        st.divider()

        if st.button(
            "← Back to Main Menu",
            use_container_width=True
        ):

            st.session_state.page = "menu"

            st.rerun()