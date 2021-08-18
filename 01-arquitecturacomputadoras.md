# Arquitectura de computadoras

En este capítulo, se describen algunos conceptos fundamentales sobre computación, incluyendo la arquitectura de von Neumann, el lenguaje máquina y los lenguajes de programación.

## Computadoras y programas

Una computadora es una **máquina** que ejecuta automáticamente **secuencias de cálculos y operaciones lógicas**, llamadas **comandos** o **instrucciones**. Estas secuencias son denominadas **programas**. En las computadoras modernas, es posible cambiar los programas que ejecutan sin necesidad de alterar sus componentes físicos. 

Los programas reciben un conjunto de datos de **entrada**, que **procesan** mediante los comandos, para enviar los resultados a los dispositivos de **salida**. Este [modelo entrada-procesamiento-salida](https://en.wikipedia.org/wiki/IPO_model) es ampliamente utilizado para esquematizar la estructura de un programa y se ilustra en la {numref}`figura-entrada-procesamiento-salida`.

```{figure} img/entrada-procesamiento-salida.png
:name: figura-entrada-procesamiento-salida

Modelo entrada - procesamiento - salida
```

Por ejemplo, el siguiente programa, implementado en el leguaje de programación [Python](https://www.python.org/), recibe como entrada una lista de números, la recorre y retorna como salida el número con el valor máximo.

```python
# Entrada
lista = [29.6, -36.81, 31.85, 25.71, 90.2, 0.4]
print("Lista de entrada: ", lista)

# Procesamiento
if (len(lista) == 0):
    print("La lista está vacía")
else:
    max = lista[0]
    i = 0
    while (i < len(lista)):
        if (lista[i] > max):
            max = lista[i]
        i = i + 1
        
    # Salida
    print("Valor máximo de la lista:", max)  
```

Las computadoras modernas están construídas con base en [circuitos integrados (CI)](https://es.wikipedia.org/wiki/Circuito_integrado), también llamados *chips* o *microchips*, como el que se muestra en la {numref}`figura-ci`. Los CI procesan [información digital](https://es.wikipedia.org/wiki/Se%C3%B1al_digital) (que usa valores discretos), la cual generalmente es binaria (i.e. de dos valores). Los CI de una computadora procesan dos estados correspondientes a **dos niveles de tensión eléctrica: alto y bajo**. Estos estados se representan con **0 y 1**. Esto facilita la aplicación de la [lógica binaria](https://es.wikipedia.org/wiki/L%C3%B3gica_binaria) y de la [aritmética binaria](https://es.wikipedia.org/wiki/Sistema_binario).

```{figure} img/chip-intel.jpg
:name: figura-ci

Circuito integrado. Imagen de <a href="https://unsplash.com/@slavudin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Slejven Djurakovic</a> disponible en <a href="https://unsplash.com/s/photos/chip?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>.

```

Para conocer el proceso que condujo al desarrollo de las computadoras modernas, puede consultar [GF0604 Procesamiento de datos geográficos 2021-I](https://gf0604-procesamientodatosgeograficos.github.io/2021i-leccion-02-arquitectura-computadoras-lenguajes-programacion/).


## Arquitectura de von Neumann

En 1945, el matemático húngaro-estadounidense [John von Neumann](https://es.wikipedia.org/wiki/John_von_Neumann) propuso un concepto conocido como **programa almacenado**, de acuerdo con el cual los datos y los programas de una computadora se almacenan en una estructura llamada **memoria**, separada del hardware que ejecuta las instrucciones. Previamente a este modelo, no era posible modificar la funcionalidad de una máquina sin alterar sus componentes físicos.

Este concepto permite que las computadoras sean más fáciles de reprogramar y es conocido actualmente como [arquitectura de von Neumann](https://es.wikipedia.org/wiki/Arquitectura_de_Von_Neumann). Se ilustra en la {numref}`figura-arquitectura-vonneumann`.

```{figure} img/arquitectura-vonneumann.jpg
:name: figura-arquitectura-vonneumann

Diagrama de la arquitectura de von Neumann. Imagen de <a href="https://commons.wikimedia.org/wiki/File:Arquitecturaneumann.jpg">David Strigoi en Wikimedia</a>.
```

Seguidamente, se describen los principales componentes de esta arquitectura:

**Memoria principal**  
Almacena las instrucciones de los programas y los datos que utilizan. Es común denominarla como RAM (*Random Access Memory*, Memoria de Acceso Aleatorio), lo que significa que toma el mismo tiempo acceder a cualquier posición de la memoria. Cada posición de memoria tiene una dirección a la que se hace referencia cuando se desea leer o escribir.

**Unidad central de procesamiento**  
La Unidad Central de Procesamiento o CPU (*Central Processing Unit*) se encarga de ejecutar las instrucciones de los programas. Está compuesta por dos partes:

* La Unidad de Control: determina cuál es la siguiente instrucción a ejecutar. Contiene memorias temporales de alta velocidad y poca capacidad llamadas registros, para almacenar los operandos y el resultado de las instrucciones.
* La Unidad de Aritmética y Lógica o ALU (*Arithmetic and Logic Unit*): ejecuta las operaciones aritméticas y lógicas.

**Sistemas de entrada y salida**  
Permiten que la computadora interactúe con el usuario y, en general, con el mundo exterior. Algunos ejemplos son el teclado y el ratón, como sistemas de entrada, y la pantalla y la impresora, como sistemas de salida.

## Código binario

Los CI de las computadoras usan voltajes bajos y altos para representar dos posibles valores de información: 0 y 1. Este es un sistema binario y cada dígito binario (0 o 1) se denomina *bit* (*binary digit*).

Los bits se agrupan (por ejemplo, en [bytes = 8 bits](https://es.wikipedia.org/wiki/Byte)) para representar elementos de información más complejos, como números más grandes o carácteres de texto. Por ejemplo:
  - El número decimal ```14``` se representa en binario como ```1110```:  
```1110``` = ```2^3*1 + 2^2*1 + 2^1*1 + 2^0*0``` = ```8 + 4 + 2 + 0``` = ```14```
  - La palabra ```bit``` se representa en [código ASCII](https://es.wikipedia.org/wiki/ASCII) como:  
```01100010 01101001 01110100``` = ```bit```

## Lenguaje máquina

El [lenguaje máquina](https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina) es un conjunto de instrucciones binarias interpretables por un CPU. Las instrucciones representan acciones a ser ejecutadas por la computadora. Cada CPU tiene su propio lenguaje máquina. Un programa consiste de una secuencia de instrucciones en lenguaje máquina.

Por ejemplo, la instrucción que se muestra en la {numref}`figura-suma-binaria` suma los contenidos de los registros 1 y 2 y almacena el resultado en el registro 6 de un CPU:

```{figure} img/suma-binaria.png
:name: figura-suma-binaria

Instrucción de suma en lenguaje máquina. Fuente <a href="https://en.wikipedia.org/wiki/Machine_code">Machine code - Wikipedia</a>.
```

## Lenguajes de programación

Debido a que programar una computadora en lenguaje máquina es excesivamente lento y complicado, en la década de 1950 comenzaron a crearse lenguajes de programación que, en lugar de unos y ceros, consisten de instrucciones formadas por palabras, usualmente en idioma inglés. Por ejemplo, el siguiente programa en lenguaje [C](https://www.iso.org/standard/74528.html) imprime la hilera de texto ["hello, world\n"](http://helloworldcollection.de/):

```c
main() {
    printf("hello, world\n");
}
```

Existe una gran [variedad de lenguajes de programación](https://en.wikipedia.org/wiki/List_of_programming_languages) que han sido creados con diversos fines: científicos, comerciales, educacionales, etc.
