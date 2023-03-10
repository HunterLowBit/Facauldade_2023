from tkinter import *
from tkinter import ttk
import tkinter as tk

class Application:
    def __init__(self, master=None):
        pass
root = Tk()
root.geometry('300x300')






Botao_Sair = Button(root, text="Fechar", command=root.destroy)
Botao_Sair.pack(pady=10)
Botao_Sair.place(x = 120, y = 250)
Application(root)
root.mainloop()