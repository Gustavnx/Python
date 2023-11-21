def imc(peso, altura):
    return peso / altura ** 2 
lista = []

u1p = float(input("Digite seu peso: "))
u1m = float(input("Digite sua altura: "))

imc1 = imc(peso=u1p, altura=u1m)
lista.append(imc1)

u2p = float(input("Digite seu peso: "))
u2m = float(input("Digite sua altura: "))

imc2 = imc(peso=u2p, altura=u2m)
lista.append(imc2)

u3p = float(input("Digite seu peso: "))
u3m = float(input("Digite sua altura: "))

imc3 = imc(peso=u3p, altura=u3m)
lista.append(imc3)

u4p = float(input("Digite seu peso: "))
u4m = float(input("Digite sua altura: "))

imc4 = imc(peso=u4p, altura=u4m)
lista.append(imc4)

print(lista)

