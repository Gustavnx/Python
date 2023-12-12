from operacoes import *

numero1 = int(input("Digite um número: "))

numero2 = int(input("Digite um número: "))


operacao = str(input("""
Somar
Subtrair 
Multiplicar
Dividir                  

Escolha qual operação você deseja prosseguir: """)).lower()




if operacao == "somar":
    print(somar(n1= numero1, n2= numero2))
    

elif operacao == "subtrair":
    print(subtrair(n1= numero1, n2= numero2))
    

elif operacao == "multiplicar":
    print(multiplicar(n1= numero1, n2= numero2))
   

elif operacao == "dividir":
    print(dividir(n1= numero1, n2= numero2))
   

else:
    print("Operação inválida")

