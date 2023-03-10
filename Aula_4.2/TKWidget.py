from tkinter import *
from tkinter import ttk
import tkinter as tk

class Application:
    def __init__(self, master=None):
        pass



root = tk.Tk()
root.geometry("300x200")


rotulo = tk.Label(root, text="Termos de Serviço!")
rotulo.pack() 
rotulo2 = tk.Label(root, text="Digite seu nome e selecione se deseja receber emails!")
rotulo2.pack() 



caixa_texto = tk.Entry(root,)
caixa_texto.pack()  

opcoes = ["Sim", "Não"]
menu = tk.OptionMenu(root, tk.StringVar(), *opcoes)
menu.pack()  


caixa_selecao = tk.Checkbutton(root, text="Aceito os termos e condições")
caixa_selecao.pack()  


btn = Button(root, text="Fechar", command=root.destroy)
btn.pack(pady=10)
btn.place(x = 120, y = 150)

Application(root)
root.mainloop()