def numero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return(n1)
    elif n2 > n1 and n2 > n3:
        return(n2)
    elif n3 > n1 and n3 > n2:
        return(n3)
    



x1 = int(input("Digite um número: "))
x2 = int(input("Digite outro número: "))
x3 = int(input("Digite mais um número: "))

print(numero(x1, x2, x3)) 

