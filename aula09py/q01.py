lista_de_numeros = []  


for i in range(1, 11):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
      lista_de_numeros.append(numeros)


print(lista_de_numeros)

