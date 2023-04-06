from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("p1")
root.geometry('300x200')
root.resizable(width=FALSE, height=FALSE)

frame = Frame(root, bg="black",height=200, width=300)
frame.grid(row=0, column=0)

def login():
    if (usuario.get()== 'robson' and senha.get() == '2402'):
        messagebox.showinfo('bem vindo','sucesso')
        root.destroy()
    else:
        messagebox.showinfo('Errado','Tente novamente')

label1 = Label(root, width=7, text='usuario',).place(x=8,y=50)

root.mainloop()

