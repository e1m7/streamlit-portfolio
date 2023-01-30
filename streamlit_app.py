import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plost

st.set_page_config(layout="wide")

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
    ### Langue étrangère
    - Russe (natif)
    - Français (moyen)
    - Anglais (moyen)
    - Bulgare (primaire)
    - Espagnol (primaire)
    ### Certificats
    Kaggle
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/1.png) Python
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/2.png) Intro to Machine Learning
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/3.png) Pandas
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/4.png) Intro to Programming
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/5.png) Intermediate Machine Learning
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/14.png) Intro to Game AI and Reinforcement Learning
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/20.png) Data Visualisations
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/21.png) Feature Engineering
    Data Flair
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/hadoop.png) Big Data Hadoop
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/spark.png) Apache Spark Scala
    Stepik
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/9.png) Python Programming
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/10.png) Python: Basics and application
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/11.png) Blockchain programming and smart contracts
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/12.png) Cryptoeconomics and Blockchain Technology
    - [image](https://github.com/e1m7/streamlit-portfolio/blob/main/image/13.png) The foundations of digital transformation
    """)
    a2.write("""
    ### Pile technologique
    - Python
    - Pandas
    - NumPy
    - Spark Core
    - Spark SQL
    - Spark Streaming
    - Spark RDD
    ---
    - Cat Boosting
    - Decision tree
    - Random forest
    - Lasso
    - LGBMR/LGBMC
    - XGBR/XGBC
    - SVM
    - KNN
    """)

if selected == "Projects":
    st.title("Projects page")
    b1, b2, b3 = st.columns(3)
    b1.write("""
    ### Applications
    Applications simples
    - [Simple Stock Price](https://e1m7-projects-project01-simple-stock-pricemyapp-kcdmo6.streamlitapp.com/)
    - [Simple Bioinformatics DNA count](https://e1m7-proj-project02-simple-bioinformatics-dna-countmyapp-k6rqf0.streamlitapp.com/)
    - [NBA Player Stats Explorer](https://e1m7-projects-project03-basketballpy-app-yzpnyj.streamlitapp.com/)
    - [NFL Football Stats Explorer](https://e1m7-projects-project04-footballmy-app-t0md5t.streamlitapp.com/)
    - [Simple Iris Flower Prediction](https://e1m7-projects-project07-iris-datamy-app-5up9d9.streamlitapp.com/)
    - [Into to Machine Learning](https://www.kaggle.com/code/lavagod/intro-to-machine-learning-tutorial)
    - [Intermediate Machine Learning](https://www.kaggle.com/code/lavagod/intermediate-machine-learning-tutorial)
    - [Human Learning](https://www.kaggle.com/code/lavagod/102-gleb-part3-human-learning-rus)
    - [Machine Learning](https://www.kaggle.com/code/lavagod/102-gleb-part4-machine-learning-rus)
    """)
    b2.write("""
    ### Pipeline
    Développements simples
    - [Create pipeline salary](https://e1m7-projects-prokect10-salarymy-app-dids65.streamlitapp.com/)
    - [Create pipeline cars](https://e1m7-projects-prokect11-carsmy-app-xrcgrz.streamlitapp.com/)
    - [Disaster Tweets](https://www.kaggle.com/code/lavagod/disaster-tweets-minimum-code-0-80232)
    - [House Price](https://www.kaggle.com/code/lavagod/house-prices-minimum-code-0-15755)
    - [Spaceship Titanic](https://www.kaggle.com/code/lavagod/spaceship-titanic-minimum-code-0-7725)
    - [Digit Recognizer](https://www.kaggle.com/code/lavagod/digit-recognizer-minimum-code-0-97846)
    - [Titanic Survived](https://www.kaggle.com/code/lavagod/titanic-minimum-code-0-78468) ♚
    - [House Prices](https://www.kaggle.com/code/lavagod/house-prices-pipeline-code-0-14893)
    - [Spaceship Titanic](https://www.kaggle.com/code/lavagod/spaceship-titanic-pipeline-code-0-78185)
    - [Mercedes Catboost + Shap](https://www.kaggle.com/code/lavagod/mercedes-catboost-shap-tutorial) ♚
    """)
    b3.write("""
    ### Modèles
    Modèles simples
    - [Gamma Telescope: KNeighbors](https://e1m7-projects-model1my-app-u03h4l.streamlitapp.com/)
    - [Gamma Telescope: Native Bayes](https://e1m7-projects-model2my-app-xvylyf.streamlitapp.com/)
    - [The sense text: 5 models](https://e1m7-projects-model3-positivemy-app-60g5hu.streamlit.app/)
    - [Super Heroes](https://www.kaggle.com/code/lavagod/super-heroes-tutorial)
    - [Arne Svenson prisoners](https://www.kaggle.com/code/lavagod/arne-svenson-prisoners-tutorial) ♚
    - [Student performance](https://www.kaggle.com/code/lavagod/student-performance-tutorial)
    - [Halite: game](https://www.kaggle.com/code/lavagod/halite-tutorial-rus)
    - [Catalogue de Messier](https://www.kaggle.com/code/lavagod/catalogue-de-messier-tutorial)
    - [PC Season 3 Episode 2](https://www.kaggle.com/code/lavagod/pc-s0302-minimum-code-0-81996) 
    - [PC Season 3 Episode 3](https://www.kaggle.com/code/lavagod/pc-s03e03-minimum-code-0-86235)
    """)

if selected == "Contact":
    st.title("Contact page")
    c1, c2 = st.columns(2)
    c1.image(Image.open('image/avatar.jpg'))
    c2.write("""
    ### Relations
    - телефон 123-456-789
    - address@server.ru
    ### Sites
    - https://platform.stratascratch.com/user/e1m7
    - https://www.codewars.com/users/e1m7
    - https://exercism.org/profiles/e1m7
    - https://www.kaggle.com/lavagod
    - https://github.com/e1m7
    """)