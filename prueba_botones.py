from tkinter import *

root = Tk()

root.title("Boton cambiante")
root.geometry("300x200")

frame = Frame()
frame.pack(fill = "both", expand = 1)

def cambiarBoton():
    boton.config(text="X")
    
    ventana2 = Tk()
    ventana2.geometry("200x100")

    entrada = Entry(ventana2)
    entrada.pack()

    ventana2.mainloop()

boton = Button(frame, text=" ",  width=5, command=lambda:cambiarBoton())
boton.place(x= "45", y= "45")

root.mainloop()
