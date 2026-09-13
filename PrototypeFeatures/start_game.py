import streamlit as st
import save_files


def show_game(username):

    st.title("🏭 THE FACTORY")

    st.subheader("Chapter 1: The Urge")

    st.write(
        "You are a factory worker in a society "
        "obsessed with beauty, status, and consumption."
    )

    st.write(
        "The factory produces special pills "
        "that are only available to the rich."
    )

    st.write(
        "Workers are forbidden from using them under "
        "threat of termination."
    )

    st.divider()

    st.warning(
        "You notice a pill sitting on the production line."
    )

    st.write(
        "Nobody is watching..."
    )

    choice = st.radio(
        "What will you do?",
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

            save_files.save_game(
                username,
                {
                    "progress": 2,
                    "choice": "Take the pill"
                }
            )

            st.session_state.progress = 2

            st.success(
                "You secretly take the pill."
            )

            st.write(
                "For a moment, everything feels perfect..."
            )

            st.write(
                "Then you hear the factory alarm."
            )

        else:

            save_files.save_game(
                username,
                {
                    "progress": 2,
                    "choice": "Leave the pill"
                }
            )

            st.session_state.progress = 2

            st.info(
                "You leave the pill behind."
            )

            st.write(
                "But before you can walk away, "
                "you hear something moving behind you..."
            )

    st.divider()

    if st.button(
        "← Back to Main Menu",
        use_container_width=True
    ):

        st.session_state.page = "menu"
        st.rerun()