pessoa = ["Abel", 28, 1.79, True, 50]


print(pessoa[0])

pessoa2 = {
    "nome": "Abel",
    "idade": 28,
    "altura": 1.79
}

print(pessoa2["nome"])



dicionario = {
    "Módulo": "Python",
    "Instituição": "Infinity School"
}

dicionario2 = dict( [ ("Módulo", "Python"), ("Instiuição", "Infinity School") ] )

dicionario3 = dict(Modulo = "Python", Instituicao = "Infinity School")

dicionario4 = {
    "Módulo": "Phyton",
    "instituição": "Infinity School" 

}


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cpf = str(input("Digite seu cpf: "))

pessoa = {
    "nome": nome,
    "idade": idade,
    "cpf": cpf
}