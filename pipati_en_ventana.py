from tkinter import *
import random

#---------raiz---------
raizP = Tk()
raizP.title("Piedra papel o tijera")
raizP.iconbitmap("icons/piedra.ico")
raizP.geometry("400x300")
raizP.resizable(0, 0)

#---------frame---------
frameP = Frame(raizP)
frameP.pack(fill= "both", expand= 1)

#---------icono---------
#piedra papel o tijera
imagen2 = PhotoImage(file= "img/Mojito.png")
fondo2 = Label(frameP, image= imagen2)
fondo2.place(x= 0, y= 0, relwidth= 1, relheight= 1)


#---------funciones----------------------


jugador = ""
CPU = random.choice(["piedra", "papel", "tijera"])

def jugadorPiedra(jugador):
    jugador = "piedra"


def jugadorPapel(jugador):
    jugador = "papel"


def jugadorTijera(jugador):
    jugador = "tijera"

       

#---------textos jugador-cpu----------
labelJ1 = Label (frameP, text= "Jugador")
labelJ1.place(x= 30, y= 20)
labelJ1.config(font= ("Verdana", 12))

labelJ2 = Label (frameP, text= "CPU")
labelJ2.place(x= 330, y= 20)
labelJ2.config(font= ("Verdana", 12))

fondoOp= Label(frameP, bg="#a4b0be")
fondoOp.place(x= 47, y= 57, width= 310, height=200)

#---------botones-----------
btnPiedra = Button(frameP, text= "Piedra", padx=2, width= 10, command=lambda:jugadorPiedra(jugador))
btnPiedra.place(x= 50, y= 60)
btnPiedra.config(bg= "#eccc68", font= ("Verdana", 12))


btnPapel = Button(frameP, text= "Papel", padx=2, width= 10, command=lambda:jugadorPapel(jugador))
btnPapel.place(x= 50, y= 95)
btnPapel.config(bg= "#eccc68", font= ("Verdana", 12))


btnTijera = Button(frameP, text= "Tijera", padx=2, width= 10, command=lambda:jugadorTijera(jugador))
btnTijera.place(x= 50, y= 130)
btnTijera.config(bg= "#eccc68", font= ("Verdana", 12))


OpCPU = Entry(frameP, width=16)
OpCPU.place (x=250,y=100)




raizP.mainloop()