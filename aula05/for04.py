print("""Frutas:
      -MAÇA
      -LARANJA
      -LIMÃO
      
      """)

while True: 
    frutas = ['MACA', 'LARANJA', 'LIMAO']

    fruta = str(input("Escolha uma fruta: ")).upper().strip()
    
    if fruta in frutas:
      print("Fruta válida")  
    if fruta == "FIM":
        print("fim")
        break 
    else:
        print("Fruta inválida")
    
   
       

    
        