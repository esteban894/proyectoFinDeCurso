#dejo viendo que hice en el curso para tener referencia para hacer este proyecto, 
# cuando vuelva de la escuela sigo haciendo cosas.
from tkinter import *
import random
from colorama import Fore, init
from random import randrange

#---------raiz---------
root = Tk()
root.title("===Juegos de Esteban===")
root.iconbitmap("chimuelo_icon.ico")
root.geometry("330x210")
root.resizable(0, 0)

#---------frame---------
miFrame = Frame(root)
miFrame.pack(fill= "both", expand= 1)

#---------fondos---------
#principal
imagen = PhotoImage(file = "img/Mango.png")
fondo = Label (miFrame, image= imagen)
fondo.place(x=0, y=0, relwidth= 1, relheight= 1)
"""
#piedra papel o tijera
imagen2 = PhotoImage(file= "img/Mojito.png")
fondo2 = Label(ventanaPiPaTi, image= imagen2)
fondo2.place(x= 0, y= 0, relwidth= 1, relheight= 1)

#ta te ti
imagen3 = PhotoImage(file= "img/Radar.jpg")
fondo3 = Label(ventanaTateti, image= imagen3)
fondo3.place(x= 0, y= 0, relwidth= 1, relheight= 1)

#ahoracadito
imagen4 = PhotoImage(file= "img/Stripe.png")
fondo4 = Label(ventanaAhorcadito, image= imagen4)
fondo4.place(x= 0, y= 0, relwidth= 1, relheight= 1)

#encuentra el numero
imagen5 = PhotoImage(file= "img/BurningOrange.png")
fondo5 = Label(ventanaEncuentraN, image= imagen4)
fondo5.place(x= 0, y= 0, relwidth= 1, relheight= 1)

"""

#---------label---------
label = Label(miFrame, text= "Elige una opción: ")
label.place(x= "10", y= "10")
label.config(bg= "#ffa751", font= ("Serif", 11))

#---------funciones---------
#--------------------------------------------------------------ahorcado----------------------------------
def ahorcadito():
    from colorama import Fore

    oportunidades = 7
    palabraAdivinar = input("Ingrese la palabra a adivinar: ").lower()
    adivinado = ["_"]* len(palabraAdivinar)
    
    print(f"Oportunidades: {oportunidades}")
    while oportunidades > 0:
        print("".join(adivinado))
    
        encontrado = False
        ganado = False
    
        letraValida= False
        while not letraValida:
            letra = input("Ingrese letra: ").lower()[0]
            if not letra.isalpha():
                print("Caracter invalido, vuelve a intentar.")
            else:
                letraValida = True
    
        for i in range(0,len(palabraAdivinar)):
            if letra == palabraAdivinar[i]:
                adivinado[i] = letra
                encontrado = True
        if not encontrado:
            oportunidades -=1
            print(f"Letra no encontrada, te quedan {oportunidades} oportunidades")
        if "".join(adivinado) == palabraAdivinar:
            ganado = True
            oportunidades = 0
    
    if ganado:
        print(Fore.GREEN + f"Ganaste!\nLa palabra era {palabraAdivinar}" + Fore.RESET)
    else:
        print(Fore.RED + f"Perdiste!\nLa palabra era {palabraAdivinar}" + Fore.RESET)


