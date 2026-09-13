import streamlit as st

import game_registration_login
import main_menu
import save_files


st.set_page_config(
    page_title="OverIndulgent",
    page_icon="☠️"
)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "progress" not in st.session_state:
    st.session_state.progress = 1


st.title("☠️ OVERINDULGENT")
st.caption("Survival Horror Prototype")


# LOGIN AND REGISTER

if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )

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
                        saved_game.get("progress", 1)
                    )
                else:
                    st.session_state.progress = 1

                st.success(message)
                st.rerun()

            else:
                st.error(message)

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
                st.info("You can now log in.")
            else:
                st.error(message)


# MAIN GAME

else:

    menu = main_menu.show_menu()

    username = st.session_state.username
    progress = st.session_state.progress

    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


    # START GAME

    if menu == "Start Game":

        st.header("The Factory")

        st.write(
            "You are a factory worker in a society "
            "obsessed with beauty, status, and consumption."
        )

        st.write(
            "The beauty pills are only for the rich. "
            "Workers are forbidden from taking them."
        )

        st.warning(
            "You secretly take one of the pills."
        )

        choice = st.radio(
            "What do you do?",
            [
                "Take the pill",
                "Leave the pill"
            ]
        )

        if st.button(
            "Continue",
            use_container_width=True
        ):

            if choice == "Take the pill":

                st.session_state.progress = 2

                save_files.save_game(
                    username,
                    {
                        "progress": 2,
                        "choice": "Take the pill"
                    }
                )

                st.success(
                    "You take the pill. "
                    "Something feels wrong..."
                )

            else:

                st.session_state.progress = 2

                save_files.save_game(
                    username,
                    {
                        "progress": 2,
                        "choice": "Leave the pill"
                    }
                )

                st.info(
                    "You leave the pill behind, "
                    "but you hear something moving nearby."
                )


    # CONTINUE GAME

    elif menu == "Continue":

        st.header("Escape the Factory")

        if progress == 1:

            st.info(
                "You have not started the game yet. "
                "Go to Start Game."
            )

        else:

            st.write(
                "The factory alarm starts ringing."
            )

            st.error(
                "TERMINATION ORDER: WORKER DETECTED"
            )

            action = st.radio(
                "A monster is approaching. What do you do?",
                [
                    "Hide and wait",
                    "Run through the factory",
                    "Fight back"
                ]
            )

            if st.button(
                "Make Choice",
                use_container_width=True
            ):

                if action == "Hide and wait":

                    st.session_state.progress = 3

                    save_files.save_game(
                        username,
                        {
                            "progress": 3,
                            "action": action
                        }
                    )

                    st.success(
                        "You survive the encounter "
                        "and find a hidden laboratory."
                    )

                elif action == "Run through the factory":

                    st.session_state.progress = 3

                    save_files.save_game(
                        username,
                        {
                            "progress": 3,
                            "action": action
                        }
                    )

                    st.success(
                        "You escape the monster "
                        "and discover strange files."
                    )

                else:

                    st.session_state.progress = 3

                    save_files.save_game(
                        username,
                        {
                            "progress": 3,
                            "action": action
                        }
                    )

                    st.warning(
                        "You fight the monster and barely survive."
                    )


            if progress >= 3:

                st.divider()

                st.subheader("The Truth")

                st.write(
                    "The files reveal that the beauty pills "
                    "were never meant to improve people's lives."
                )

                st.write(
                    "Overconsumption has changed the rich "
                    "into monsters that see workers as food "
                    "or threats."
                )

                ending = st.radio(
                    "What will you choose?",
                    [
                        "Expose the truth",
                        "Keep the truth for yourself",
                        "Destroy the remaining pills"
                    ]
                )

                if st.button(
                    "Finish Game",
                    use_container_width=True
                ):

                    save_files.save_game(
                        username,
                        {
                            "progress": 4,
                            "ending": ending
                        }
                    )

                    st.session_state.progress = 4

                    st.success(
                        "Your choice: " + ending
                    )

                    st.balloons()


    # ABOUT

    elif menu == "About Game":

        st.header("About OverIndulgent")

        st.write(
            "OverIndulgent is a narrative-driven survival "
            "horror game about overconsumption, greed, "
            "beauty, and social inequality."
        )

        st.subheader("Goal")

        st.write(
            "The game encourages players to think about "
            "instant gratification, status, and the effects "
            "of wanting more."
        )

        st.subheader("User Journey")

        st.write("1. Register or log in.")
        st.write("2. Start the game.")
        st.write("3. Take or reject the beauty pill.")
        st.write("4. Escape the factory and monsters.")
        st.write("5. Discover the truth about the pills.")
        st.write("6. Make choices that affect the ending.")
        st.write("7. Finish the game or return to the menu.")


    # EXIT

    elif menu == "Exit":

        st.header("Exit Game")

        st.write(
            "Thank you for playing OverIndulgent."
        )

        st.info(
            "You may close the browser tab to exit."
        )
