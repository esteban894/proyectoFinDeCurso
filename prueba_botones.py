from tkinter import *

"""root = Tk()

root.title("Boton cambiante")
root.geometry("300x200")

frame = Frame()
frame.config(bg= "#a4b0be")
frame.pack(fill = "both", expand = 1)

def cambiarBoton():
    pass

piedra = Button(frame, text="piedra",  width=5, command=lambda:cambiarBoton())
piedra.place(x= "45", y= "45")


papel = Button(frame, text="papel",  width=5, command=lambda:cambiarBoton())
papel.place(x= "45", y= "100")


tijera = Button(frame, text="tijera",  width=5, command=lambda:cambiarBoton())
tijera.place(x= "45", y= "140")


root.mainloop()


from tkinter import *

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x80")
        self.label = tk.Label(self.root,
                              text = "Text to be read")

        self.button = tk.Button(self.root,
                                text="Read Label Text",
                                command=self.readLabelText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def readLabelText(self):
        print(self.label.cget("text"))      

app=Test()
"""
from tkinter import *

def Jugar(boton):
    OpcionPiedra = boton.cget("text")
    print(OpcionPiedra)


root = Tk()
root.geometry("200x80")

label = Label(root, text= "piedra")
button = Button(root, text= "X", command=lambda:Jugar(label))

label2 = Label(root, text= "papel")
button2 = Button(root, text= "X", command=lambda:Jugar(label2))

label3 = Label(root, text= "tijera")
button3 = Button(root, text= "Ti", command=lambda:Jugar(label3))


label.pack()
button.pack()

label2.pack()
button2.pack()

label3.pack()
button3.pack()


root.mainloop()

