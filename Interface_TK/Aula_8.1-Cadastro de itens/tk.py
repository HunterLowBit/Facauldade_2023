import db
from tkinter import *

def salvar():
    produto = produto_c.get()
    preço = preço_c.get()
    db.cria_db(produto,preço)
    produto_c.delete(0,END)
    preço_c.delete(0,END)



root = Tk()
root.title("p1")
root.geometry('300x200')
root.resizable(width=FALSE, height=FALSE)

frame = Frame(root, bg="black",height=200, width=300)
frame.grid(row=0, column=0)


label1 = Label(root, width=7, text='Produto',font=('Arial',15)).place(x=8,y=50)
label1 = Label(root, width=7, text='Preço',font=('Arial',15)).place(x=8,y=90)

produto_c = Entry(root,width=15,font=('Arial',15))
produto_c.place(x=110,y=50)
preço_c = Entry(root, width=15,font=('Arial',15))
preço_c.place(x=110,y=90)

Button(root, text="salvar",font=('Arial',12),bg="white",command=salvar).place(x=150,y=150)
root.mainloop()