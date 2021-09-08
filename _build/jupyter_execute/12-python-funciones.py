#!/usr/bin/env python
# coding: utf-8

# # Python - funciones

# Las [funciones](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) son conjuntos de sentencias que **tienen un nombre y realizan una tarea específica** como, por ejemplo, un cálculo matemático o un procesamiento de texto. Por lo general, una función recibe datos de entrada, llamados **argumentos**, y **retorna un valor**.
# 
# 
# El uso de funciones tiene múltiples ventajas, entre las que pueden mencionarse:
# 
# - Mejoran la legibilidad de los programas: mediante el uso de nombres significativos para las secciones de código que realizan una tarea.
# - Evitan la duplicidad de código fuente: una función se define una vez y luego pueden ser invocada muchas veces en un programa.
# - Facilitan el mantenimiento de los programas: al realizar las modificaciones en el código de una función, se evita la necesidad de realizarlas en múltiples secciones de un programa.
# - Facilitan la reutilización de código: mediante mecanismos como módulos de funciones (archivos con colecciones de funciones).

# ## Funciones predefinidas

# Python tiene una lista de [funciones predefinidas](https://docs.python.org/3/library/functions.html), de las cuales algunas se han utilizado ya en este curso:

# In[1]:


# type(): tipo de datos de una expresión
type(20)


# In[2]:


# int(): convierte una expresión a un número de tipo entero (int)
int("100")


# In[3]:


# len(): retorna la cantidad de elementos (items) de una hilera, lista 
# u otros tipos de secuencias y de colecciones.
lista_provincias = ["Limón", "Guanacaste", "Puntarenas", "Heredia", "Alajuela", "Cartago", "San José"]
len(lista_provincias)


# In[4]:


# pow(): eleva un número a una potencia
pow(5, 2)


# Estas funciones predefinidas pueden invocarse en cualquier parte de un programa en Python, con solo escribir su nombre y argumentos.

# ## Funciones definidas en módulos de la biblioteca estándar

# La [biblioteca estándar de Python](https://docs.python.org/3/library/) es el conjunto de módulos que se incluye junto con cada distribución de Python, sin necesidad de instalarlos separadamente. Estos módulos proporcionan un conjunto de funciones más especializadas en áreas como matemáticas, multimedios, redes y otras. Para utilizar estas funciones, primero debe importarse el módulo del que forman parte mediante la sentencia [import](https://docs.python.org/3/reference/simple_stmts.html#import). Por ejemplo:

# In[5]:


import math


# La instrucción anterior brinda acceso a las funciones del módulo [math](https://docs.python.org/3/library/math.html), que contiene un conjunto de funciones matemáticas. Por ejemplo:

# In[6]:


# math.factorial(): retorna el factorial de un número
math.factorial(4)


# In[7]:


# math.sqrt(): retorna la raíz cuadrada de un número
math.sqrt(9)


# Nótese que para invocar a estas funciones, debe escribirse antes el nombre del módulo y un punto.

# ## Paquetes externos

# No están incluídos en la biblioteca estándar de Python y deben instalarse de acuerdo con el procedimiento definido por sus autores, como por ejemplo con los programas administradores de paquetes [pip](https://pypi.org/project/pip/) y [Conda](https://conda.io/).
# 
# Muchos de estos paquetes se distribuyen a través de repositorios como el [Python Package Index (PyPI)](https://pypi.python.org/), que a la fecha alberga cerca de 260000 proyectos desarrollados por la comunidad de desarrolladores en Python.

# ## Sintaxis para la definición de nuevas funciones

# En Python, el programador puede definir nuevas funciones a través de la palabra reservada **def**, con la siguiente sintaxis:
# 
# ```python
# def <nombre_funcion>(<arg1>, <arg2>, ..., <argn>):
#     <bloque de sentencias>
#     return <valor_retorno>
# ``` 
# 
# - El nombre de la función es elegido por el usuario y sigue las mismas reglas y recomendaciones que en el caso de los nombres de las variables.
# - Los argumentos se especifican entre paréntesis y se separan entre paréntesis. Si la función no tiene argumentos, deben incluirse paréntesis vacíos.
# - La palabra reservada **return** especifica el valor de retorno de la función.

# ### Ejemplos

# In[8]:


# Definición de una función
def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32.0) * 5.0 / 9.0
    return grados_celsius

# Llamados a la función
print(fahrenheit_a_celsius(104))
print(fahrenheit_a_celsius(50))
print(fahrenheit_a_celsius(32))
print(fahrenheit_a_celsius(14))


# ## Ejercicios

# 1. Defina una función llamada celsius_a_fahrenheit() e inclúyala en el programa del ejemplo anterior. Realice algunos llamados de prueba a la nueva función.
