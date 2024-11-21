import streamlit as st
import backend as bk

def main():
    
    st.title('Analisis Zapatillas Crossfit')
    
    # Load data 
    df = bk.load_data()
    st.dataframe(df)

    # Interactive widgets
    st.sidebar.header('Controls')
    meses = st.sidebar.slider('month', min_value=0, max_value=12, value=0, step=1)
    
        
if __name__ == '__main__':
    main()