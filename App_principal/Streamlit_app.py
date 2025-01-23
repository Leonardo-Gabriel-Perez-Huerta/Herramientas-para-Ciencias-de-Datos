import streamlit as st

# Define las páginas con sus rutas y títulos en una sola lista
pages = [
    st.Page("Indicadores_de_calidad_de_vida.py", title="Indicadores de Calidad de Vida"),
    st.Page("Tabla_de_datos.py", title="Tabla de Datos"),
    st.Page("Grafica_de_dispersion.py", title="Gráfica de Dispersión"),
    st.Page("Grafica_de_cajas.py", title="Gráfica de Cajas"),
    st.Page("Histograma.py", title="Histograma"),
    st.Page("Grafica_de_barras.py", title="Gráfica de Barras")
]

# Crear la navegación
pg = st.navigation(pages)

# Ejecutar la navegación
pg.run()







