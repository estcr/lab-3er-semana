import pandas as pd
import funciones as f
import graficos as g


def load_data():
    df=pd.read_csv(r"https://raw.githubusercontent.com/estcr/lab-3er-semana/refs/heads/main/zalando/data/datos_aleatorios_2023.csv")
    df=funcion_principal(df)
    return df

def funcion_principal(df):
    df = f.funcion_limpieza(df)
    df = f.columnas_nuevas(df) 
    return df 

def ejecutar_graficos(df):
    g.distribucion_precio_por_marca(df).show()
    g.grafico_precios_por_marca(df).show()
    g.grafico_precios_modelos_importantes(df, titulo="Comparación de Precios Promedios por Mes").show()
    g.grafico_precios_por_modelo(df).show()
    g.grafico_precios_agrupados(df).show()