import streamlit as st
import save_files


def show_scene(username):

    st.title("THE TRUTH")
    st.subheader("Chapter 4: Restricted Area")

    st.write("You finally reach a hidden section of the factory.")
    st.write(
        "Unlike the production floor, this room is clean, quiet, "
        "and strangely luxurious."
    )

    st.write("There are hundreds of files scattered across the desks.")

    st.write("You pick one up.")

    st.warning("PRODUCT EXPERIMENT — CONSUMER MUTATION REPORT")

    st.write(
        "The pills were never designed simply to make people beautiful."
    )

    st.write(
        "The files describe physical and psychological changes "
        "caused by excessive consumption."
    )

    st.write(
        "The wealthy consumers aren't just addicted to the pills. "
        "They are changing."
    )

    st.divider()

    choice = st.radio(
        "What will you do with the evidence?",
        [
            "Take the files",
            "Leave the files",
            "Search for more information"
        ]
    )

    if st.button("CONTINUE", use_container_width=True):

        save_files.save_game(
            username,
            {
                "progress": 5,
                "choice": choice
            }
        )

        st.session_state.progress = 5
        st.session_state.scene_choice = choice
        st.session_state.page = "ending"

        st.rerun()