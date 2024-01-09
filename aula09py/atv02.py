from tkinter import*

caixa = Tk()
caixa.title("NOTAS")
caixa.geometry("300x300")
def media():
    n1 = float(nota1_input.get())
    n2 = float(nota2_input.get())
    n3 = float(nota3_input.get())
    soma = n1 + n2 + n3
    m = soma / 3

    if m >= 7 and m <= 9:
        resultado.configure(text=f"Você foi aprovado", bg="green", fg= "white")
    elif m < 7:
        resultado.configure(text=f"Você foi reprovado", bg="red", fg= "white")
    elif m == 10:
        resultado.configure(text=f"Você foi aprovado com distinção", bg="blue", fg="white")
     




nota1 = Label(text="Digite sua primeira nota: ",bg= "#015B39", fg= "white").pack()

nota1_input = Entry()
nota1_input.pack()

nota2 = Label(text="Digite sua segunda nota: ",bg= "#015B39", fg= "white").pack()

nota2_input = Entry()
nota2_input.pack()

nota3 = Label(text="Digite sua terceira nota: ",bg= "#015B39", fg= "white").pack()

nota3_input = Entry()
nota3_input.pack()

botão = Button(caixa, text="Calcular", command=media, bg="#A9C6BB", fg= "white")
botão.pack()

resultado = Label(text="")
resultado.pack()


caixa.mainloop()