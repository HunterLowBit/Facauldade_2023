#invocar janela tkinter exibindo a hora atual que ira fechar a aplicação em 10 segundos
from tkinter import *
from time import sleep
import datetime

janela = Tk()
janela.title("Hora do dia")
janela.geometry("300x300")

def hora():
    hora = str(int(str(datetime.datetime.now()).split()[3].split(":")[0]))
    minuto = str(int(str(datetime.datetime.now()).split()[3].split(":")[1]))
    segundo = str(int(str(datetime.datetime.now()).split()[3].split(":")[2]))
    print(hora, minuto, segundo)
    label = Label(janela, text=hora + ":" + minuto + ":" + segundo, font=("Arial", 20))
    label.pack()
    sleep(120)
    label.destroy()
    janela.destroy()

button = Button(janela, text="Clique para fechar a aplicação", command=hora)
button.pack()

janela.mainloop()
