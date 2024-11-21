
def funcion_limpieza(df):
    import pandas as pd

    # Limpieza de las columnas
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
    df['current_price'] = df['current_price'].str.replace("€", "", regex=False).str.strip()
    df['current_price'] = pd.to_numeric(df['current_price'], errors='coerce')
    df['normal_price'] = df['normal_price'].str.replace("€", "", regex=False).str.strip()
    df['normal_price'] = pd.to_numeric(df['normal_price'], errors='coerce')
    df["model"]= df["model"].str.title()
    
    # Eliminar filas donde ambos precios son nulos
    df.dropna(subset=["current_price", "normal_price"], how="all", inplace = True)
    df=df.reset_index(drop=True)

    return df  



colores_principales = ['blue', 'black', 'white', 'red', 'yellow', 'green', 'brown', 'pink', 'grey', 'gold', 'silver', 'violet', 'gray', 'orange']

# Función para obtener el color más cercano usando fuzzywuzzy
def obtener_color_principal(color):
    import pandas as pd
    from fuzzywuzzy import process
    if pd.isna(color):
        return None
    # Buscar el color más cercano
    color_principal, _ = process.extractOne(color.lower(), colores_principales)
    return color_principal


def columnas_nuevas(df):
    # Crear una nueva columna 'month' para extraer el mes
    df['month'] = df['date'].dt.month
    # Crear una nueva columna 'marcas' usando funcion map desde un diccionario.
    dic_marcas = {'Metcon 9': 'Nike','Metcon 9 Flyease': 'Nike','Air Zoom Tr 1': 'Nike','Metcon 8 Unisex': 'Nike','Legend Essential 3': 'Nike','Mc 3': 'Nike',
    'Flex Experience Rn 12 Prm': 'Nike','Zoom Hyperspeed Court Se Unisex': 'Nike','Nanoflex 2': 'Reebok','Nano': 'Reebok','Nano Court': 'Reebok',
    'Nano Gym': 'Reebok','Nfx Trainer': 'Reebok','Nanoflex Tr 2': 'Reebok','Flexagon Energy': 'Reebok','Nfx': 'Reebok','Flexagon Force 4': 'Reebok',
    'Disperse Xt 3 Unisex': 'Puma','Fuse 3.0': 'Puma','Pwrframe Tr': 'Puma','Tribase Reign 6': 'Under Armour','Reign Lifter Unisex': 'Under Armour',
    'Cxt2': 'Tyr','Cxt1 Trainer Unisex': 'Tyr'}
    df['brand'] = df['model'].map(dic_marcas)
    df['%discount'] = (((df['normal_price'] - df['current_price']) / df['normal_price']) * 100).round(2)
    df['main_color'] = df['color'].apply(obtener_color_principal)
    return df

def funcion_principal(df):
    df = funcion_limpieza(df)
    df = columnas_nuevas(df) 
    return df 