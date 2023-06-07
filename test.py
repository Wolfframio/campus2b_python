import math

print(3 + 2 -10)
print(3.0 + 2 - 10)
print(3 * 2)
print(10 / 3)
print((1 + 3) / 4)
print(1 + 3 / 4)
print(2**2)
print(3**2)
print(math.sqrt(25))
print(round((612**0.25), 2))


cadena1 = "Hola Mundo"
cadena2 = 'Hola Mundo'
cadena3 = "abcdefghi"
cadena4 = "123456"

cadena5 = cadena1 + cadena2
cadena6 = cadena1 + " " + cadena3
cadena7 = cadena1 * 2
print(cadena7)
print()
print(len(cadena5), len(cadena6), len(cadena7))

print(cadena1[0], cadena1[1], cadena1[2], 
      cadena1[1:(len(cadena1) - 2)], cadena1[0], cadena1[3], \
          cadena1[6], cadena1[9])
print()
cadena1[1:2]
cadena1[1:-1]
cadena1[1::3]
print("joserramon")

print(cadena4.count(cadena4))


print('H' in cadena1, 'M' in cadena1, 'Ma' in cadena1)
print()
cadena1mayus = cadena1.upper()
print(cadena1mayus)
cadena1minus = cadena1.lower()
print(cadena1minus)

print("\n")
print(cadena1.replace("Ho", "Mo"))
cadena10 = cadena1.replace("Ho", "Mo")
print(cadena10)


print('a', end="")
print('b')


lista = ["paco", "pepe", "peio", "joserra"]

for i in lista:
    print(i)

i = 0
while i <= len(lista):
    print("manolo")
    i += 1

lista.append("suso")
print(lista)

lista.extend("jorge")
print(lista)

lista = [3,2,1]
del (lista[2])
print(lista)

lista = [3,2,1]
print(lista.pop())

lista = [3,2,1,4,5,6,3]

while 3 in lista == True:
    lista.pop()
print(lista)

lista = ['Alberto','es','mas','alto','que','Pedro']
''.join(lista)
' '.join(lista)
'_'.join(lista)

lista = [0,2,4,6,1,3,5,7]
print(sorted(lista))

lista11 = [0,2,4,6,1,3,5,7]
lista11.sort()
print(lista11)

lista15 = [0,2,4,6,1,3,5,7]
lista15.sort(reverse = True)
print(lista15)



