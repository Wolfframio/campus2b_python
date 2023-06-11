conan = open(r"python\conan.txt", "r")
texto = conan.read()

""" lista_n = texto.split("\n")

lista_final = []
for elemento in lista_n:
    lista_final.extend(elemento.split(" "))
 """

for caracter in texto:
    if caracter == '\n':
        break
    print(caracter, end='')
