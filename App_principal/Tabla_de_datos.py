import streamlit as st
import pandas as pd

###################################
# Tabla de datos
##################################

st.subheader("Tabla de datos")
st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")

df = pd.read_csv("../Datos/quality_life_2020.csv", sep=";")
st.dataframe(df)

st.page_link("Grafica_de_dispersion.py", label = "Siguiente página")  # El nombre del archivo de la siguiente página

st.page_link("Indicadores_de_calidad_de_vida.py", label = "Página anterior")