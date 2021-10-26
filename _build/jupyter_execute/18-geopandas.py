#!/usr/bin/env python
# coding: utf-8

# # La biblioteca geopandas

# [GeoPandas](http://geopandas.org/) es un proyecto de software libre que extiende los tipos de datos de [Pandas](http://pandas.pydata.org/) para incorporar objetos geométricos (puntos, líneas, polígonos, etc). GeoPandas se apoya en las bibliotecas [Shapely](https://pypi.org/project/Shapely/) para realizar las operaciones geométricas, [Fiona](https://github.com/Toblerity/Fiona) para acceder a los datos (ej. en archivos) y [Descartes](https://bitbucket.org/sgillies/descartes/src/default/) y [Matplotlib](https://matplotlib.org/) para graficación.
# 
# El objetivo de GeoPandas es facilitar el trabajo con datos geoespaciales en el lenguaje Python, lo que se logra a través de la implementación de nuevas estructuras. Las dos estructuras principales de GeoPandas son:
# 
# - [GeoSeries](http://geopandas.org/data_structures.html#geoseries): es un vector en el que cada elemento es un conjunto de una o varias geometrías correspondientes a una observación. Por ejemplo, el polígono (o multipolígono) que representa una provincia.
# - [GeoDataFrame](http://geopandas.org/data_structures.html#geodataframe): es una estructura tabular (i.e. con filas y columnas) de datos geométricos y no geométricos (ej. textos, números). El conjunto de geometrías se implementa a través de GeoSeries.

# ## Instalación

# ### En una estación de trabajo

# geopandas puede instalarse tanto mediante [Conda](https://conda.io/) como mediante [pip](https://pypi.org/project/pip/).
# 
# ```shell
# # Instalación mediante Conda
# conda install geopandas
# 
# # Instalación mediante pip
# pip install geopandas
# ```

# ### En Google Colab

# ```shell
# # Instalación de bibliotecas de GDAL para Python
# !apt install gdal-bin python-gdal python3-gdal
# 
# # Instalación de r-tree
# !apt install python3-rtree
# 
# # Instalación de GeoPandas
# !pip install git+git://github.com/geopandas/geopandas.git
# 
# # Instalación de Descartes
# !pip install descartes
# ```

# ## Carga

# In[1]:


# Carga de bibliotecas
import math

import pandas as pd
import geopandas as gpd

import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster

import matplotlib
import matplotlib.pyplot as plt


# In[2]:


# Versión de geopandas
gpd.__version__


# In[3]:


# Versión de folium
folium.__version__


# ## Estructuras de datos
# Las dos principales estructuras de datos de geopandas son geoseries y geodataframes.

# ## Operaciones básicas

# ### read_file() - carga de datos

# In[4]:


# Lectura de datos de países
paises = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

paises


# ### info() - información general sobre un conjunto de datos

# In[5]:


paises.info()


# ### head(), tail(), sample() - despliegue de filas de un conjunto de datos

# In[6]:


# Muestra de 10 filas
paises.head(10)


# ### Selección de columnas

# In[7]:


paises[["name", "pop_est"]]


# ### Selección de filas

# In[8]:


# Países con población estimada mayor o igual a mil millones
paises[paises["pop_est"] >= 1000000000]


# ### Selección de filas y columnas en la misma expresión

# In[9]:


paises.loc[paises["pop_est"] >= 1000000000, ["name", "pop_est"]]


# ### plot() - mapeo

# In[10]:


# Mapa de coropletas
paises.plot(column = "pop_est", figsize=(15,15))


# ## Operaciones de análisis

# ### Mapeo básico

# In[11]:


# Carga de datos de distritos de Costa Rica

# Desde un shapefile local descomprimido
# distritos = gpd.read_file("datos/division-territorial/LIMITE_POLITICO_ADMINISTRATIVO_region.shp")

# Desde un shapefile local comprimido
# distritos = gpd.read_file("zip://./datos/division-territorial/limite_politico_administrativo_region.zip")

# Desde un shapefile remoto comprimido
# distritos = gpd.read_file("zip://https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/division-territorial/limite_politico_administrativo_region.zip")

# Desde un GeoJSON remoto
distritos = gpd.read_file("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/division-territorial/LIMITE_POLITICO_ADMINISTRATIVO_region.geojson")


# Mapeo
distritos.plot(figsize=(15, 15))


# In[12]:


# Carga de datos de la red de caminos de Costa Rica

# Desde un GeoJSON remoto
caminos = gpd.read_file("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/red-caminos/redcamino2008crtm05.geojson")

# Mapeo
caminos.plot(figsize=(15,15))


# In[13]:


# Mapeo de múltiples capas

ax = distritos.plot(edgecolor='black', facecolor='none', figsize=(15, 15))
caminos.plot(ax=ax, color='blue')


# ### Mapeo con folium

# #### Opciones básicas de configuración

# In[14]:


# Creación de un mapa con un centro (x, y)
m = folium.Map(location=[10, -84])

# Despliegue del mapa en el notebook
m


# In[15]:


# Especificación del ancho y del largo (en pixeles) del mapa
m = folium.Map(
    location=[10, -84], 
    width=650, height=400)

m


# In[16]:


# Especificación del nivel inicial de acercamiento (zoom)
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7)

m


# #### Manejo de capas base

# Por defecto, Folium utiliza OpenStreetMap como mapa base. Pueden elegirse otros mapas base mediante el parámetro tiles, el cual tiene un conjunto de valores predeterminados:
# 
#     - “OpenStreetMap”
#     - “Mapbox Bright”
#     - “Mapbox Control Room”
#     - “Stamen” ("Terrain", "Toner" y "Watercolor")
#     - “Cloudmade” (Requiere una llave del API)
#     - “Mapbox” (Requiere una llave del API)
#     - “CartoDB” ("positron" y "dark_matter")

