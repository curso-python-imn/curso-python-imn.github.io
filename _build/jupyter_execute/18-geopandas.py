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
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


# Versión de geopandas
gpd.__version__


# ## Ejemplos de uso

# In[3]:


# Lectura de datos de países
paises = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

paises


# In[4]:


# Muestra de 10 filas
paises.head(10)


# In[5]:


# Mapa de coropletas
paises.plot(column = "pop_est")


# In[ ]:




