#!/usr/bin/env python
# coding: utf-8

# # Python - exploración y visualización de datos

# ## Sobre el Titanic
# 
# El [RMS Titanic](https://es.wikipedia.org/wiki/RMS_Titanic) fue un transatlántico británico que se hundió en 1912 durante su viaje inaugural entre Southampton y Nueva York. Fallecieron más de 1500 personas de las 2224 que viajaban en el barco.
# 
# El naufragio del Titanic conmocionó e indignó al mundo entero por el elevado número de víctimas mortales y por los errores cometidos en el accidente. Solamente portaba botes salvavidas para 1178 pasajeros, poco más de la mitad de los que iban a bordo en su viaje inaugural y un tercio de su capacidad total de 3547 personas. 
# 
# El Titanic es quizá el barco más famoso de la historia y su memoria se mantiene muy viva gracias a numerosos libros, canciones, películas, exposiciones y memoriales.

# ![El RMS Titanic](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/800px-RMS_Titanic_3.jpg)

# El RMS Titanic al salir de Southampton el 10 de abril de 1912. Imagen de dominio público disponible en [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:RMS_Titanic_3.jpg).

# ## Análisis de datos del Titanic

# Se proporcionan dos archivos CSV (valores separados por comas) con datos sobre los pasajeros del Titanic:
# 
# - [entrenamiento.csv](https://github.com/curso-python-imn/curso-python-imn.github.io/blob/main/datos/titanic/entrenamiento.csv): contiene datos detallados sobre un subconjunto de pasajeros (891 registros), incluyendo una columna que indica si cada uno sobrevivió o no al naufragio.
# - [evaluacion.csv](https://github.com/curso-python-imn/curso-python-imn.github.io/blob/main/datos/titanic/evaluacion.csv): contiene otro subconjunto (418 registros) con las mismas columnas del conjunto de datos de entrenamiento, excepto la que indica si el pasajero sobrevivió al naufragio.

# Para analizar los datos, se utilizarán las bibliotecas [numpy](https://numpy.org/) y [pandas](https://pandas.pydata.org/) de Python.

# In[1]:


import numpy as np # biblioteca para álgebra lineal
import pandas as pd # biblioteca para análisis de datos


# ### Visualización

# In[2]:


# Carga de los datos de un archivo en un data frame de pandas
datos_entrenamiento = pd.read_csv("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/titanic/entrenamiento.csv")

# Despliegue de los primeros registros
datos_entrenamiento.head()


# In[3]:


datos_evaluacion = pd.read_csv("https://raw.githubusercontent.com/curso-python-imn/curso-python-imn.github.io/main/datos/titanic/evaluacion.csv")


# ### Exploración

# #### Sexo

# In[4]:


mujeres_sobrevivientes = datos_entrenamiento.loc[datos_entrenamiento.Sex == 'female']["Survived"]
tasa_sobrevivencia_mujeres = sum(mujeres_sobrevivientes)/len(mujeres_sobrevivientes)

print("Porcentaje de mujeres que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_mujeres))


# In[5]:


hombres_sobrevivientes = datos_entrenamiento.loc[datos_entrenamiento.Sex == 'male']["Survived"]
tasa_sobrevivencia_hombres = sum(hombres_sobrevivientes)/len(hombres_sobrevivientes)

print("Porcentaje de hombres que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_hombres))


# #### Edad

# In[6]:


sobrevivientes_menores = datos_entrenamiento.loc[datos_entrenamiento.Age < 18]["Survived"]
tasa_sobrevivencia_menores = sum(sobrevivientes_menores)/len(sobrevivientes_menores)

print("Porcentaje de menores de edad que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_menores))


# In[7]:


sobrevivientes_mayores = datos_entrenamiento.loc[datos_entrenamiento.Age >= 18]["Survived"]
tasa_sobrevivencia_mayores = sum(sobrevivientes_mayores)/len(sobrevivientes_mayores)

print("Porcentaje de mayores de edad que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_mayores))


# #### Clase

# In[8]:


clase1_sobrevivientes = datos_entrenamiento.loc[datos_entrenamiento.Pclass == 1]["Survived"]
tasa_sobrevivencia_clase1 = sum(clase1_sobrevivientes)/len(clase1_sobrevivientes)

print("Porcentaje de pasajeros de primera clase que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_clase1))


# In[9]:


clase2_sobrevivientes = datos_entrenamiento.loc[datos_entrenamiento.Pclass == 2]["Survived"]
tasa_sobrevivencia_clase2 = sum(clase2_sobrevivientes)/len(clase2_sobrevivientes)

print("Porcentaje de pasajeros de segunda clase que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_clase2))


# In[10]:


clase3_sobrevivientes = datos_entrenamiento.loc[datos_entrenamiento.Pclass == 3]["Survived"]
tasa_sobrevivencia_clase3 = sum(clase1_sobrevivientes)/len(clase3_sobrevivientes)

print("Porcentaje de pasajeros de tercera clase que sobrevivieron: {:3.2f}".format(tasa_sobrevivencia_clase3))


# ### Modelado

# In[11]:


from sklearn.ensemble import RandomForestClassifier

y = datos_entrenamiento["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(datos_entrenamiento[features])
X_test = pd.get_dummies(datos_evaluacion[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': datos_evaluacion.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")


# In[ ]:




