import random
x = True
dados = []

while x:
    nome = str(input("Digite seu nome: ")).lower()
    for letra in nome:
        if letra not in "abcdefghijklmnopqrstuvxyzç":
           continue           
              
    
     

    cpf = str(input("Digite seu cpf: "))
    if len(cpf) < 14:
        print("Cpf inválido!")
        continue
    
    valor = float(input("Digite o valor do produto: "))
    if valor not in (0,1,2,3,4,5,6,7,8,9):
        print("Valor inválido!")
        continue

    fim = str(input("Deseja sair do programa? sim ou não: ")).lower()

    dados.append((nome, cpf, valor))

    if fim == "não" and "nao":
        continue
    if fim == "sim":
        break

computador = random.choice(dados)
    
print(computador)

print(f"Parabéns {computador[0]}, cpf:{computador[1]}, você foi sorteado por ter feito uma compra no valor de R${computador[2]}")




