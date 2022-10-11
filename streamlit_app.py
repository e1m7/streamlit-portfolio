import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "Projects", "Contact"],
        icons = ["house", "book", "envelope"],
        menu_icon = "cats",
        default_index = 0,

    )

if selected == "Home":
    st.title("Home page")

if selected == "Projects":
    st.title("Projects page")

if selected == "Contact":
    st.title("Contact page")