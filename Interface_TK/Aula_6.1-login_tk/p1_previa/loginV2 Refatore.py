from tkinter import *
from tkinter import messagebox
     
janela = Tk()
janela.title("Sistema de login")
janela.geometry("300x200")
janela.resizable(width=FALSE, height=FALSE) 

frame_login = Frame(janela, bg='black', height=200, width=300, relief='ridge')
frame_login.grid(row=0, column=0) 

def login():
    if (usuario.get() == "Robson" and senha.get() == "2402"):
        messagebox.showinfo('Sucesso', 'Seja bem vindo!') 
        janela.destroy()
    else:
        messagebox.showerror("Erro", "usuário ou senha incorretos") 
        
Label1 = Label(frame_login, width=7, text="Usuário:", background='orange', foreground='black', font=("Arial", 15, "bold")).place(x=10, y=50)
Label2 = Label(frame_login, width=7, text="Senha:", background='orange', foreground='black', font=("Arial", 15, "bold")).place(x=10, y=90)

usuario = Entry(frame_login, width=15, font=("Arial", 15, "bold"))
usuario.place(x=110, y=50)   
senha = Entry(frame_login, width=15, show="*", font=("Arial", 15, "bold"),fg='black')
senha.place(x=110, y=90)

Button(frame_login, text="Entrar", command=login, background='orange', foreground='white', font=("Arial", 15, "bold")).place(x=140, y=130)
janela.mainloop()