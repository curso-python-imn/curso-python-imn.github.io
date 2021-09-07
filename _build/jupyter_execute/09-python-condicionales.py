#!/usr/bin/env python
# coding: utf-8

# # Python - condicionales

# Los condicionales son instrucciones que permiten evaluar condiciones (i.e. expresiones lógicas) y alterar el flujo del programa de acuerdo con su valor.

# ## La sentencia if

# En Python, los condicionales se implementan a través de la sentencia [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement). En su forma más básica, tiene la siguiente estructura:
# 
# ```python
# if <condición>:
#     <bloque de sentencias>
# ```
# 
# <condición> es una expresión lógica (que es verdadera o falsa). Si la condición es verdadera, se ejecutará el bloque de sentencias que está luego de los dos puntos (:). En Python, un bloque de instrucciones se identifica por la cantidad de espacios que lo tabulan.
# 
# Por ejemplo:

# In[1]:


print("Inicio del programa.")
print("Este programa indica si una persona es menor de edad.")
print("\n")

edad = 15
if edad < 18:
    print("- La persona es MENOR.")
    print("- No puede votar en las elecciones presidenciales.")
    print("- No puede tener licencia para conducir automóviles.")
    
print("\n")    
print("Fin del programa.")


# Después de ejecutar el bloque (si se cumple la condición), el programa continua ejecutando las instrucciones que están fuera del bloque, si es que las hay.

# ### La cláusula else

# Es una cláusula opcional que se utiliza para especificar un bloque alterno que se ejecuta si no se cumple la condición del if. Tiene la siguiente estructura:
# 
# ```python
# if <condición>:
#     <bloque de sentencias>
# else:
#     <bloque de sentencias>
# ```
# 
# Solamente puede usarse una cláusula else en cada sentencia if. Por ejemplo:

# In[2]:


print("Inicio del programa.")
print("Este programa indica si una persona es menor o adulta.")
print("\n")

edad = 22
if edad < 18:
    print("- La persona es MENOR.")
    print("- No puede votar en las elecciones presidenciales.")
    print("- No puede tener licencia para conducir automóviles.")    
else:
    print("- La persona es ADULTA.")
    print("- Puede votar en las elecciones presidenciales.")
    print("- Puede tener licencia para conducir automóviles.")
    
print("\n")    
print("Fin del programa.")


# ### La cláusula elif

# Es una cláusula opcional que permite especificar condiciones adicionales entre las cláusulas if y else. 
# 
# ```python
# if <condición>:
#     <bloque de sentencias>
# elif <condición>:
#     <bloque de sentencias>
# else:
#     <bloque de sentencias>
# ```    
# 
# Puede usarse cualquier cantidad de cláusulas elif. La cláusula elif puede utilizarse sin la clásula else y viceversa.
# 
# Ejemplo:

# In[3]:


print("Inicio del programa.")
print("Este programa indica si una persona es menor, adulta o adulta mayor.")
print("\n")

edad = 65
if edad < 18:
    print("- La persona es MENOR.")
    print("- No puede votar en las elecciones presidenciales.")
    print("- No puede tener licencia para conducir automóviles.")
elif (edad >= 18) and (edad < 65):
    print("- La persona es ADULTA.")
    print("- Puede votar en las elecciones presidenciales.")
    print("- Puede tener licencia para conducir automóviles.")    
else:
    print("- La persona es ADULTA MAYOR.")
    print("- Puede votar en las elecciones presidenciales.")
    print("- Puede tener licencia para conducir automóviles.")
    print("- Tiene acceso gratuito al servicio público de autobuses.")
    print("- Tiene prioridad en las filas de atención en bancos y otros servicios.")
    
print("\n")    
print("Fin del programa.")


# ## Acerca de los bloques en Python

# Los bloques son conjuntos de sentencias contiguas que están tabulados con la misma cantidad de espacios. La cantidad de espacios puede ser decidida por el programador, pero [se recomienda usar cuatro espacios](https://www.python.org/dev/peps/pep-0008/#indentation).
# 
# **NOTA:** deben utilizarse espacios y NO TABULADORES. Si se mezclan espacios y tabuladores, el programa puede comportarse de forma errónea.

# ## Ejercicios

# Escriba un programa que:
# * Le solicite al usuario su peso y su estatura.
# * Calcule su índice de masa corporal.
# * Indique el valor del índice y si este es considerado bajo (menor que 18.5), normal (entre 18.5 y 25) o alto (mayor o igual que 25).
# 
# Los detalles del cálculo del índice están en [https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator](https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator).
