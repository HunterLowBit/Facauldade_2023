from tkinter import *


class Application:
    def __init__(self, master=None):
        pass
root = Tk()
texto_Vermelho = Label(foreground="red",text="Olá, Seja bem vindo ao TKinter", font=('Times New Roman',50,))
Botao_Sair = Button(root, text="Fechar", command=root.destroy)

texto_Vermelho.pack()
Botao_Sair.pack(pady=10)

Application(root)
root.mainloop()