#--------------------------------------------ta te ti-------------------------------------------
def taTeTi():

    def printTablero(tabero):
        for i in range(0,7,3):
            print(tablero[i] + '|' + tablero[i+1] + "|" + tablero[i+2])

    tablero = [" "] * 9
    turnoX = True
    juegoTerminado = False

    while not juegoTerminado:
        posibleJugada = False

        while not posibleJugada:
            try:
                posicion = int(input(Fore.BLUE + "Ingrese celda (1-9): " + Fore.RESET))
                if tablero[posicion - 1] == " ":
                    posibleJugada = True            
                else:
                    print(Fore.LIGHTCYAN_EX + "Esa posicion ya está ocupada" + Fore.RESET)

            except (ValueError, IndexError):
                print(Fore.RED + "Valor ingresado incorrecto" + Fore.RESET)

        tablero[posicion - 1] = "x" if turnoX else "o"
        printTablero(tablero)
        if (tablero[0] == tablero[1] == tablero[2] and tablero[0] != " " or
            tablero[3] == tablero[4] == tablero[5] and tablero[3] != " " or
            tablero[6] == tablero[7] == tablero[8] and tablero[6] != " " or
            tablero[0] == tablero[3] == tablero[6] and tablero[0] != " " or
            tablero[1] == tablero[4] == tablero[7] and tablero[1] != " " or
            tablero[2] == tablero[5] == tablero[8] and tablero[2] != " " or
            tablero[0] == tablero[4] == tablero[8] and tablero[0] != " " or 
            tablero[2] == tablero[4] == tablero[6] and tablero[2] != " " ):
            if turnoX:
                print(Fore.GREEN + 'El ganador es: "x"' + Fore.RESET)
            else:
                print(Fore.GREEN + 'El gnador es: "o"' + Fore.RESET)
            #print(Fore.GREEN + "El ganador es: " + "x" if turnoX else "El ganador es: o" + Fore.RESET)
            juegoTerminado = True

        if " " not in tablero:
            print(Fore.YELLOW + "Empate" + Fore.RESET)
            juegoTerminado = True
        turnoX = not turnoX

#-----------------------------------------------------piedra papel o tijera----------------------
puntoJugador = 0
puntoCPU = 0


def jugarPiedraPapelTijera(puntoJugador, puntoCPU):

    while True:

        jugador = input("Elegí una opción: piedra, papel o tijera \n").lower()
        compu = random.choice(["piedra", "papel", "tijera"])

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


#funciones utilizadas dentro del juego
def ganoJugador(jugador, oponente):
    if ((jugador == "piedra" and oponente == "tijera") or
        (jugador == "tijera" and oponente == "papel") or
        (jugador == "papel" and oponente == "piedra")):
        return True
    else:
        return False


def ganoCPU(jugador, oponente):
    if ((oponente == "piedra" and jugador == "tijera") or
        (oponente == "tijera" and jugador == "papel") or
        (oponente == "papel" and jugador == "piedra")):
        return True
    else:
        return False    


#----------------------------------------encuentra el numero-------------------------

def encuentraElNumero():

    numero = randrange(1,101)

    print("Adivina el numero entre 1 y 100")

    init()

    while True:
        try:
            valor = int(input())
        except ValueError:
            print(Fore.LIGHTRED_EX + "ingresa un caracter valido." + Fore.RESET)
        else:
            if numero == valor:
                print(Fore.GREEN + f"Ganaste, el numero era {numero}" + Fore.RESET)
                break
            print(Fore.CYAN + "Mas chico" + Fore.RESET if (numero < valor) else Fore.YELLOW + "Mas grande" + Fore.RESET)


#---------botonera---------
botonJuego1= Button(miFrame, text="Piedra, Papel o Tijeras", width=18, height=2, command=lambda:jugarPiedraPapelTijera(puntoJugador, puntoCPU))
botonJuego1.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego1.place(x= "20",y= "50")

botonJuego2= Button(miFrame, text="Ta-Te-Ti", width= 8, height= 2, command=lambda:taTeTi())
botonJuego2.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego2.place(x= "223", y= "50")

botonJuego3= Button(miFrame, text="Ahorcado", width= 10, height= 2, command=lambda:ahorcadito())
botonJuego3.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego3.place(x= "20", y= "120")

botonJuego4= Button(miFrame, text="Encuentra el numero", width= 16, height= 2, command=lambda:encuentraElNumero())
botonJuego4.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego4.place(x= "153", y= "120")

root.mainloop()