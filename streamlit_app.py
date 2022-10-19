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
    a1, a2 = st.columns([5, 2])
    a1.write("""
    ### Information
    - enseignement supérieur (Université d'état de Saratov, 1997)
    - spécialité "professeur de Mathématiques et d'informatique"
    - doctorat en sciences de l'éducation (2000 -...)
    - programmeur (langages de base Python, JavaScript)
    - vainqueur du projet éducation (2008, 1M Euro), chef de projet
    - participant au projet" éducation " (2016, 1,5M Euro), chef d'une petite partie du projet
    - livre "les Bases de la programmation pour les étudiants", pour les étudiants en sciences humaines
    - livre "Python: application pratique" [link](https://t.ly/rCCw), projets en langage simple à complexe
    - livre "Blockchain: contacts intelligents" [link](https://t.ly/FOc8), rédaction de contrats intelligents de simple à complexe
    - certificats et diplômes obtenus pendant le travail [link](https://t.ly/7FE-)

    """)
    a1.write("""
    ### Références
    - professeur à l'institut (2000-2006) [link](https://t.ly/d9zy), création de cours de programmation, participation à des conférences, préparation aux examens finaux
    - professeur à l'institut (2006-2015) [link](https://t.ly/aa6l), participation aux activités de projet, contrôle des relations internationales, participation à des conférences internationales
    - programmation freelance (2015-2019), création de sites Web pour les entreprises, travail en tant qu'administrateur de site, gestionnaire de contenu, directeur des relations publiques
    - professeur de collège (2019-...) [link](https://disk.yandex.ru/d/DGhMJddbb3fuVg), préparation et tenue de compétitions régionales sur la blockchain, développement de cours de programmation
    """)
    a1.write("""
    ### Langue étrangère
    - Russe (natif)
    - Français (moyen)
    - Anglais (moyen)
    - Bulgare (primaire)
    - Espagnol (primaire)
    """)
    a1.write("""
    ### Certificats
    - Python [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/1.png)
    - Intro to Machine Learning [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/2.png)
    - Pandas [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/3.png)
    - Intro to Programming [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/4.png)
    """)
    ser = pd.Series(data={'a': 1, 'b': 2, 'c': 3})
    df = pd.DataFrame(ser, columns=('111', '222', '333'))
    a1.table(df)

    a2.write("""
    ### Pile technologique
    - Python
    - Spark
    - Spark SQL
    - Spark RDD
    - AWS
    - Web-design
    - Web-programmation
    """)

if selected == "Projects":
    st.title("Projects page")
    b1, b2 = st.columns(2)
    b1.write("""
    ### Level 1
    - [Simple Stock Price](https://e1m7-projects-project01-simple-stock-pricemyapp-kcdmo6.streamlitapp.com/)
    - [Simple Bioinformatics DNA count](https://e1m7-proj-project02-simple-bioinformatics-dna-countmyapp-k6rqf0.streamlitapp.com/)
    - [NBA Player Stats Explorer](https://e1m7-projects-project03-basketballpy-app-yzpnyj.streamlitapp.com/)
    - [NFL Football Stats Explorer](https://e1m7-projects-project04-footballmy-app-t0md5t.streamlitapp.com/)
    - [Simple Iris Flower Prediction](https://e1m7-projects-project07-iris-datamy-app-5up9d9.streamlitapp.com/)
    """)
    b2.write("""
    ### Level 2
    """)

if selected == "Contact":
    st.title("Contact page")
    c1, c2 = st.columns(2)
    c1.image(Image.open('avatar2.jpg'))
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