import streamlit as st
import save_files


def show_scene(username):

    st.title("SOMETHING IS WRONG")

    st.subheader("Chapter 3: The Factory Floor")

    choice = st.session_state.get(
        "scene_choice",
        ""
    )

    if choice == "Hide inside the storage room":

        st.write(
            """
            You quietly slip into the storage room
            and shut the door behind you.
            """
        )

        st.write(
            """
            The footsteps pass by.

            You hold your breath.
            """
        )

        st.write(
            """
            Then you hear something breathing
            on the other side of the door.
            """
        )

    elif choice == "Run toward the emergency exit":

        st.write(
            """
            You sprint toward the emergency exit.
            """
        )

        st.write(
            """
            The lights flicker.

            Something moves at the end of the hallway.
            """
        )

        st.write(
            """
            You stop.

            Whatever it is...
            it doesn't look human.
            """
        )

    else:

        st.write(
            """
            You decide to go deeper into the factory.
            """
        )

        st.write(
            """
            The further you walk, the quieter it becomes.
            """

        )

        st.write(
            """
            You eventually reach a restricted area
            that workers are never supposed to enter.
            """
        )

    st.divider()

    st.warning(
        "You hear a strange sound nearby."
    )

    choice2 = st.radio(
        "What will you do?",
        [
            "Investigate the sound",
            "Keep moving",
            "Hide and wait"
        ]
    )

    if st.button(
        "CONTINUE",
        use_container_width=True
    ):

        save_files.save_game(
            username,
            {
                "progress": 4,
                "choice": choice2
            }
        )

        st.session_state.progress = 4
        st.session_state.scene_choice = choice2
        st.session_state.page = "scene4"

        st.rerun()