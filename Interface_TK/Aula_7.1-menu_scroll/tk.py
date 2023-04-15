from tkinter import *
from tkinter import messagebox
janela = Tk()
janela.title("-")
janela.geometry("300x200")
janela.config(background='black')
janela.option_add('*tearOff', FALSE)


def mensagem():
    messagebox.showinfo('EM CONSTRUÇÃO','Não esta pronto, aguarde')
 

#menu
menubar = Menu(janela) 
janela.config(menu=menubar) 
filemenu = Menu(menubar)
menubar.add_cascade(label="Arquivos", menu=filemenu) 
filemenu.add_command(label="Abrir", command=mensagem)
filemenu.add_separator() 
filemenu.add_command(label="Sair", command=janela.quit) 


menubar.add_command(label="Sair", command=janela.quit)
label = Label(text="Primeiramente", bg='black', fg='white', font=('times new roman', 20,'bold')).place(x=100,y=100)  



janela.mainloop()