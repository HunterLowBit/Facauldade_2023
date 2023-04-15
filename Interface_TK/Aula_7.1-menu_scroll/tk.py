from tkinter import *
from tkinter import messagebox
janela = Tk()
janela.title("TESTE DE TEXTO")
janela.geometry("660x388")
janela.config(background='black')
janela.resizable(False, False)
janela.option_add('tearOff', FALSE)


def mensagem():
    messagebox.showinfo('EM CONSTRUÇÃO','Não esta pronto, aguarde')
 
menubar = Menu(janela) 
janela.config(menu=menubar) 
filemenu = Menu(menubar)
menubar.add_cascade(label="Arquivos", menu=filemenu) 
filemenu.add_command(label="Abrir", command=mensagem)
filemenu.add_separator() 
filemenu.add_command(label="Sair", command=janela.quit) 

menubar.add_command(label="Sair", command=janela.quit)

texto = Text(janela)
texto.grid(row=0, column=0, sticky="nsew")

# Adicionar a barra de rolagem ao texto
scrollbar = Scrollbar(janela, command=texto.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
texto.config(yscrollcommand=scrollbar.set)

texto.insert('end', 'DIGITE AQUI!')


janela.mainloop()