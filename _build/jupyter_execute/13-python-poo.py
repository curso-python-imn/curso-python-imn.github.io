#!/usr/bin/env python
# coding: utf-8

# # Python - programación orientada a objetos

# La [Programación Orientada a Objetos (POO)](https://en.wikipedia.org/wiki/Object-oriented_programming) es un [paradigma de programación](https://en.wikipedia.org/wiki/Programming_paradigm) basado en el concepto de **objeto**. En el contexto de la POO, los objetos son entidades que poseen:
# - **Estado**: implementado con un conjunto de variables llamadas **propiedades**.
# - **Comportamiento**: implementado con un conjunto de funciones llamadas **métodos**.
# 
# Los objetos se agrupan en [clases](https://docs.python.org/3/tutorial/classes.html). Todos los objetos de una clase contienen los mismos métodos y propiedades. Una clase puede verse como una plantilla o “machote” a partir de la cual se crean objetos. A un objeto creado a partir de una clase se le llama también una **instancia** de esa clase.

# In[1]:


# Definición de la clase cuentaBancaria
class cuentaBancaria:
    # Propiedades
    propietario = ""
    balance = 0
    
    # Métodos
    # Constructor de la clase: crea nuevas instancias e inicializa las propiedades
    def __init__(self, propietario, balance):
        self.propietario = propietario
        self.balance = balance
    
    # Método para realizar depósitos
    def depositar(self, monto):
        self.balance = self.balance + monto

    # Método para realizar retiros
    def retirar(self, monto):
        self.balance = self.balance - monto

    # Método para imprimir información
    def imprimirInformacion(self):
        print("Propietario: " + self.propietario + ", Balance: " + str(self.balance))       


# Una vez definida una clase, pueden declararse objetos o instancias de esta. Las instancias pueden invocar métodos de la clase mediante la notación:
# 
# ```python
#     <instancia>.<método>
# ``` 
# 
# A continuación, se presentan algunos ejemplos de instancias de la clase _cuentaBancaria_ y de llamados a sus métodos.

# In[2]:


# Instancia cuenta01
cuenta01 = cuentaBancaria("Juan Pérez", 1000)
cuenta01.depositar(5000)
cuenta01.imprimirInformacion()


# In[3]:


# Instancia cuenta02
cuenta02 = cuentaBancaria("María Pérez", 10000)
cuenta02.depositar(15000)
cuenta02.retirar(24000)
cuenta02.imprimirInformacion()


# ## Objetos y clases predefinidas de Python

# Todos los datos de un programa en Python se representan mediante objetos o por relaciones entre objetos. Los tipos de datos corresponden a las clases de los objetos.

# In[4]:


# Clase int
print(type(234))


# In[5]:


# Clase float
print(type(10.3))


# In[6]:


# Clase bool
print(type(True))


# In[7]:


# Clase list
print(type([True, 23, 20.6, (1, 2, 3)]))


# El que un dato sea un objeto, implica que además de su valor tiene un conjunto de operaciones asociadas (métodos) que se aplican mediante operadores (ej. +, -, *, %) o funciones (ej. len(), type()). Tanto los operadores como las funciones pueden aplicarse en varias clases. Por ejemplo, el operador + se usa para _int_, _float_, _str_, _list_ y otras clases; _len()_ se usa también en varios tipos de datos.
