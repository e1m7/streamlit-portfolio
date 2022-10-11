import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout="wide")

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
    a1.write("""
    ### Info
    - кандидат наук
    - программист
    - преподаватель колледжа/университета
    - эксперт WorldSkills блокчейн
    - эксперт WorldSkills веб-дизайн
    """)
    a2.write("""
    ### Стек технологий
    - Python (Flask, Django, Bottle)
    - HTML/CSS/JavaScript
    - NodeJS/Streamlit
    - React/Angular/Vue
    - Blockchain
    """)
    a3.write("""
    ### Иностранные языки
    - Русский (родной)
    - Французский (средний)
    - Английский (средний)
    - Болгарский (начальный)
    - Испанский (начальный)
    """)


if selected == "Projects":
    st.title("Projects page")

if selected == "Contact":
    st.title("Contact page")
    c1, c2 = st.columns(2)
    c1.image(Image.open('avatar.jpg'))
    c2.write("test")