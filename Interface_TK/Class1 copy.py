#janela de tkinter  
from tkinter import *

janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x300")

#Label
label = Label(janela, text="Login")
label.pack()

#Entry
entrada = Entry(janela)
entrada.pack()

#Botao
botao = Button(janela, text="Entrar")
botao.pack()

#loop   
janela.mainloop()
