import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plost

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
    a1, a2 = st.columns(2)
    b1, b2 = st.columns(2)
    a1.write("""
    ### Информация
    - высшее образование (Саратовский университет, 1997)
    - специальность "учитель математики и информатики"
    - кандидат падагогических наук (2000-...)
    - программист (Python, JavaScript)
    - победитель проекта "Образование" (2008, 1М евро)
    - участник проекта "Образование" (2016, 1,5М евро)
    - книга "Основы программирования для студентов"
    - книга "Python: практическое применение" [link](https://t.ly/rCCw)
    - книга "Блокчейн: смарт-контакты" [link](https://t.ly/FOc8)
    - сертификаты и грамоты [link](https://t.ly/7FE-)
    """)
    b1.write("""
    ### Опыт работы
    - преподаватель института (2000-2006) [link](https://t.ly/d9zy)
    - преподаватель университета (2006-2015) [link](https://t.ly/aa6l)
    - фриланс программирование (2015-2019)
    - преподаватель колледжа (2019-...) [link](https://disk.yandex.ru/d/DGhMJddbb3fuVg)
    """)
    a2.write("""
    ### Стек технологий
    - Python/Pandas/Spark/SQL
    - Django/Flask/Bottle
    - HTML/CSS/JavaScript
    - NodeJS/React/Angular/Vue
    - Машинное обучение (Python)
    - Нейронные сети (JavaScript)
    - API/FastAPI/RestAPI
    """)
    b2.write("""
    ### Иностранные языки
    - Русский (родной)
    - Французский (средний)
    - Английский (средний)
    - Болгарский (начальный)
    - Испанский (начальный)
    """)

if selected == "Projects":
    st.title("Projects page")
    b1, b2 = st.columns(2)
    b1.write("""
    - [Simple Stock Price](https://e1m7-projects-project01-simple-stock-pricemyapp-kcdmo6.streamlitapp.com/)
    - [Simple Bioinformatics DNA count](https://e1m7-proj-project02-simple-bioinformatics-dna-countmyapp-k6rqf0.streamlitapp.com/)
    - [NBA Player Stats Explorer](https://e1m7-projects-project03-basketballpy-app-yzpnyj.streamlitapp.com/)
    - [NFL Football Stats Explorer](https://e1m7-projects-project04-footballmy-app-t0md5t.streamlitapp.com/)
    """)

if selected == "Contact":
    st.title("Contact page")
    c1, c2 = st.columns(2)
    c1.image(Image.open('avatar.jpg'))
    c2.write("""
    ### Контакты
    - телефон 123-456-789
    - address@server.ru
    ### Ссылки
    - https://www.codewars.com/users/e1m7
    - https://exercism.org/profiles/e1m7
    - https://www.kaggle.com/lavagod
    - https://github.com/e1m7
    """)