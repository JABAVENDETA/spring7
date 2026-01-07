import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Analisis del mercado de vehiculos")

st.header("Distribución de precios")

# Casilla para histograma
if st.checkbox("Mostrar histograma del kilometraje"):
    st.write("Distribución del kilometraje de los vehículos")
    fig_hist = px.histogram(df, x="odometer")
    st.plotly_chart(fig_hist)

# Casilla para gráfico de dispersión
if st.checkbox("Mostrar gráfico de dispersión precio vs año"):
    st.write("Relación entre el precio y el año del modelo")
    fig_scatter = px.scatter(df, x="model_year", y="price")
    st.plotly_chart(fig_scatter)