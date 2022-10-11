import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

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
    a1, a2 = st.columns(2)
    a1.write(""" 
        ### Ivan Sedov
        * кандидат наук
        * преподаватель 20+
        * эксперт WorldSkills
    """)
    a2.write("test")


if selected == "Projects":
    st.title("Projects page")

if selected == "Contact":
    st.title("Contact page")
    c1, c2 = st.columns(2)
    c1.image(Image.open('avatar.jpg'))
    c2.write("test")