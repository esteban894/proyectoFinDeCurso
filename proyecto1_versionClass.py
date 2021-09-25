#Intente hacerlo de esta forma, pero me da errores que en el archivo proyecto1.py no me los da,
# entonces por ahora se queda de la otra forma, no se aplica la imagen al fondo del frame

from tkinter import ttk
from tkinter import *

class Ventana():
    def __init__(self, root):
        self.root = root
        self.root.title("¡Juegos de Esteban!")
        self.root.iconbitmap("chimueloV2.ico")
        self.root.geometry("500x300")

        miFrame = Frame(self.root)
        miFrame.pack()
        miFrame.config(bg="grey")
        
        imagenFondo = PhotoImage(file = "Mango.png")
        fondo = Label(miFrame, image= imagenFondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)


        Label(miFrame, text="Elige un juego: ").grid(row = 0, column = 0, pady= 5)
        boton1 = Button(miFrame, text="Piedra, papel o tijeras").grid(row = 1, column = 0,padx = 2, pady= 5)
        boton2 = Button(miFrame, text="Ta-Te-Ti").grid(row = 1, column= 1, padx = 2, pady= 5)


if __name__ == "__main__":
    root = Tk()
    app= Ventana(root)
    root.mainloop()