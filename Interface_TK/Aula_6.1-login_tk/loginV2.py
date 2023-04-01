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
     

janela = Tk()
janela.title("Sistema de login")
janela.geometry("300x200")
janela.config(background=c1)
janela.resizable(width=FALSE, height=FALSE) 


frame_login = Frame(janela, bg=c0, height=190, width=290, relief='ridge')
frame_login.grid(row=0, column=0, padx=5, pady=5,sticky="NSEW") 

separador = Frame(janela, bg=c6, height=30, width=2, relief='flat')
separador.grid(row=0, column=0, padx=10, pady=10,sticky="NSEW")


def login():
    if (usuario.get() == "Robson" and senha.get() == "2402"):
        messagebox.showinfo('Sucesso', 'Seja bem vindo!') 
        janela.destroy()
    else:
        messagebox.showerror("Erro", "usuário ou senha incorretos") 



label_linha = Label(separador,width=21, text="DIGITE AS CREDENCIAIS",anchor=NE, font=("Arial", 12), bg=c1 , fg=c0).place(x=44, y=12)

Label1 = Label(separador, width=7, text="Usuário:", background=c6, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=50)
Label2 = Label(separador, width=7, text="Senha:", background=c6, foreground=c1, font=("Arial", 15, "bold")).place(x=8, y=90)

#Fundo da entry
label_linha = Label(separador,width=12, text="",anchor=NE, font=("Arial", 17, "bold"), bg=c1 , fg=c1).place(x=103, y=48)
label_linha = Label(separador,width=12, text="",anchor=NE, font=("Arial", 17, "bold"), bg=c1 , fg=c1).place(x=103, y=88)
 
usuario = Entry(separador, width=15, font=("Arial", 15, "bold"))
usuario.place(x=105, y=50)   

senha = Entry(separador, width=15, show="*", font=("Arial", 15, "bold"),fg=c8)
senha.place(x=105, y=90)


#Botão de login estilizado
label_linha = Label(separador,width=200, text="",anchor=NE, font=("Arial", 2, "bold"), bg=c1 , fg=c1).place(x=0, y=132)
label_linha = Label(separador,width=200, text="",anchor=NE, font=("Arial", 2, "bold"), bg=c1 , fg=c1).place(x=0, y=164)
label_linha = Label(separador,width=100, text="",anchor=NE, font=("Arial", 12, "bold"), bg=c5 , fg=c1).place(x=0, y=140)

Button(separador, text="Entrar", command=login, background=c1, foreground=c0, font=("Arial", 15, "bold")).place(x=140, y=132)





janela.mainloop()

