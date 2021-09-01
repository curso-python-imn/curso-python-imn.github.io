#!/usr/bin/env python
# coding: utf-8

# # Python - expresiones

# En Python, una [expresión](https://docs.python.org/3/reference/expressions.html) es una combinación de:
# * [Literales](https://docs.python.org/3/reference/lexical_analysis.html#literals): valores constantes de números, hileras, listas, booleanos y otros tipos de datos.
# * Variables.
# * Los dos anteriores combinados mediante [operadores](https://docs.python.org/3/reference/lexical_analysis.html#operators) o funciones.
# 
# **Una expresión tiene un valor numérico, textual, booleano o de otro tipo**. En las secciones siguientes se brindan algunos ejemplos de expresiones.
# 
# **NOTA:** al escribir una expresión en la línea de comandos del interpretador de Python o en un _notebook_, esta retorna su valor. Sin embargo, esto no sucede en un programa. En este último caso, si se quiere visualizar el valor de una expresión, debe imprimirse con la función **print()**, por ejemplo.

# Para los ejemplos siguientes, se definen las variables:

# In[1]:


x = 20
y = 21.5
h = "Python"


# ## Expresiones aritméticas

# Se utilizan para realizar operaciones matemáticas con números enteros, complejos o de punto flotante.

# ### Operadores aritméticos
# 
# <table>
# 
# <tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
# 
# <tr><td>+</td><td>Suma</td><td>4 + 3 (= 7)</td></tr>
# <tr><td>-</td><td>Resta</td><td>10 - 5 (= 5)</td></tr>
# <tr><td>*</td><td>Multiplicación</td><td>3 * 4 (= 12)</td></tr>
# <tr><td>/</td><td>División</td><td>5 / 2 (= 2.5)</td></tr>
# <tr><td>//</td><td>División entera</td><td>5 // 2 (= 2)</td></tr>
# <tr><td>%</td><td>Módulo</td><td>5 % 2 (= 1)</td></tr>
# <tr><td>**</td><td>Exponenciación</td><td>2 ** 3 (= 8)</td></tr>
# </table>

# ### Ejemplos

# In[2]:


# Literal
0


# In[3]:


# Variable
x


# In[4]:


# Literal, variable, operador aritmético y función
34 + int(y)


# ## Expresiones booleanas

# Se les llama también expresiones lógicas. Tienen solamente dos posibles valores:
# * **True** (verdadero)
# * **False** (falso)
# 
# Son sumamente importantes en Python (y en otros lenguajes de programación) porque con base en expresiones boolenanas se construyen sentencias como condicionales y ciclos.

# ### Operadores booleanos

# <table>
# 
# <tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
# 
# <tr><td>and</td><td>Retorna <strong>True</strong> si ambos operandos son verdaderos y <strong>False</strong> en caso contrario</td><td>(1 < 2) and (4 > 3) [= True]</td></tr>
# <tr><td>or</td><td>Retorna <strong>True</strong> si al menos uno de los operados es verdadero y <strong>False</strong> en caso contrario</td><td>(10 > 20) or (40 < 30) [= False]</td></tr>
# <tr><td>not</td><td>Retorna <strong>True</strong> si el operando el falso  y <strong>False</strong> en caso contrario</td><td>not (4 > 2) [= False]</td></tr>
# </table>

# ### Operadores relacionales

# Con frecuencia, las expresiones boolenas incluyen operadores relacionales (de comparación).
# <table>
# 
# <tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
# 
# <tr><td>==</td><td>Igual</td><td>(3 + 1) == (2 ** 2)</td></tr>
# <tr><td>!=</td><td>Diferente</td><td>0 != 1</td></tr>
# <tr><td>></td><td>Mayor que</td><td>3 > 2</td></tr>
# <tr><td><</td><td>Menor que</td><td>2 < 3</td></tr>
# <tr><td>>=</td><td>Mayor o igual que</td><td>3 >= (2 + 1)</td></tr>
# <tr><td><=</td><td>Menor o igual que</td><td>2 <= 5</td></tr>
# 
# </table>

# ### Ejemplos

# In[5]:


# Literal
True


# In[6]:


# Literal y variable
x == 20


# In[7]:


# Literal, variable y operador
x > 100


# In[8]:


# Literales, variables, operador aritmético y operador relacional
(x + 45) > 10 


# In[9]:


# Literales, variables, operadores aritméticos, operadores relacionales y operadores lógicos
((x + 45) > 10) and ((y - 20) <= 0)


# ## Otras expresiones

# In[10]:


# Hileras
"Hola " + h


# In[11]:


# Listas
[1, 2, 3] + ["a", "b", "c"]


# In[12]:


# Conjuntos
{10, 20, 30, 40, 50} - {30, 50}

