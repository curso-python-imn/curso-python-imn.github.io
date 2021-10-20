#!/usr/bin/env python
# coding: utf-8

# # La biblioteca pandas

# [pandas](https://pandas.pydata.org/) es una biblioteca de Python para análisis y manipulación de datos. Proporciona estructuras de datos y operaciones para manejar tablas numéricas y series temporales. Fue creada por Wes McKinney in 2008. El nombre "pandas" hace referencia tanto a "*Panel Data*" como a "*Python Data Analysis*".
# 
# Como su estructura principal de datos, pandas implementa el [data frame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), el cual es un arreglo rectangular, organizado en filas y columnas.

# ## Instalación

# pandas puede instalarse tanto mediante [Conda](https://conda.io/) como mediante [pip](https://pypi.org/project/pip/).
# 
# ```shell
# # Instalación mediante Conda
# conda install pandas
# 
# # Instalación mediante pip
# pip install pandas
# ```

# ## Carga
# Antes de cargar pandas, debe cargarse antes la biblioteca [numpy](https://numpy.org/), para operaciones de álgebra lineal. Nótese el uso de los alias np y pd, los cuales no son obligatorios, pero sí recomendados.

# In[1]:


import numpy as np # biblioteca para álgebra lineal
import pandas as pd # biblioteca para análisis de datos


# ## Estructuras de datos
# Las dos principales estructuras de datos de pandas son series y dataframes.

# ### Series
# Las series son arreglos unidimensionales que contienen datos de cualquier tipo. Se asemejan a una columna de una tabla.

# In[2]:


primos = [2, 3, 5, 7, 11]

serie_primos = pd.Series(primos)

serie_primos


# Cada elemento de una serie tiene un índice (i.e. posición), comenzando con 0.

# In[3]:


# Primer elemento
print(serie_primos[0])

# Segundo elemento
print(serie_primos[1])


# Los índices también pueden tener etiquetas personalizadas:

# In[4]:


serie_primos = pd.Series(primos, index = ["A", "B", "C", "D", "E"])

serie_primos


# In[5]:


# Elemento en el índice "D"
print(serie_primos["D"])


# ### Dataframes
# Los dataframes son estructuras multidimensionales. Una serie puede verse como una columna de una tabla y un dataframe como una tabla completa. Un dataframe puede construirse a partir de varias series.

# In[6]:


# Dataframe construído a partir de dos series
datos = {
  "pais": ["PA", "CR", "NI"],
  "poblacion": [4.1, 5.0, 6.6]
}

paises = pd.DataFrame(datos)

paises


# El atributo **loc** permite retornar una o más filas de un dataframe:

# In[7]:


# Segundo elemento
paises.loc[1]


# In[8]:


# Segundo y tercer elemento
paises.loc[[1, 2]]


# Los índices de los dataframes también pueden etiquetarse:

# In[9]:


paises = pd.DataFrame(datos, index=["pais0", "pais1", "pais2"])
paises


# In[10]:


# Elemento en "pais0"
paises.loc["pais0"]


# ## Operaciones básicas

# Seguidamente, se describen y ejemplifican algunas de las funciones básicas de pandas.
# 
# En los siguientes ejemplos, se utilizará un conjunto de registros de presencia de felinos (familia *Felidae*) de Costa Rica, obtenido a través de una [consulta al portal de GBIF](https://www.gbif.org/occurrence/download/0016217-210914110416597).

# ### read_csv() - carga de datos

# In[11]:


felidae = pd.read_csv("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/gbif/felidae.csv", sep="\t")


# ### info() - información general sobre un conjunto de datos

# In[12]:


felidae.info()


# ### head(), tail(), sample() - despliegue de filas de un conjunto de datos

# In[13]:


# Primeros 10 registros
felidae.head()


# In[14]:


# Últimos 15 registros
felidae.tail()


# In[15]:


# 5 registros seleccionados aleatoriamente
felidae.sample(5)


# Los contenidos de un data frame también pueden desplegarse al escribir su nombre en la consola de Python.

# In[16]:


felidae


# ### Selección de columnas

# Las columnas que se despliegan en un data frame pueden especificarse mediante una lista.

# In[17]:


# Despliegue de las columnas con el nombre científico, la especie, la fecha, el año, el mes y el día
felidae[["scientificName", "species", "eventDate", "year", "month", "day"]]


# ### Selección de filas

# In[18]:


# Selección de filas correspondientes a jaguares (*Panthera onca*)
panthera_onca = felidae[felidae["species"] == "Panthera onca"]

