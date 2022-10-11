import streamlit as st
from streamlit_option_menu import option_menu

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home", "Projects", "Contact"],
        icons = ["house", "book", "envelope"],
        menu_icon = "cast",
        default_index = 0,

    )

if selected == "Home":
    st.title("Home page")
    a1, a2, a3 = st.columns(3)
    a1.image(Image.open('streamlit-logo-secondary-colormark-darktext1.png'))
    a2.metric("Wind", "9 mph", "-8%")
    a3.metric("Humidity", "86%", "4%")


if selected == "Projects":
    st.title("Projects page")

if selected == "Contact":
    st.title("Contact page")