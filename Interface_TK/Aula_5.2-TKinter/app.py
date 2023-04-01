from tkinter import *


class Application:
    def __init__(self, master=None):
        pass
    
root = Tk()

def muda_botao_dois(evento):
    print('Apertei o botão 2')
    texto_Vermelho.config(
    text='2 foi apertado',
    bg='red', 
    fg='blue'
    )
    
def fechar(evento):#Pode ser escrito em português alem de puxar 'command' sendo uma tupla
    print('fechando')
    Botao_Sair.config( 
        text='fechando app',
        command=root.quit
    )
    
    
root.bind('e', fechar)

root.bind('2',muda_botao_dois)

label = Label(fg='blue')

texto_Vermelho = Label(foreground="red",text="Olá, Seja bem vindo ao TKinter", font=('Times New Roman',50,))
Botao_Sair = Button(root, text="Fechar", command=root.destroy)

texto_Vermelho.pack()
Botao_Sair.pack(pady=10)







Application(root)
root.mainloop()