# Despliegue de los primeros registros
panthera_onca.head()


# In[19]:


# Selección de filas correspondientes a jaguares (*Panthera onca*) o pumas (*Puma concolor*)
panthera_onca_puma_concolor = felidae[(felidae["species"] == "Panthera onca") | (felidae["species"] == "Puma concolor")]

# Despliegue de los primeros registros
panthera_onca_puma_concolor.head(10)


# ## Operaciones de análisis

# ### Graficación

# #### Carga de bibliotecas

# In[20]:


import matplotlib.pyplot as plt # biblioteca de graficación
get_ipython().run_line_magic('matplotlib', 'inline')

import calendar # biblioteca para manejo de fechas


# #### Estilo de los gráficos

# In[21]:


# Estilo de los gráficos
plt.style.use('ggplot')


# #### Ejemplos de gráficos

# ##### Distribución de registros de presencia por año

# In[22]:


# Cambio del tipo de datos del campo de fecha
felidae["eventDate"] = pd.to_datetime(felidae["eventDate"])

# Agrupación de los registros por año
felidae_registros_x_anio = felidae.groupby(felidae['eventDate'].dt.year).count().eventDate

felidae_registros_x_anio


# In[23]:


# Conversión a un dataframe
felidae_registros_x_anio_df = pd.DataFrame({'anio':felidae_registros_x_anio.index, 'registros':felidae_registros_x_anio.values}) 

# Conversión del tipo de la columna de año
felidae_registros_x_anio_df["anio"] = pd.to_numeric(felidae_registros_x_anio_df["anio"], downcast='integer')
felidae_registros_x_anio_df.style.set_precision(2)

felidae_registros_x_anio_df


# In[24]:


# Graficación
felidae_registros_x_anio_df.plot(x='anio', y='registros', kind='bar', figsize=(12,7), color='red')

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por año', fontsize=20)
plt.xlabel('Año', fontsize=16)
plt.ylabel('Cantidad de registros', fontsize=16)


# ##### Distribución de registros de presencia por mes

# In[25]:


# Agrupación de los registros por mes
felidae_registros_x_mes = felidae.groupby(felidae['eventDate'].dt.month).count().eventDate

felidae_registros_x_mes


# In[26]:


# Reemplazo del número del mes por el nombre del mes
felidae_registros_x_mes.index=[calendar.month_name[x] for x in range(1,13)]

felidae_registros_x_mes


# In[27]:


# Gráfico de barras
felidae_registros_x_mes.plot(kind='bar',figsize=(12,7), color='blue', alpha=0.5)

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por mes', fontsize=20)
plt.xlabel('Mes', fontsize=16)
plt.ylabel('Cantidad de registros', fontsize=16);


# ##### Graficación en una línea de tiempo

# In[28]:


# Agrupación de los registros por fecha
registros_x_fecha = felidae.groupby(felidae['eventDate'].dt.date).count().eventDate

registros_x_fecha


# In[29]:


# Gráfico de líneas
registros_x_fecha.plot(figsize=(20,8), color='blue')

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por fecha', fontsize=20)
plt.xlabel('Fecha',fontsize=16)
plt.ylabel('Cantidad de registros',fontsize=16);
plt.legend()


# # Análisis de riesgo ante eventos hidrometeorológicos extremos

# ## Nicoya

# In[30]:


# Lectura de datos
datos = pd.read_csv("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/analisis-riesgo/indicadores-vulnerabilidad-NICOYA.csv")


# ### Tabla de datos por UGM

# In[31]:


# Despliegue de datos
datos


# In[32]:


datos.info()


# In[33]:


datos_belennosarita = datos[datos["COD_DIST"] == 50207]

datos_belennosarita.sample(5)


# ### Distribución porcentual de la población a nivel de distrito

# In[34]:


# Suma de población por distrito
poblacion_x_distrito = datos.groupby(datos['DISTRITO'])['TOTAL'].sum()

poblacion_x_distrito


# In[35]:


# Gráfico de pastel
poblacion_x_distrito.plot.pie()


# ### Características de la población dependiente

# In[36]:


# Suma de población dependiente por distrito
poblaciondependiente_x_distrito = datos.groupby(datos['DISTRITO'])['TOTAL_DEPENDIENTE'].sum()

poblaciondependiente_x_distrito


# In[37]:


# Gráfico de barras
poblaciondependiente_x_distrito.plot.bar()

