nota1 = float(input("Nota prova 1: "))
nota2 = float(input("Nota prova 2: "))
nota3 = float(input("Nota prova 3: "))
nota4 = float(input("Nota prova 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 

if media >= 7:
    print("Aprovado")
elif media <= 7:
    print("Reprovado")