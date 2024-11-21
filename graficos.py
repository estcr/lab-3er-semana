


def distribucion_precio_por_marca(df):
    import plotly.express as px

    # Crear el Box Plot comparando 'current_price' por 'marca'
    fig = px.box(df, x='brandt', y='current_price', title="Distribución de Precios por Marca",
                labels={'brandt': 'Marca', 'current_price': 'Precio Actual'},
                color='brandt')  # Colorea el box plot por marca

    return fig



def grafico_precios_por_marca(df):
    """
    Genera un gráfico de subplots 2x3 que compara el promedio de precios mensuales
    para diferentes marcas, destacando los valores mínimos y máximos.

    Parámetros:
        - df: DataFrame que contiene las columnas 'brandt', 'current_price', 'normal_price' y 'month'.

    Retorna:
        - fig: Objeto Plotly Figure listo para ser mostrado.
    """
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # Crear un subplot 2x3 para tener 5 gráficos (2 filas y 3 columnas)
    fig = make_subplots(
        rows=2, cols=3,  # 2 filas y 3 columnas
        subplot_titles=['Nike', 'Reebok', 'Under Armour', 'Tyr', 'Puma'],  # Los títulos de cada subgráfico
        vertical_spacing=0.1,  # Espacio vertical entre los subgráficos
        horizontal_spacing=0.1,  # Espacio horizontal entre los subgráficos
        shared_yaxes=True,  # Compartir el eje Y entre todos los gráficos
    )

    # Lista de marcas para filtrar y crear gráficos
    marcas = ['Nike', 'Reebok', 'Under Armour', 'Tyr', 'Puma']

    # Iterar sobre las marcas para crear los gráficos y agregarlos a la cuadrícula
    for i, marca in enumerate(marcas):
        # Filtrar los datos para cada marca
        df_filtered = df[(df['brandt'] == marca) & (df['current_price'] != df['normal_price'])]
        promedios_marca = df_filtered.groupby('month')['current_price'].mean().round(2).reset_index()

        # Calcular los valores mínimo y máximo de 'current_price'
        min_price = promedios_marca['current_price'].min()
        max_price = promedios_marca['current_price'].max()

        # Crear una columna adicional 'color' para marcar los valores mínimos y máximos
        promedios_marca['color'] = promedios_marca['current_price'].apply(
            lambda x: 'minimo' if x == min_price else ('maximo' if x == max_price else 'normal')
        )

        # Crear el gráfico de barras para la marca actual
        trace = go.Bar(
            x=promedios_marca['month'],
            y=promedios_marca['current_price'],
            name=marca,
            marker_color=promedios_marca['color'].map({'minimo': 'green', 'maximo': 'red', 'normal': 'blue'}),
            hovertemplate="Mes: %{x}<br>Precio Promedio: €%{y:.2f}<extra></extra>"
        )

        # Determinar la posición del gráfico en la cuadrícula (filas, columnas)
        if marca == 'Tyr':
            row = 2  # Para Tyr ponemos en la fila 2
            col = 1  # En la primera columna
        elif marca == 'Puma':
            row = 2  # Para Puma ponemos en la fila 2
            col = 2  # En la segunda columna
        else:
            row = 1 + i // 3  # Para el resto de marcas, la primera fila
            col = 1 + i % 3  # Para las 3 primeras marcas, ajustar en las primeras columnas

        # Añadir el gráfico al subplot
        fig.add_trace(trace, row=row, col=col)

    # Actualizar el diseño del gráfico
    fig.update_layout(
        title="Promedio de Precios por Mes para Diferentes Marcas",
        showlegend=False,  # No mostrar leyenda global
        height=700,  # Ajustar la altura de la figura para eliminar el espacio extra
        width=900,  # Ajustar el ancho de la figura
        title_x=0.5,  # Centrar el título global
        title_y=0.95,  # Centrar el título verticalmente
    )

    # Ajustar los títulos de los ejes y el formato
    fig.update_xaxes(
        tickmode='array',
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        ticktext=["Ene", "Feb", "Mar", "Abr", "May", "Jun", 
                  "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    )

    # Actualizamos el título del eje Y para los gráficos de la primera fila
    fig.update_yaxes(title_text="Precio Promedio (€)", row=1, col=1)

    # Ahora añadimos el título del eje Y para la segunda fila de gráficos (Tyr y Puma)
    fig.update_yaxes(title_text="Precio Promedio (€)", row=2, col=1)

    return fig



def grafico_precios_modelos_importantes(df, titulo="Comparación de Precios Promedios por Mes"):
    """
    Genera un gráfico de líneas para comparar los precios promedio de modelos específicos por mes.

    Parámetros:
        - df: DataFrame, contiene las columnas 'model', 'month', y 'current_price'.
        - titulo: Cadena, título del gráfico (opcional).
    
    Retorna:
        - fig: Objeto de Plotly Figure listo para ser mostrado.
    """
    import plotly.express as px
    # Modelos seleccionados para analizar
    modelos_seleccionados = ['Metcon 9', 'Tribase Reign 6', 'Nano']

    # Filtrar los modelos deseados
    df_filtered = df[df['model'].isin(modelos_seleccionados)]

    # Agrupar por modelo y mes, y calcular el precio promedio
    df_grouped = df_filtered.groupby(['month', 'model'])['current_price'].mean().reset_index()

    # Crear el gráfico de líneas
    fig = px.line(df_grouped, x='month', y='current_price', color='model',
                  title=titulo,
                  labels={
                      'month': 'Mes', 
                      'current_price': 'Precio Promedio (€)', 
                      'model': 'Modelo'
                  },
                  line_group='model')  # Asegura que cada modelo tenga su propia línea

    # Mejorar la visualización del eje X para que los nombres de los meses se muestren de forma legible
    fig.update_xaxes(
        tickmode='array',
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        ticktext=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    )
    fig.update_xaxes(tickangle=45)  # Inclinar las etiquetas del eje X para facilitar su lectura
    
    return fig


def grafico_precios_por_modelo(df):
    """
    Genera un gráfico de dispersión que compara los precios promedio actuales y normales
    para modelos específicos agrupados por color principal.

    Parámetros:
        - df: DataFrame que contiene las columnas 'model', 'main_color', 'current_price', y 'normal_price'.

    Retorna:
        - fig: Objeto Plotly Figure listo para ser mostrado.
    """
    import plotly.express as px

    # Modelos específicos que queremos analizar
    modelos_seleccionados = ['Nano', 'Metcon 9', 'Tribase Reign 6']

    # Filtrar y agrupar los datos por modelo y color principal, calculando los promedios de precios
    df_filtered = df[df['model'].isin(modelos_seleccionados)].groupby(
        ['model', 'main_color'], as_index=False
    ).agg({
        'current_price': 'mean',  # Promedio del precio actual
        'normal_price': 'mean'   # Promedio del precio normal
    })

    # Crear el gráfico de dispersión
    fig = px.scatter(
        df_filtered, 
        x="current_price",  # Eje X: current_price
        y="normal_price",   # Eje Y: normal_price
        color="model",      # Colorear por modelo
        size='normal_price',  # Tamaño de los puntos basado en el precio normal
        hover_data=['model', 'main_color'],  # Mostrar modelo y color principal al pasar el ratón
        title="Gráfico de Precios Segun Variación por Color en Modelos Más Importantes",
        labels={
            "current_price": "Precio Actual (€)",  # Título personalizado para el eje X
            "normal_price": "Precio Normal (€)",   # Título personalizado para el eje Y
            "model": "Modelo",                    # Cambiar título de la leyenda
            "main_color": "Color Principal"       # Cambiar título del símbolo
        }
    )

    return fig


def grafico_precios_agrupados(df):
    """
    Genera un gráfico de dispersión que compara los precios promedio actuales y normales,
    agrupados por marca y color principal.

    Parámetros:
        - df: DataFrame que contiene las columnas 'brandt', 'main_color', 'current_price', y 'normal_price'.

    Retorna:
        - fig: Objeto Plotly Figure listo para ser mostrado.
    """
    import plotly.express as px

    # Agrupar por marca y color principal, calculando los promedios de precios
    df_grouped = df.groupby(['brandt', 'main_color']).agg(
        avg_current_price=('current_price', 'mean'),
        avg_normal_price=('normal_price', 'mean')
    ).reset_index()

    # Crear el gráfico con los datos agrupados
    fig = px.scatter(
        df_grouped, 
        x="avg_current_price", 
        y="avg_normal_price", 
        color="brandt", 
        size='avg_normal_price', 
        hover_data=['brandt', 'main_color'], 
        symbol='main_color',
        title="Promedio de Precios: Actual vs Normal por Marca y Color")

    return fig


def ejecutar_graficos(df):
    distribucion_precio_por_marca(df).show()
    grafico_precios_por_marca(df).show()
    grafico_precios_modelos_importantes(df, titulo="Comparación de Precios Promedios por Mes").show()
    grafico_precios_por_modelo(df).show()
    grafico_precios_agrupados(df).show()
