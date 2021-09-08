#!/usr/bin/env python
# coding: utf-8

# # Python - ciclos

# Los ciclos son bloques de instrucciones que se ejecutan varias veces. Para manejar ciclos, Python provee dos mecanismos: la sentencia **_while_** y la sentencia **_for_**.

# ## La sentencia while

# La setencia [while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) se utiliza para ejecutar repetidamente un bloque de instrucciones mientras que una condición sea verdadera. Su estructura básica es:
# 
# ```python
# while <condicion>:
#     <bloque de sentencias>
# ``` 
# 
# Típicamente, en el bloque hay instrucciones que provocan que la condición se vuelva falsa eventualmente y el ciclo termine. De lo contrario, se producirá un **ciclo infinito**. Nótese que si la condición ya es falsa cuando el flujo del programa llega al **_while_**, el bloque no se ejecutará nunca.

# ### Ejemplos

# In[1]:


# Contador de números en orden ascendente
n = 1
while n <= 5:
    print(n)
    n = n + 1


# In[2]:


# Contador de números en orden descendente
n = 5
while n >= 1:
    print(n)
    n = n - 1


# In[3]:


# Recorrido de una hilera
texto = "Lorem ipsum"
n = 0
while n < len(texto) :
    print(texto[n])
    n = n + 1


# In[4]:


# Validación de entrada de datos
numero = -1
while not(numero >= 5 and numero <= 10) :
    numero = float(input("\nPor favor ingrese un número entre 5 y 10: "))
    if not(numero >= 5 and numero <= 10) :
        print("El número no está entre 5 y 10, por favor inténtelo de nuevo...")
print("¡Gracias!")


# ## La sentencia for

# La sentencia [for](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) se utiliza para iterar sobre los elementos de estructuras de datos como secuencias (ej. hilera, lista, tupla). Su sintaxis puede resumirse de la siguiente manera:
# 
# ```python
# for <variable_iteracion> in <secuencia>:
#     <bloque de sentencias>
# ``` 
# 
# La variable de iteración es una variable que asume el valor del elemento que se procesa en cada iteración.

# ### Ejemplos

# In[ ]:


# Recorrido de una lista
alumnos = ['Juan', 'María', 'Pedro']
for alumno in alumnos:
    print("¡Buenos días " + alumno + "!")


# In[ ]:


# Recorrido de un rango de números
# La función range(a, b) crea una secuencia de números entre a y b-1.
for numero in range(1, 11):
    print(numero)


# In[ ]:


# Cálculo de la cantidad de elementos 
lista = [3, 41, 12, 9, 74, 15]
contador = 0
print("Lista: ", lista)
for item in lista :
    contador += 1 # esto es lo mismo que: contador = contador + 1
print("Cantidad de elementos:", contador)


# In[ ]:


# Suma de los elementos de una lista
lista = [3, 41, 12, 9, 74, 15]
suma = 0
print("Lista: ", lista)
for item in lista :
    suma += item
print("Suma de los elementos:", suma)


# ## La sentencia break

# La sentencia [break](https://docs.python.org/3/reference/simple_stmts.html#break) finaliza un ciclo y pasa el flujo del programa a la instrucción que sigue al bloque del while o del for.

# In[ ]:


# Busca el primer número de una lista que sea mayor que 20 y sale del ciclo una vez que lo ha encontrado
lista = [3, 41, 12, 9, 74, 15]
print("Lista: ", lista)
for item in lista :
    if item > 20 :
        print("Primer número mayor que 20: ", item)
        break


# ## La sentencia continue

# La sentencia [continue](https://docs.python.org/3/reference/simple_stmts.html#continue) interrumpe la iteración actual de un ciclo y continúa con la siguiente. No sale completamente del ciclo, como la sentencia break.

# In[ ]:


# Imprime el doble de cada uno de los números mayores que 20 que hay en una lista. 
# Si el número de la iteración es menor o igual que 20, utiliza la sentencia continue para "saltarse" esa iteración.

lista = [3, 41, 12, 9, 74, 15]
print("Lista: ", lista)
for item in lista :
    if item <= 20:
        continue
    print(item * 2)


# ## Ejercicios

# 1. Escriba un programa que calcule el promedio de los números de una lista.
# 2. Escriba un programa que calcule la desviación estándar de los números de una lista.
# 
# (Maneje la lista en una variable)