# In[17]:


# Mapa de Stamen Terrain
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=5, 
    tiles='Stamen Terrain')
m


# In[18]:


# Mapa de Stamen Toner
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='Stamen Toner')

m


# In[19]:


# Mapa de Stamen Watercolor
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='Stamen Watercolor')

m


# In[20]:


# Mapa de CartoDB positron
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='CartoDB positron')

m


# In[21]:


# Mapa de CartoDB dark_matter
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='CartoDB dark_matter')

m


# El siguiente es un ejemplo que utiliza como mapa base el mapa "World Imagery" de ESRI. Pueden verse más ejemplos de mapas de ESRI en https://ocefpaf.github.io/python4oceanographers/blog/2015/03/23/wms_layers/.

# In[22]:


# Mapa "World Imagery "de ESRI
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/MapServer/tile/{z}/{y}/{x}', 
    attr='ESRI World Imagery')

m


# Registros de presencia de especies en la Infraestructura Mundial de Información en Biodiversidad (GBIF). Pueden verse más ejemplos de uso de este tipo de información en la documentación del API de mapas de GBIF.

# In[23]:


# Registros de presencia de especies en GBIF
m = folium.Map(
    location=[0, 0],
    width=650, height=400,
    zoom_start=1,
    tiles='https://api.gbif.org/v2/map/occurrence/density/{z}/{x}/{y}@1x.png?style=purpleYellow.point',
    attr='GBIF')

m


# #### Controles del mapa

# In[24]:


# Control de escala
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    control_scale=True)

m


# In[25]:


# Mapa con múltiples capas base

# Creación de un mapa
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    control_scale=True)

# Se añaden capas base adicionales
folium.TileLayer(
    tiles='CartoDB positron', 
    name='CartoDB positron').add_to(m)

folium.TileLayer(
    tiles='Stamen Terrain', 
    name='Stamen Terrain').add_to(m)


# ESRI NatGeo World Map
folium.TileLayer(
    tiles='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/MapServer/tile/{z}/{y}/{x}',
    name='NatGeo World Map',
    attr='ESRI NatGeo World Map').add_to(m)

# Densidad de registros de presencia de especies
folium.TileLayer(
    tiles='https://api.gbif.org/v2/map/occurrence/density/{z}/{x}/{y}@1x.png?&bin=hex&hexPerTile=28&style=classic.poly',
    name='Densidad de registros de presencia de especies',
    attr='GBIF').add_to(m)

# Se añade un control de capas
folium.LayerControl().add_to(m)

m


# #### Grabación del mapa en el disco

# In[26]:


# Grabación de mapa
# m.save("/home/mfvargas/mapa.html")


# #### Mapas con múltiples capas

# In[27]:


# Mapa con capa base y capa vectorial

# Creación del mapa
m = folium.Map(location=[10, -84], tiles='CartoDB positron', zoom_start=7)

# Se añaden al mapa las capas GeoJson
folium.GeoJson(data="https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/red-caminos/redcamino2008wgs84.geojson", name='Cantones').add_to(m)

# Control de capas
folium.LayerControl().add_to(m)

# Despliegue del mapa
m


# #### Mapeo de puntos de un archivo CSV

# In[28]:


# Lectura del archivo
felidae = pd.read_csv("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/gbif/felidae.csv", sep="\t")

felidae.head()


# In[29]:


# Creación del mapa
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Adición de marcadores
for idx, row in felidae.iterrows():
    Marker([row['decimalLatitude'], row['decimalLongitude']], popup=row['species']).add_to(m)

# Despliegue del mapa
m


# **Ejercicio:** incluya en la ventana emergente ("popup") de los puntos, la información relacionda con la localidad y la fecha.

# #### Mapas de puntos agrupados ("cluster maps")

# In[30]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Adición de puntos agrupados
mc = MarkerCluster()
for idx, row in felidae.iterrows():
    if not math.isnan(row['decimalLongitude']) and not math.isnan(row['decimalLatitude']):
        mc.add_child(Marker([row['decimalLatitude'], row['decimalLongitude']], popup=row['species']))
m.add_child(mc)

# Despliegue del mapa
m


# #### Mapas de burbuja ("bubble maps")

# In[31]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Adición de las "burbujas"
for i in range(0,len(felidae)):
    Circle(
        location=[felidae.iloc[i]['decimalLatitude'], felidae.iloc[i]['decimalLongitude']],
        radius=1000,
        color="black", 
        popup=row['species']).add_to(m)

# Despliegue del mapa
m


# El tamaño y el color de los puntos puede utilizarse para diferenciar algún atributo de los datos.

# In[32]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

def color_especie(especie):
    if especie == "Panthera onca":
        return 'orange'
    else:
        return 'black'

# Adición de las "burbujas"
for i in range(0,len(felidae)):
    Circle(
        location=[felidae.iloc[i]['decimalLatitude'], felidae.iloc[i]['decimalLongitude']],
        radius=1000,
        color=color_especie(felidae.iloc[i]['species']),
        popup=felidae.iloc[i]['species']).add_to(m)

# Despliegue del mapa
m


# **Ejercicio:** Modifique la función color_especie() para que retorne un color diferente por cada especie de felino.

# #### Mapas de calor ("heatmaps")

# In[33]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Mapa de color
HeatMap(data=felidae[['decimalLatitude', 'decimalLongitude']], radius=10).add_to(m)

# Despliegue del mapa
m


# #### Mapas de coropletas ("choropleth maps")

# In[ ]:




