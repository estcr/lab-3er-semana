import streamlit as st
import backend as bk

def main():
    st.title('Análisis de Zapatillas de Crossfit')
    
    # Descripción del análisis
    st.markdown("""
    ### Análisis de Precios de Zapatillas de Crossfit

    Este cuaderno tiene como objetivo principal ejecutar el análisis de precios de zapatillas de Crossfit utilizando las funciones previamente desarrolladas. 

    A través de este análisis, se busca:
    - Identificar las variaciones en los precios normales y en oferta.
    - Analizar las diferencias entre marcas, colores y modelos.
    - Generar visualizaciones para extraer conclusiones clave sobre los patrones de precios y promociones.

    El análisis fue realizado mediante un conjunto de funciones para la limpieza y visualización de datos, asegurando que los datos sean procesados de manera eficiente y reproducible.
    """)
    
    # Load data
    df = bk.load_data()
    
    # Sidebar
    st.sidebar.header("Filtros")
    
    # Filtrar por mes con opción "All"
    unique_months = ['All'] + df['month'].dropna().unique().tolist()
    selected_month = st.sidebar.selectbox("Selecciona un mes", options=unique_months)
    
    # Filtrar por rango de precios
    min_price, max_price = int(df['current_price'].min()), int(df['current_price'].max())
    selected_price_range = st.sidebar.slider(
        "Selecciona un rango de precios",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price)
    )
    
    # Filtrar por marca con opción "All"
    unique_brands = ['All'] + df['brand'].dropna().unique().tolist()
    selected_brands = st.sidebar.multiselect("Selecciona marcas", options=unique_brands, default='All')
    
    # Aplicar filtros
    filtered_df = df[(
        (df['month'] == selected_month) | (selected_month == 'All')
    ) & (
        df['current_price'] >= selected_price_range[0]
    ) & (
        df['current_price'] <= selected_price_range[1]
    ) & (
        (df['brand'].isin(selected_brands)) if 'All' not in selected_brands else True
    )]
    
    # Mostrar DataFrame filtrado
    st.dataframe(filtered_df)
    
    # Mostrar cantidad de resultados
    st.write(f"Total de resultados: {len(filtered_df)}")

    # Resultados y Conclusiones
    st.markdown("""
    ## Resultados y Conclusiones

    A través de los gráficos generados, se destacan los siguientes puntos clave:

    1. **Variación de Precios por Marca**:
       - Las marcas muestran diferencias significativas en sus rangos de precios.
       - En los gráficos de barras, se identificaron los meses más baratos (verde) y más caros (rojo) para cada marca.

    2. **Análisis de los Modelos Más Populares**:
       - Los gráficos de líneas muestran fluctuaciones en los precios de los tres modelos más importantes.
       - Esto sugiere que las campañas de marketing y promociones tienen un impacto directo en los precios.

    3. **Relación entre Color y Precio**:
       - Los gráficos de dispersión muestran que ciertos colores pueden influir en el precio final.
       - Los descuentos no siempre son uniformes entre los diferentes colores de un mismo modelo.

    4. **Distribución de Precios**:
       - Las visualizaciones revelan una amplia variabilidad en los precios de diferentes marcas, lo que resalta la importancia de segmentar las ofertas según el mercado objetivo.

    ### Próximos Pasos
    - Automatizar la obtención de datos en tiempo real mediante web scraping.
    - Implementar un modelo predictivo para identificar las fechas más probables de descuentos.
    - Diseñar una API que notifique a los consumidores sobre posibles ofertas.
    """)
    
    # Ejecutar gráficos
    bk.ejecutar_graficos(df)

    # Sidebar con información del autor
    st.sidebar.markdown("""
    ### Autor:
    Esteban Cristos Muzzupappa
    
    - [Linkedin](https://www.linkedin.com/in/esteban-daniel-cristos-muzzupappa-37b72635/)
    - [GitHub](https://github.com/estcr)
    """)

if __name__ == '__main__':
    main()
