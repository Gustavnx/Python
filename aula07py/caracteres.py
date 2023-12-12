def texto(nome):
    return len(nome)




def vogais(nome):
    contador = 0
    for i in nome:
        if i in "aeiou":
            contador += 1
    
    return contador 




def consoantes(nome):
    contador = 0
    for i in nome:
        if i in "bcdfghjklmnpqrstvxyz":
            contador += 1
    return contador
 




def vazio(nome):
    contador = 0
    for i in nome:
        if i in " ":
            contador += 1
    return contador