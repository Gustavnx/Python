
from random import choice

def ganhador (usuario, computador):
        if usuario == "pedra" and computador == "tesoura":
            print("Você Ganhou!")
        elif usuario == "tesoura" and computador == "pedra":
            print("Máquina Ganhou!")


        elif usuario == "tesoura" and computador == "papel":
            print("Você Ganhou!")
        elif usuario == "papel" and computador == "tesoura":
            print("Máquina Ganhou!")


        elif usuario == "papel" and computador == "pedra":
            print("Você Ganhou!")
        elif usuario == "pedra" and computador == "papel":
            print("Máquina Ganhou!")
        
        else:
            print("Empatou!")



flag = True

while flag:


    opcao = str(input(
    """ 
    - Pedra 
    - Papel
    - Tesoura
    Escolha uma das opções acima: """)).lower()
    
    lista = ["pedra", "papel", "tesoura"]

    maquina = choice(lista)

    if opcao not in lista:
        print("Opção Inválida!")
        break 

    print(opcao)
    print(maquina)


    ganhador(opcao, maquina) 
    
    while True:

        x = input(
    """
    Digite "1" para continuar 

    Digite "2" para parar 

    Digite a sua opção:  """)
        
        if x == "1":
            break
        elif x == "2":
            flag = False
            break
        else:
            print("Inválido!")
            continue
