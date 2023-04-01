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
janela.title("Sistema de login")
janela.geometry("300x200")
janela.config(background=c1)
janela.resizable(width=FALSE, height=FALSE) 


frame_login = Frame(janela, bg=c0, height=190, width=290, relief='flat')
frame_login.grid(row=0, column=0, padx=5, pady=5,sticky="NSEW") 

separador = Frame(janela, bg=c6, height=30, width=2, relief='flat')
separador.grid(row=0, column=0, padx=10, pady=10,sticky="NSEW")


def login():
    if (usuario.get() == "Robson" and senha.get() == "2402"):
        messagebox.showinfo('Sucesso', 'Seja bem vindo!') 
        janela.destroy()
    else:
        messagebox.showerror("Erro", "usuário ou senha incorretos") 


Label1 = Label(separador, width=7, text="Usuário:", background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=50)
Label2 = Label(separador, width=7, text="Senha:", background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=90)

 
 
usuario = Entry(separador, width=15, font=("Arial", 15, "bold"))
usuario.place(x=105, y=50)   

senha = Entry(separador, width=15, show="*", font=("Arial", 15, "bold"))
senha.place(x=105, y=90)

Button(separador, text="Entrar", command=login, background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=140, y=140)





janela.mainloop()