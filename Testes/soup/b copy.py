#janela tkinter
from tkinter import *

janela = Tk()
janela.title("janela tkinter")
janela.geometry("500x500")


texto = Label(janela, text="testando")
texto.pack()

texto2 = Label(janela, text="testando 2")
texto2.pack()    

    
#mainloop

janela.mainloop()