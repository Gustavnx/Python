def sem(cor):
    if cor == "vermelho":
        return "PARE!"
    elif cor == "amarelo":
        return "ATENÇÃO!"
    elif cor == "verde":
        return "CONTINUE!"
    else:
        return "ERROR!"
    
print("""
      VERDE
      VERMELHO 
      AMARELO""")

cor = str(input("Escolha uma cor: ")).lower()

print(sem(cor))
    