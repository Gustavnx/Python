nota1 = int(input("Qual a sua primeira nota: "))
nota2 = int(input("Qual a sua segunda nota: "))
nota3 = int(input("Qual a sua terceira nota: "))
nota4 = int(input("Qual a sua quarta nota: "))

sn = nota1 + nota2 + nota3 + nota4
media = sn / 4

notas = [nota1,nota2, nota3, nota4]

maior = (max(notas))
menor = (min(notas))

if media >= 7:
    situacao = "aprovado"

if media < 7:
    situacao = "reprovado"

dicionario = {
    "Nome do aluno": "Gustavo Magalhães",
    "Suas 4 notas" : notas,
    "Maior nota" : maior,
    "Menor nota" : menor,
    "Sua média" : media,
    "Situação" : situacao 
}

print(dicionario)

