#!/usr/bin/env python
# coding: utf-8

# # Python - colecciones

# ### La clase str

# Como ya se ha explicado, la clase [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) se utiliza para representar datos textuales en Python. Esta clase proporciona un conjunto de [métodos](https://docs.python.org/3/library/stdtypes.html#string-methods), de los que se presentan algunos ejemplos a continuación.

# In[1]:


# str.capitalize(): retorna una copia de 'str' con el primer carácter en mayúscula y el resto en minúscula.
'hola'.capitalize()


# In[2]:


# str.lower(): retorna una copia de 'str' con todos los caracteres en minúscula
'HOLA'.lower()


# In[3]:


# str.count(sub[, start[, end]]): retorna el número de hileras no traslapadas de la subhilera 'sub' 
# en el rango [start, end], el cual es opcional, de 'str'.

cita_socrates = 'Yo solo sé, que no sé nada'
cita_socrates.count('sé') # se cuentan todas las ocurrencias de 'sé'


# In[4]:


cita_socrates.count('sé', 0, 10) # se cuentan solo las ocurrencias ubicadas en el rango [0, 10]


# In[5]:


# str.find(sub[, start[, end]]): retorna el índice menor en donde se encuentra 'sub'
# en el rango [start, end] de 'str'

'Yo solo sé, que no sé nada'.find('solo')


# In[6]:


# str.replace(old, new[, count]): retorna una copia de 'str' con todas las ocurrencias
# de la subhilera 'old' reemplazadas por 'new'. 
# Si 'count' es especificado, solo se reemplazan las primeras 'count' ocurrencias de 'old'
cita_socrates.replace("solo", "solamente")


# **Formateo de hileras**
# 
# Se implementa a través del método [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format). Pueden verse varios ejemplos en [https://pyformat.info/](https://pyformat.info/).

# In[7]:


# Formateo de números enteros
'La suma de 3 + 4 es {} y la resta de 10 - 6 es {}'.format(7, 4)


# In[8]:


# Formateo de un número en punto flotante (6 caracteres, 4 después del punto decimal)
'La relación entre la longitud de una circunferencia y su diámetro es {:6.4f}'.format(3.141592653589793)


# In[9]:


# Formateo de fecha y hora
from datetime import datetime
'{:%d/%m/%Y %H:%M}'.format(datetime(2001, 2, 3, 4, 5))


# ### La clase list

# La clase [list](https://docs.python.org/3/library/stdtypes.html#lists) implementa secuencias mutables (i.e. modificables) de objetos que se especifican como **ítems separados por comas y encerrados entre paréntesis cuadrados**.
# 
# Se presentan a continuación algunos ejemplos de operaciones y métodos de la clase _list_, los cuales son comunes a todas las clases de [secuencias mutables](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types):

# In[10]:


lista = [10, 20, 30, 40, 50]


# In[11]:


# Reemplazo de un ítem con base en su posición
lista[2] = 300
lista


# In[12]:


# Borrado de un ítem con base en su posición
del lista[4]
lista


# In[13]:


# list.append(x): agrega 'x' al final de 'list'
lista.append(50)
lista


# In[14]:


# list.insert(i, x): inserta 'x' en al posición 'i'
lista.insert(4, 45)
lista


# ### La clase dict

# La clase [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) implementa un conjunto de pares ordenados de la forma _atributo_:_valor_. Por ejemplo:

# In[15]:


persona = {"cedula":"408730281", "nombre":"Juan", "apellido":"Pérez"}


# Ejemplos de operaciones y métodos de la clase dict:

# In[16]:


# Retorno de valor correspondiente a una llave
persona["cedula"]


# In[17]:


# Asignación de un valor a una llave
persona["nombre"] = "María"
persona


# In[18]:


# Verificación de si una llave existe
"apellido" in persona


# In[19]:


# dict.items(): retorna los ítems (pares (llave, valor)) de 'dict'
persona.items()


# In[20]:


# dict.keys(): retorna las llaves de 'dict'
persona.keys()


# In[21]:


# dict.values(): retorna los valores de 'dict'
persona.values()


# In[22]:


# dict.get(key[, default]): retorna el valor de la llave 'key' en 'dict'
persona.get("apellido")

