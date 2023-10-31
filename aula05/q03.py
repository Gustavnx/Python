g1 = str("m")
g2 = str("f")

opcao = input("""Qual seu gênero:
F - feminino
M - masculino
:  """).lower()


if opcao == g1:
    print("Sexo masculino")
elif opcao == g2: 
    print("sexo feminino")
else:
    print("sexo inválido") 

