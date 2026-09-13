import streamlit as st
import save_files


def show_scene(username):

    st.title("THE ALARM")

    st.subheader("Chapter 2: Termination")

    st.write(
        """
        The factory suddenly goes silent.
        """

    )

    st.write(
        """
        Then the alarm begins to scream.
        Red lights flash across the production floor.
        """

    )

    st.warning(
        "UNAUTHORIZED PILL CONSUMPTION DETECTED."
    )

    st.write(
        """
        You freeze.

        They know.
        """

    )

    st.write(
        """
        Footsteps begin getting closer.
        You need to get out before they find you.
        """
    )

    st.divider()

    choice = st.radio(
        "Where will you go?",
        [
            "Hide inside the storage room",
            "Run toward the emergency exit",
            "Go deeper into the factory"
        ]
    )

    if st.button(
        "CONTINUE",
        use_container_width=True
    ):

        save_files.save_game(
            username,
            {
                "progress": 3,
                "choice": choice
            }
        )

        st.session_state.progress = 3
        st.session_state.scene_choice = choice
        st.session_state.page = "scene3"

        st.rerun()