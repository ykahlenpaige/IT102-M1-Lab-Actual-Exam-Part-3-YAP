import streamlit as st


def show_menu():
    st.sidebar.title("OVERINDULGENT")

    st.sidebar.write("Survival Horror")

    menu = st.sidebar.radio(
        "MAIN MENU",
        [
            "Start Game",
            "Continue",
            "About Game",
            "Exit"
        ]
    )

    return menu
