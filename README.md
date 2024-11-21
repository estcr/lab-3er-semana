# Análisis de Precios de Zapatillas de Crossfit

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar los precios de las zapatillas de Crossfit en oferta y precio normal a través de un proceso de web scraping, utilizando datos obtenidos de sitios web de marcas específicas. A partir de esta información, se generan visualizaciones de las variaciones de precios, se analizan patrones estacionales y se proponen recomendaciones para los consumidores y empresas del sector.

El proceso de análisis y limpieza de datos se ha realizado con el fin de proporcionar a la empresa de retail información sobre las mejores épocas para realizar campañas de marketing y optimizar sus precios.

## Objetivo del Proyecto
El análisis de precios se realizó con el objetivo de:

1. **Obtener precios actuales y precios en oferta** para las zapatillas de Crossfit más populares.
2. **Limpiar y procesar los datos** para asegurar la correcta estructura y análisis.
3. **Visualizar las variaciones de precios** mediante gráficos y obtener insights acerca de los mejores momentos para las ofertas.
4. **Establecer conclusiones y recomendaciones** sobre la estacionalidad de los precios y la variabilidad entre marcas y colores de los productos.

## Herramientas Utilizadas
Para el desarrollo de este proyecto, se utilizaron las siguientes herramientas y bibliotecas:

- **Python**: Lenguaje principal utilizado para el procesamiento y análisis de los datos.
- **Selenium**: Para realizar web scraping dinámico en sitios web que requieren interacción con JavaScript.
- **BeautifulSoup**: Para la extracción de datos de HTML.
- **Pandas**: Para la manipulación y limpieza de los datos.
- **NumPy**: Para la creación de datos ficticios y cálculos numéricos.
- **Fuzzywuzzy**: Para la estandarización y coincidencia de texto, especialmente útil en la limpieza de nombres y colores.
- **Matplotlib & Seaborn**: Para la visualización de los datos y la creación de gráficos.
- **Datetime**: Para la gestión de fechas y tiempos, y la creación de fechas ficticias.
- **Visual Studio Code**: Editor de código utilizado en el desarrollo del proyecto.
- **GitHub**: Plataforma utilizada para almacenar el código y colaborar en el desarrollo.

## Proceso de Limpieza de Datos
Durante el análisis, se enfrentaron varios desafíos relacionados con la obtención y limpieza de datos. A continuación se describen los principales pasos realizados:

1. **Obtención de datos**: A través de Selenium y BeautifulSoup se realizaron solicitudes HTTP a los sitios web y se extrajeron los datos relevantes para el análisis, como los precios actuales y los precios en oferta.
   
2. **Limpieza y procesamiento de datos**:
   - Se eliminaron columnas irrelevantes y se transformaron datos en el formato adecuado (por ejemplo, fechas y números).
   - Se utilizaron técnicas como `map` y un diccionario para asignar las marcas a cada modelo de zapatilla.
   - Se utilizó `fuzzywuzzy` para la coincidencia y filtrado de colores principales de las zapatillas.
   - Se creó una columna adicional para calcular el **porcentaje de descuento** entre el precio normal y el precio de oferta.

3. **Generación de datos ficticios**:
   - Se creó un **DataFrame ficticio** para el año 2023, con variaciones en los precios de las zapatillas dentro de un rango del 90% al 110%.
   - Se generaron fechas ficticias para simular el comportamiento de precios en distintos meses.

4. **Agrupación y análisis**:
   - Se agruparon los datos por modelo y color, y se calcularon promedios de precios por mes.
   - Se crearon gráficos para mostrar las variaciones de precios entre las marcas y los colores de las zapatillas.

## Principales Problemas Encontrados
Durante el desarrollo del proyecto se presentaron algunos desafíos importantes:

1. **Web Scraping**: La dificultad principal radicó en la obtención de datos precisos y completos, especialmente debido a la variabilidad de las páginas web que se tenían que scrapear y las diferencias en el formato de los datos.
   
2. **Análisis de Datos Complejos**: Con tantos modelos, colores y precios, la visualización de patrones y la creación de conclusiones claras fue desafiante. Fue necesario aplicar técnicas de limpieza y agrupación avanzadas para poder analizar los datos de manera efectiva.

## Visualizaciones y Resultados

A continuación, se detallan algunos de los gráficos generados a partir del análisis:

1. **Gráfico de Barras por Marca**:
   - Este gráfico muestra los meses con **precios más baratos** (en verde) y **precios más caros** (en rojo) por cada marca de zapatillas.
   - Permite observar la variabilidad de precios y detectar las mejores épocas de descuento.

2. **Gráfico de Líneas para Modelos Específicos**:
   - Se analizó la variación de precios de los tres modelos más populares de zapatillas, destacando las fluctuaciones que ocurren en ciertas épocas del año.
   - Este gráfico ayuda a entender cómo las campañas de marketing afectan los precios de los modelos a lo largo del tiempo.

3. **Gráfico de Dispersión por Color**:
   - En este gráfico se puede observar la relación entre el precio de las zapatillas y su color principal. Algunas zapatillas del mismo modelo tienen precios significativamente diferentes dependiendo del color, lo que sugiere que las promociones o la popularidad de ciertos colores influyen en los precios.

4. **Distribución de Precios por Marca**:
   - Se destaca la gran **variabilidad de precios** entre diferentes marcas, lo que indica la necesidad de una segmentación de precios basada en la marca, modelo y color de la zapatilla.

## Conclusiones

- **Estacionalidad de los Precios**: Se observó una clara **variación estacional** en los precios, con descuentos significativos durante los meses de primavera y principios de verano. Esto sugiere que las marcas tienden a lanzar ofertas en esas fechas.
  
- **Diferencias entre Modelos y Colores**: Los precios de las zapatillas varían dependiendo del modelo y el color. Esto se debe probablemente a factores como la demanda y la oferta de ciertos modelos o colores.

- **Recomendaciones para la Empresa**:
  1. **Promociones estacionales**: Focalizar las campañas de marketing y descuentos en los meses de primavera y verano para aprovechar las fluctuaciones en los precios.
  2. **Segmentación por modelo y color**: Ofrecer promociones específicas para ciertos modelos o colores que tienden a tener precios más bajos en ciertas épocas del año.

## Plan Futuro
El próximo paso en este proyecto es **automatizar el proceso de scraping** para obtener datos actualizados diariamente, de manera que podamos construir un **modelo predictivo** para prever las fechas y los precios de las ofertas de las marcas de zapatillas de Crossfit. La idea es utilizar esta información para crear una **API** que notifique a los usuarios sobre las mejores ofertas en tiempo real.

## Entregables

- **Código**: Scripts completos de limpieza, análisis y visualización de datos.
- **Visualizaciones**: Gráficos generados para ilustrar los resultados del análisis.
- **Informe**: Resumen con las conclusiones del análisis y las recomendaciones.

## Enlaces

- **Dataset Utilizado**: [Enlace al Dataset] (si aplica).
- **Repositorio en GitHub**: [Tu repositorio en GitHub] (si aplica).

## Participantes

- **Esteban Cristos** - [Enlace a tu LinkedIn] (si aplica).
