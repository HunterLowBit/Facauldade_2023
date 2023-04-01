from tkinter import *
from tkinter import messagebox

c0 = "green"
c1 = "black"
c2 = "red"
c3 = "blue"
c4 = "white"

janela = Tk()
janela.title("sistema de login")
janela.geometry("310x300")
janela.config(background=c4)
janela.resizable(width=FALSE, height=FALSE)

frame_cima = Frame(janela, bg=c1, height=70, width=310, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=0,sticky="NSEW") 

frame_baixo = Frame(janela, bg=c2, height=200, width=310, relief='flat') 
frame_baixo.grid(row=1, column=0, padx=0, pady=0,sticky="NSEW")

#-------------------------------------#
#configuração do Frame_Cima           #
#-------------------------------------#

Label_name = Label(frame_cima, text="login",anchor=NE, font=("Arial", 22, "bold"), bg=c1, fg=c4) 
Label_name.place(x=5, y=5)

label_linha = Label(frame_cima,width=100, text="",anchor=NE, font=("Arial", 6, "bold"), bg=c1 , fg=c1)
label_linha.place(x=0, y=60)

#-------------------------------------#
#configuração do Frame_Baixo          #
#-------------------------------------#

label_name = Label(frame_baixo, text="Nome *",anchor=SW, font=("Arial", 15, "bold"), bg=c2, fg=c3)
label_name.place(x=15, y=20)


entry_name = Entry(frame_baixo, width=22,justify=LEFT, font=("Arial", 15), highlightthickness=1, bg=c4, fg=c1)
entry_name.place(x=15, y=50)


#-------------------------------------#
#configuração do Frame_Baixo+1        #
#-------------------------------------#

label_name = Label(frame_baixo, text="Senha *",anchor=SW, font=("Arial", 15, "italic"), bg=c2, fg=c3)
label_name.place(x=15, y=80)


entry_name = Entry(frame_baixo, width=22,justify=LEFT, font=("Arial", 12, "italic"), highlightthickness=1, bg=c4, fg=c1)
entry_name.place(x=15, y=110)

#criar botão de login

button_login = Button(frame_baixo, text="Login", highlightthickness=1, bg=c4, fg=c1, width=10, height=1)
button_login.place(x=15, y=150) 


janela.mainloop()