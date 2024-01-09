from tkinter import*

caixa = Tk()
caixa.title("Notas")
caixa.geometry("300x300")

def soma():
    soma_f1 = int(nota1_input.get())
    som_f2 = int(nota2_input.get())
    sum = soma_f1 + som_f2
    resultado.configure(text=f"soma: {sum}")




nota1 = Label(text="Digite sua nota: ", bg="red", fg="white", font="Arial")
nota1.pack()

nota1_input = Entry()
nota1_input.pack()

#botão_nota1 = Button()
#botão_nota1.pack()

nota2 = Label(text="Digite sua outra nota: ")
nota2.pack()

nota2_input = Entry()
nota2_input.pack()

botão_nota2 = Button(caixa, text="ENVIAR", command= soma)
botão_nota2.pack()

resultado = Label(text="")
resultado.pack

caixa.mainloop()