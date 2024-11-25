import streamlit as st
from transformers import pipeline
import streamlit as st
st.title("Mi Portafolio de Proyectos")
st.sidebar.title("Navegación")

opciones = ["Inicio", "Proyecto 1: NLP", "Proyecto 2: ML", "Proyecto 3: Data Analysis"]
seleccion = st.sidebar.radio("Selecciona un proyecto:", opciones)

if seleccion == "Inicio":
    st.write("¡Bienvenido a mi portafolio!")

elif seleccion == "Proyecto 1: NLP":
    st.write("Aquí se mostrará mi trabajo en Procesamiento de Lenguaje Natural.")


    st.title("Modelo de Clasificación de Texto")
    text = st.text_area("Introduce un texto:")
    if st.button("Clasificar"):
        # classifier = pipeline("sentiment-analysis")
        # result = classifier(text)
        result = 'holap'
        st.write(result)

elif seleccion == "Proyecto 2: ML":
    st.write("Aquí se mostrará mi trabajo en Machine Learning.")
elif seleccion == "Proyecto 3: Data Analysis":
    st.write("Aquí se mostrará mi trabajo en Análisis de Datos.")
