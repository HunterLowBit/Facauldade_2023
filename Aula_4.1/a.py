from tkinter import *
from tkinter import OptionMenu

class Application:
    def __init__(self, master=None):
        pass
root = Tk()
a = Radiobutton (root, text="Option 1", variable=vars, value=1,command=SEL)
b = Button (root, text="Option - 2")
texto = Label(text="|_______-__-_______|", font=('Arial',50))
textoa = Label( text="|_______-__-_______|", font=('Times New Roman',50,))
textob = Label(text="|_______-__-_______|", font=('Segoe Script',50))

c = Spinbox(text="abc")


texto.pack()
textoa.pack()
textob.pack()
a.pack()
b.pack()

c.pack()

Application(root)
root.mainloop()
