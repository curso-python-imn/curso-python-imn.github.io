#!/usr/bin/env python
# coding: utf-8

# # Python - excepciones

# Las [excepciones](https://docs.python.org/3/reference/executionmodel.html#exceptions) son un mecanismo que provee Python para manejar errores o situaciones inesperadas que se producen durante la ejecución de los programas. Mediante este mecanismo, el curso de ejecución del programa se interrumpe cuando ocurre un error y una excepción es "levantada" (_raised_). El control pasa entonces a otro bloque de instrucciones, el cual se encarga de manejar el error.

# ## Las sentencias try y except

# Las sentencias [try](https://docs.python.org/3/reference/compound_stmts.html#try) y [except](https://docs.python.org/3/reference/compound_stmts.html#except) son las que implementan el manejo de excepciones en Python. En el bloque **_try_** se coloca el código que puede ocasionar que se levante la excepción y en el bloque **_except_** se ubica el código que maneja la excepción.
# 
# La estructura básica es la siguiente:
# 
# ```python
# try:
#     <bloque de sentencias que puede generar un error>
# except:
#     <bloque de sentencias que maneja el error>
# ``` 
# 
# Por ejemplo, un llamado a la función **_float()_** puede ocasionar un error si la hilera de entrada no corresponde a un número entero.

# In[1]:


x = float("8,5")


# In[ ]:


try:
    x = float("8,5")
except:
    print("Por favor utilice un número")


# El siguiente ejemplo maneja el mismo error, que puede generarse por una entrada errónea por parte del usuario.

# In[ ]:


fahr_hilera = input('Ingrese la temperatura en grados Fahrenheit: ')
try:
    fahr = float(fahr_hilera)
    celsius = (fahr - 32.0) * 5.0 / 9.0
    print("El equivalente el grados Celsius es: ", celsius)
except:
    print('Por favor ingrese un número.')


# ## Ejercicio

# Reescriba el programa que calcula el IMC y maneje las excepciones que puedan producirse.
