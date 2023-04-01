from tkinter import *
from tkinter import messagebox

c0 = "white"
c1 = "black"
c2 = "red"
c3 = "blue"
c4 = "green"
c5 = "yellow"
c6 = "orange"
c7 = "pink"
c8 = "purple"
c9 = "brown"
c10 = "grey"
c11 = "dark grey"
c12 = "light grey"
c13 = "brown"
c14 = "ice blue"
c15 = "ice green"
c16 = "ice yellow"
c17 = "ice orange"
c18 = "ice pink"
c19 = "ice purple"
c20 = "ice brown"
c21 = "ice grey"
c22 = "ice dark grey"
c23 = "ice light grey"


janela = Tk()
janela.title("sistema de login")
janela.geometry("400x400")
janela.config(background=c0)
janela.resizable(width=FALSE, height=FALSE) 


def login():
    if (usuario.get() == "admin" and senha.get() == "admin"):
        messagebox.showinfo("Bem vindo", "Bem vindo ao sistema")
        janela.destroy()
    else:
        messagebox.showerror("Erro", "usuário ou senha incorretos") 


Label(janela, text="Usuário:", background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=10)
Label(janela, text="Senha:", background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=50)

 
usuario = Entry(janela, width=20, font=("Arial", 15, "bold"))
usuario.place(x=100, y=10)   

senha = Entry(janela, width=20, show="*", font=("Arial", 15, "bold"))
senha.place(x=100, y=50)

Button(janela, text="Entrar", command=login, background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=100, y=90)






janela.mainloop()