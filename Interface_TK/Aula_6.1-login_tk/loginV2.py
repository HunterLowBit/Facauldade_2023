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
janela.config(background=c0)
janela.resizable(width=FALSE, height=FALSE) 

frame_login = Frame(janela, bg=c1, height=190, width=290, relief='flat')
frame_login.grid(row=0, column=0, padx=5, pady=5,sticky="NSEW") 

def login():
    if (usuario.get() == "Robson" and senha.get() == "2402"):
        messagebox.showinfo('Sucesso', 'Seja bem vindo!') 
        janela.destroy()
    else:
        messagebox.showerror("Erro", "usuário ou senha incorretos") 


Label1 = Label(frame_login, width=7, text="Usuário:", background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=10)
Label2 = Label(frame_login, width=7, text="Senha:", background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=50)

 
usuario = Entry(frame_login, width=15, font=("Arial", 15, "bold"))
usuario.place(x=110, y=10)   

senha = Entry(frame_login, width=15, show="*", font=("Arial", 15, "bold"))
senha.place(x=110, y=50)

Button(frame_login, text="Entrar", command=login, background=c0, foreground=c1, font=("Arial", 15, "bold")).place(x=110, y=90)





janela.mainloop()