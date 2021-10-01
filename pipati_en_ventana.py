from tkinter import *
import random
from colorama import Fore

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

puntoJugador = 0
puntoCPU = 0

def Jugar(boton):

    def jugarPiedraPapelTijera():

        while True:

            global puntoJugador
            global puntoCPU

            jugador = boton.cget("text")
            compu = random.choice(["Piedra", "Papel", "Tijera"])

            if jugador == compu:  #Empate
                print(Fore.YELLOW + f"Empate!")
                print(f"La CPU jugó: {compu}" + Fore.RESET)
                print(Fore.CYAN + f"Marcador: {puntoJugador} a {puntoCPU}" + Fore.RESET)


            if ganoJugador(jugador, compu): #Ganas tu
                puntoJugador += 1
                print(Fore.GREEN + f"Ganaste la jugada!")
                print(f"La CPU jugó: {compu}" + Fore.RESET)
                print(Fore.CYAN + f"Marcador: {puntoJugador} a {puntoCPU}" + Fore.RESET)

            elif ganoCPU(jugador, compu): #Gana la compu
                puntoCPU += 1
                print(Fore.RED + f"Perdiste la jugada!")
                print(f"La CPU jugó: {compu}" + Fore.RESET)
                print(Fore.CYAN + f"marcador: {puntoJugador} a {puntoCPU}" + Fore.RESET)

            if (puntoJugador == 3):
                print(Fore.GREEN + "¡¡¡Ganaste!!!" + Fore.RESET)
                break
            elif (puntoCPU == 3):
                print(Fore.RED + "Gano la CPU :(" + Fore.RESET)
                break


    def ganoJugador(jugador, oponente):
        if ((jugador == "Piedra" and oponente == "Tijera") or
        (jugador == "Tijera" and oponente == "Papel") or
        (jugador == "Papel" and oponente == "Piedra")):
            return True
        else:
            return False
    
    def ganoCPU(jugador, oponente):
        if ((oponente == "Piedra" and jugador == "Tijera") or
        (oponente == "Tijera" and jugador == "Papel") or
        (oponente == "Papel" and jugador == "Piedra")):
            return True
        else:
            return False
    
    jugarPiedraPapelTijera()



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
btnPiedra = Button(frameP, text= "Piedra", padx=2, width= 10, command=lambda:Jugar(btnPiedra))
btnPiedra.place(x= 50, y= 60)
btnPiedra.config(bg= "#eccc68", font= ("Verdana", 12))


btnPapel = Button(frameP, text= "Papel", padx=2, width= 10, command=lambda:Jugar(btnPapel))
btnPapel.place(x= 50, y= 95)
btnPapel.config(bg= "#eccc68", font= ("Verdana", 12))


btnTijera = Button(frameP, text= "Tijera", padx=2, width= 10, command=lambda:Jugar(btnTijera))
btnTijera.place(x= 50, y= 130)
btnTijera.config(bg= "#eccc68", font= ("Verdana", 12))

#---------salida de Opcion CPU---------
OpCPU = Entry(frameP, width=16)
OpCPU.place (x=250,y=100)

#---------marcador---------

separador = Label(frameP,text="-")
separador.place(x= 175, y= 180)
separador.config(bg= "#a4b0be")

marcadorJ1 = Entry(frameP, text="0")
marcadorJ1.place(x= 150, y= 180, width=25)

marcadorCPU = Entry(frameP, text= "0")
marcadorCPU.place (x= 185, y= 180, width= 25)

raizP.mainloop()