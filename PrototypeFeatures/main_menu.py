import streamlit as st


def show_menu():

    st.title("OVERINDULGENT")

    st.subheader("Main Menu")

    st.write("Welcome to the factory.")

    st.divider()

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