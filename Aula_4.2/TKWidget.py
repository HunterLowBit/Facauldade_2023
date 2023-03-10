from tkinter import *
from tkinter import ttk
import tkinter as tk

class Application:
    def __init__(self, master=None):
        pass
root = Tk()
root.geometry('300x300')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        python_image = tk.PhotoImage(file='DOG.jpg')
        ttk.Label(self, image=python_image).pack()




Botao_Sair = Button(root, text="Fechar", command=root.destroy)
Botao_Sair.pack(pady=10)
Botao_Sair.place(x = 120, y = 250)
Application(root)
root.mainloop()