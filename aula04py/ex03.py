def vh(valor, hora):
    return valor / hora

x = int(input("Qual o seu salário: "))
y = int(input("Quantas horas você trabalha: "))

resultado = vh(valor=x, hora=y)

print(f"Você ganha {resultado} por hora")  
