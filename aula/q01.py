def funcao(palavra):
    quantidade_vogais = 0
    for letra in palavra:
        if letra in "aeiou":
            quantidade_vogais += 1
            if quantidade_vogais > 3:
                return "mais de 3 vogais"
            else:
                return "menos de 3 vogais"
        return quantidade_vogais

        

palavra = str(input("Digite uma palavra: ")).lower()

print(funcao(palavra)) 