conan = open("conan.txt", "r")
texto = conan.read()

start = 0
end = 0
dic = {}
while texto.find("Conan:", start) != -1:
    start = texto.find("Conan:", start)
    end = texto.find("\n", start)
    dic[start] = texto[start + 7: end]
    print(texto[start + 7: end + 1])
    start = texto.find("Conan:", start) + 1
print()
print(dic)
