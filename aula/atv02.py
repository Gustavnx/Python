palavra = lambda texto1, texto2 : texto1 + texto2 if len(texto1) > 5 and len(texto2) > 5 else "ERRO"

x = str(input("Digite uma palavra: "))
y = str(input("Digite outra palavra: "))


print(palavra(texto1= x, texto2= y))

