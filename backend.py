import pandas as pd
import funciones as f
import graficos as g


def load_data():
    df=pd.read_csv(r"..\zalando\data\datos_aleatorios_2023.csv")
    df=funcion_principal(df)
    return df

def funcion_principal(df):
    df = f.funcion_limpieza(df)
    df = f.columnas_nuevas(df) 
    return df 

def ejecutar_graficos(df):
    import streamlit as st
    st.header("Análisis de Precios")
    
    st.subheader("Distribución de Precios por Marca")
    st.plotly_chart(g.distribucion_precio_por_marca(df))
    
    st.subheader("Precios por Marca")
    st.plotly_chart(g.grafico_precios_por_marca(df))
    
    st.subheader("Comparación de Precios Promedios por Mes")
    st.plotly_chart(g.grafico_precios_modelos_importantes(df, titulo="Comparación de Precios Promedios por Mes"))
    
    st.subheader("Precios por Modelo")
    st.plotly_chart(g.grafico_precios_por_modelo(df))
    
    st.subheader("Precios Agrupados")
    st.plotly_chart(g.grafico_precios_agrupados(df))