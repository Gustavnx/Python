def hora(x):
    if x <= 11 and x >= 4:
      print("Bom dia")
    elif x >= 12 and x <= 18:
       print("Boa tarde")
    elif x >= 19 and x <= 24:
       print("Boa noite")
    else:
       print("Nada ave a hora man")
       
       

hr = int(input("Digita a hora man: ")) 

print(hora(hr)) 

