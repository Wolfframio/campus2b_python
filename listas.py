"""
Operaciones comunes con listas
1. Crea una lista con los nombres de los 6 primeros días de la semana. Llama a esa 
lista, lista1
2. Crea una lista con los números del 1 al 7, llama a esa lista, lista2
3. Crea las siguientes listas:
lista3 = ["Lunes", 1, "Mayo", 2018]
lista4 = [["Alberto", 1.75, 80],["Ana", 1.70, 65],["María", 1.90, 80]]
lista5 = [["Stanley Kubrick", ["Senderos de Gloria", 1957]], ["Woody 
Allen", ["Hannah y sus hermanas", 1986]]]
4. De lista1, extrae:
▪ Segundo elemento,
▪ Primer elemento,
▪ Último elmento
5. Comprueba qué tipo de dato tenemos en el último elemento de lista1
6. De lista5, escribe el código para obtener los siguientes datos:
▪ Stanley Kubrick
▪ 1986
▪ ["Senderos de Gloria", 1957]
▪ ["Woody Allen", ["Hannah y sus hermanas", 1986]]

7. Crea 2 copias de lista1, una en lista6 y otra en lista7. Después crea una nueva
lista8 que sea un alias de lista7. Crea una lista vacía en lista9
"""
lista1 = ["lunes", "martes", "miercoles", "jueves", "viernes"]

lista6 = lista1.copy()
#es lo mismo que lista6 = list(lista1) clona una lista

lista7 = lista1.copy()

lista8 = lista7


"""
8. 8. Elimina el "Miércoles" de la lista6, así como el "Viernes” de la lista8.
 Comprueba la lista7.
9. Ordena la lista1, lista2 y lista3. Estudia los resultados obtenidos.
10.Comprueba si ‘lunes’ existe en lista3.
11.Modifica el tercer elemento de la lista2, para que incluya el número 1000
12.Añade ‘Domingo’ a la lista1.
13.Ejecuta el comando necesario para obtener el tamaño de la lista5. ¿Cuál es el 
tamaño de la segunda lista en la lista4?
14.Extiende la lista6 con la lista3
"""


lista2 = [1, 2, 3, 4, 5, 6, 7]
lista22 = [1, 2, 3, 4, 5, 6, 7]
lista33 = list(lista22)
lista33.pop()



lista3 = ["Lunes", 1, "Mayo", 2018]
lista4 = [["Alberto", 1.75, 80],["Ana", 1.70, 65],["María", 1.90, 80]]
lista5 = [["Stanley Kubrick", ["Senderos de Gloria", 1957]], 
          ["Woody Allen", ["Hannah y sus hermanas", 1986]]]

print(lista1[1])
print(lista1[0])
print(lista1[-1])
print(type(lista1[1]))
print()

lista1 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']   
lista2 = [1, 2, 3, 4, 5, 6, 7]
lista2 = list(range(1, 8))

lista6 = list(lista1)
print(lista6)
lista7 = list(lista1)
lista8 = lista7

