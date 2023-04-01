from tkinter import *
from tkinter import ttk
import tkinter as tk

class Application:
    def __init__(self, master=None):
        pass

#def printa_no_botao():
 #   print('fui clicado')
  #  Botao.config(text='Fui clicado')
    
def muda_botao():
    print('trocando cor')
    Botao.config(foreground='red',background='black', font=('Times New Roman',14), text='Fui clicado')
  
    
    
root = tk.Tk()
root.geometry("300x200")

rotulo = tk.Label(root, text="Texto teste")
rotulo.pack() 
Botao = tk.Button(root, text="Clica aqui", command=muda_botao)
Botao.pack() 



botao_sair = Button(root, text="Confirmar e Fechar", command=root.destroy)
botao_sair.pack(pady=10)
botao_sair.place(x = 90, y = 150)

def muda_label(evento):
    print('Apertei 1')
    rotulo.config(text='ASD')

root.bind('1', muda_label)
    

Application(root)
root.mainloop()

#pygubu
#rad RAPID APP DEVELOPEMENT

#TROCAR FONTE E COR DA BOTÂO EM FUNÇÃO


