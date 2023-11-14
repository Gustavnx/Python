nome = str(input("Digite o seu nome: ")).lower()
sobrenome = str(input("Digite o seu sobrenome: ")).lower()
idade = int(input("Digite a sua idade: "))
email = str(input("Digite seu email: ")).lower()

dicionario = {
    "nome": nome,
    "sobrenome": sobrenome,
    "idade": idade,
    "email": email,
}

print(dicionario) 