import streamlit as st
import backend as bk

def main():
    st.title('Análisis de Zapatillas de Crossfit')
    
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
    filtered_df = df[
        ((df['month'] == selected_month) | (selected_month == 'All')) & 
        (df['current_price'] >= selected_price_range[0]) & 
        (df['current_price'] <= selected_price_range[1]) & 
        ((df['brand'].isin(selected_brands)) if 'All' not in selected_brands else True)
    ]
    
    # Mostrar DataFrame filtrado
    st.dataframe(filtered_df)
    
    # Mostrar cantidad de resultados
    st.write(f"Total de resultados: {len(filtered_df)}")

if __name__ == '__main__':
    main()
