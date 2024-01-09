from tkinter import*

caixa = Tk()
caixa.title("Aula 1 TK")
caixa.geometry("300x300")

def saudacao():
    nome = usuario_input.get()
    resultado.configure(text=f"Bem vindo {nome}" )

usuario = Label(text="Digite o seu nome: ")
usuario.pack()

usuario_input = Entry()
usuario_input.pack()

botão_enviar = Button(caixa, text="Enviar", command=saudacao)
botão_enviar.pack()

resultado = Label(text="")
resultado.pack()


caixa.mainloop()