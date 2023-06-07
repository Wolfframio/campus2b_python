"""

1. Crea un programa que leyendo una lista ascendente de números del 1 al 5.
Guardar dicha lista en una variable llamada lista1.
compruebe se la primera posición es mayor que la última.  
En caso de serlo, deberá mostrar en pantalla ‘El
primer elemento de la lista es mayor que el último’, en caso contrario ‘El primer
elemento de la lista es menor que el último’
"""
lista1 = list(range(1, 6))
print(lista1)
if lista1[0] > lista1[-1]:
    print("El primer elemento de la lista es mayor que el último")
else:
    print("El primer elemento de la lista es menor que el último")

"""
2. Aprovechar el programa anterior y ordenar lista1 en sentido descendente. Volver
a ejecutar el código y comprobar que el resultado obtenido es el opuesto al del
punto1.
"""

lista1.sort(reverse=True)
print(lista1)
if lista1[0] > lista1[-1]:
    print("El primer elemento de la lista es mayor que el último")
else:
    print("El primer elemento de la lista es menor que el último")


"""
3. Crear un programa, que detecte si al introducir un número, éste es positivo o
negativo. Deberás usar la función input para introducir el número. NOTA: input
trabaja sólo con cadenas de texto, por lo que deberás convertir el dato
introducido a número.
"""
num = int(input("Introduce un número\n"))

if num >= 0:
    print("El número introducido es positivo")
else:
    print("El número introducido es negativo")


"""
4. Crear un programa que sea capaz de ‘adivinar’ un número del 1 al 4 mediante el
método de bisección.
1. Los pasos serían, elegir un número del 1 al 4.
2. El programa deberá preguntarnos si el número a adivinar es mayor que
2
3. Si la respuesta es positiva, deberá preguntarnos si el número es 3 o no
y ya tendríamos el resultado para números elegidos superiores a 2.
Si la respuesta del punto 2 es negativa, tendremos que plantear el caso
opuesto al del punto 3.
5. Crear un programa que para una edad dada, compruebe las 3 condiciones
siguientes:
1. Edad <0, muestre en pantalla ‘Edad negativa’.
2. 0 <= Edad <18, muestre en pantalla, ‘Menor de edad’.
3. Edad >= 18, muestre en pantalla, ‘Mayor de edad’.
Deberás plantear el ejercicio a través de if, elseif, else.
6. Crear un programa que dado un número, nos diga si el número es múltiplo de 2,
de 4 y 2 o no es múltiplo de 2. Tendrás que tener en cuenta que los múltiplos de
4 son múltiplos de 2, pero no al revés. Por ello el orden de las condiciones a
evaluar, es relevante.
7. Desarollar un programa que para 3 números dados, determine su orden (de
menor a mayor). Introduce los 3 números, mediante sendas funciones input
(una función input para cada número a introducir)
8. Desarrollar un programa que pida 2 palabras y nos diga si riman o no. Si las 3
últimas letras son iguales, las palabras riman. Si las 2 últimas letras son iguales,
las palabras riman poco. Si solo 1 letra o ninguna son iguales, las palabras no
riman. Ten en cuenta el tamaño mínimo de las palabras a comparar, si no el de al
menos 3 no podrás hacer las comparaciones.

"""

