diccionario = {'P2': 'Amaia', 'P3': 'Nekane', 'P4': 'Ekaitz'}
print('P1' in diccionario)

diccionario[3] = "jogito"

#obtener keys de diccionario
print(diccionario.keys())

#obtener valores de diccionario
print(diccionario.values())

"""
#obtener claves de un valor
def clave (diccionario, valor):
    for a in diccionario.keys():
        if diccionario [a] != "Nekane":
            
            print("El valor " + "Nekane" + " no está en el diccionario")
"""           


#abrir un doc. 
#volcar contenido spliteado por espacios. 
#crear diccionario. Clave es la palabra. Valor es el numero de apariciones
"""
quijote = open('..\\Intro//quijote.txt', encoding='utf-8')
contenido = quijote.read()
lista_palabras = contenido.split()
def tabla_frecuencias (texto):
    diccionario = {}
    for palabra in texto:
        if palabra in diccionario:
            diccionario [palabra] += 1
        else:
            diccionario [palabra] = 1
    return diccionario

print(tabla_frecuencias(lista_palabras))
"""
"""
1. Crea un diccionario que contenga las siguientes claves y valores:
◦ Claves: 1, 2, 3, 4, 5
◦ Valores: 1, 4, 9, 16, 25
Guarda el resultado en diccionario1
"""
diccionario1 = dict ({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
print(diccionario1)



"""
2. Una vez creado el diccionario, extraer sus valores.
"""
valores = diccionario1.values()
print(valores)


"""
3. Extrae el valor de la clave 2
"""
print(diccionario1[2])


"""
4. Añade un nuevo elemento (clave y valor). Clave 6 y valor 35. Comprueba el
resultado.
"""
diccionario1[6] = 35
print(diccionario1)


"""
5. Modifica el valor recién creado por el de 36
"""
diccionario1[6] = 36
print(diccionario1)


"""
6. Elimina la clave 5
"""
del diccionario1[5]
print(diccionario1)


"""
7. Añadir un nuevo elemento (clave y valor), donde la clave sea 7 y el valor una lista
compuesta de los valores ‘A’, ‘B’ y ‘C’
"""

diccionario1[7] = ['A', 'B', 'C']
print(diccionario1)


"""
8. Extraer el segundo valor de la lista correspondiente a la última clave (‘B’)
"""
print(diccionario1[7][1])
