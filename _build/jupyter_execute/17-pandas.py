#!/usr/bin/env python
# coding: utf-8

# # La biblioteca pandas

# [pandas](https://pandas.pydata.org/) es una biblioteca de Python para análisis y manipulación de datos. Proporciona estructuras de datos y operaciones para manejar tablas numéricas y series temporales.
# 
# El [data frame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) es una estructura rectangular, organizada en filas y columnas, en la cual pandas almacena los datos.

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


# ## Operaciones básicas

# Seguidamente, se describen y ejemplifican algunas de las funciones básicas de pandas.
# 
# En los siguientes ejemplos, se utilizará un conjunto de registros de presencia de felinos (familia *Felidae*) de Costa Rica, obtenido a través de una [consulta al portal de GBIF](https://www.gbif.org/occurrence/download/0016217-210914110416597).

# ### read_csv() - carga de datos

# In[2]:


felidae = pd.read_csv("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/gbif/felidae.csv", sep="\t")


# ### info() - información general sobre un conjunto de datos

# In[3]:


felidae.info()


# ### head(), tail(), sample() - despliegue de filas de un conjunto de datos

# In[4]:


# Primeros 10 registros
felidae.head()


# In[5]:


# Últimos 15 registros
felidae.tail()


# In[6]:


# 5 registros seleccionados aleatoriamente
felidae.sample(5)


# Los contenidos de un data frame también pueden desplegarse al escribir su nombre en la consola de Python.

# In[7]:


felidae


# ### Selección de columnas

# Las columnas que se despliegan en un data frame pueden especificarse mediante una lista.

# In[8]:


# Despliegue de las columnas con el nombre científico, la especie, la fecha, el año, el mes y el día
felidae[["scientificName", "species", "eventDate", "year", "month", "day"]]


# ### Selección de filas

# In[9]:


# Selección de filas correspondientes a jaguares (*Panthera onca*)
panthera_onca = felidae[felidae["species"] == "Panthera onca"]

# Despliegue de los primeros registros
panthera_onca.head()


# In[10]:


# Selección de filas correspondientes a jaguares (*Panthera onca*) o pumas (*Puma concolor*)
panthera_onca_puma_concolor = felidae[(felidae["species"] == "Panthera onca") | (felidae["species"] == "Puma concolor")]

# Despliegue de los primeros registros
panthera_onca_puma_concolor.head(10)


# ## Operaciones de análisis

# ### Graficación

# #### Carga de bibliotecas

# In[11]:


import matplotlib.pyplot as plt # biblioteca de graficación
get_ipython().run_line_magic('matplotlib', 'inline')

import calendar # biblioteca para manejo de fechas


# #### Estilo de los gráficos

# In[12]:


# Estilo de los gráficos
plt.style.use('ggplot')


# #### Ejemplos de gráficos

# ##### Distribución de registros de presencia por año

# In[13]:


# Cambio del tipo de datos del campo de fecha
felidae["eventDate"] = pd.to_datetime(felidae["eventDate"])

# Agrupación de los registros por año
felidae_registros_x_anio = felidae.groupby(felidae['eventDate'].dt.year).count().eventDate

felidae_registros_x_anio


# In[14]:


# Conversión a un dataframe
felidae_registros_x_anio_df = pd.DataFrame({'anio':felidae_registros_x_anio.index, 'registros':felidae_registros_x_anio.values}) 

# Conversión del tipo de la columna de año
felidae_registros_x_anio_df["anio"] = pd.to_numeric(felidae_registros_x_anio_df["anio"], downcast='integer')
felidae_registros_x_anio_df.style.set_precision(2)

felidae_registros_x_anio_df


# In[15]:


# Graficación
felidae_registros_x_anio_df.plot(x='anio', y='registros', kind='bar', figsize=(12,7), color='red')

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por año', fontsize=20)
plt.xlabel('Año', fontsize=16)
plt.ylabel('Cantidad de registros', fontsize=16)


# ##### Distribución de registros de presencia por mes

# In[16]:


# Agrupación de los registros por mes
felidae_registros_x_mes = felidae.groupby(felidae['eventDate'].dt.month).count().eventDate

felidae_registros_x_mes


# In[17]:


# Reemplazo del número del mes por el nombre del mes
felidae_registros_x_mes.index=[calendar.month_name[x] for x in range(1,13)]

felidae_registros_x_mes


# In[18]:


# Gráfico de barras
felidae_registros_x_mes.plot(kind='bar',figsize=(12,7), color='blue', alpha=0.5)

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por mes', fontsize=20)
plt.xlabel('Mes', fontsize=16)
plt.ylabel('Cantidad de registros', fontsize=16);


# ##### Graficación en una línea de tiempo

# In[19]:


# Agrupación de los registros por fecha
registros_x_fecha = felidae.groupby(felidae['eventDate'].dt.date).count().eventDate

registros_x_fecha


# In[20]:


# Gráfico de líneas
registros_x_fecha.plot(figsize=(20,8), color='blue')

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por fecha', fontsize=20)
plt.xlabel('Fecha',fontsize=16)
plt.ylabel('Cantidad de registros',fontsize=16);
plt.legend()


# In[ ]:




