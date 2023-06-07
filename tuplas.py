"""
1. Crea las siguientes tuplas:
tupla1 = (1,2,"tres","cuatro",5)
tupla2 = (1)
"""

tupla1 = (1,2,"tres","cuatro",5)
tupla2 = (1)
print(type(tupla1))
print(type(tupla2))

"""
2. Comprueba el tipo de tupla1 y tupla2. ¿Es correcto?. Haz los cambios necesarios
en tupla2 para que su tipo sea tupla.
"""

tupla2 = (1, )
print(type(tupla2))
print()

"""
3. Extrae las posiciones 1 y 2 de tupla1. Extrae las posiciones 2 y 3 de tupla1. 
Extrae los elementos desde la segunda posición hasta la anteúltima de tupla1. 
Extrae todos los elementos a partir de la segunda posición de tupla1.
"""
print(tupla1[1], tupla1[2], tupla1[3], tupla1[4])
print(tupla1[1: -1])
print(tupla1[1:])

"""
4. Comprueba la longitud de tupla1
"""
print()
print(len(tupla1))
print()

"""
5. Concatena tupla1 y tupla2, guarda el resultado en tupla3. Comprueba el 
tamaño de tupla3
"""

tupla3 = tupla1 + tupla2
print(tupla3)
print()

"""
6. Duplica tupla1 y guarda el resultado en tupla4.
"""

tupla4 = 2 * tupla1
print(tupla4)

print()
"""
7. Comprueba la existencia o no de los siguientes elementos en tupla1:
“tres”, “tre”, 4, “cinco
"""

print("tres" in tupla1)
print("tre" in tupla1)
print(4 in tupla1)
print("cinco" in tupla1)


    