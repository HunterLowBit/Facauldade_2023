#criar janela tkinter
from tkinter import *

janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

#criar botão    
botao = Button(janela, text="Login", command=lambda: janela.destroy())
botao.pack()




#criar label e entrada de dados
label = Label(janela, text="Digite o nome do usuário: ")
label.pack()

entrada = Entry(janela)
entrada.pack()




janela.mainloop()