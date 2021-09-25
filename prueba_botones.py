from tkinter import *

root = Tk()

root.title("Boton cambiante")
root.geometry("300x200")

frame = Frame()
frame.pack(fill = "both", expand = 1)

def cambiarBoton():
    boton.config(text="X")

boton = Button(frame, text=" ",  width=5, command=lambda:cambiarBoton())
boton.pack()

root.mainloop()