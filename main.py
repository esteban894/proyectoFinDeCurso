#dejo viendo que hice en el curso para tener referencia para hacer este proyecto, 
# cuando vuelva de la escuela sigo haciendo cosas.
from tkinter import *
import random
from colorama import Fore, init
from random import randrange
from getpass import getpass
import os
import time

#---------raiz---------
root = Tk()
root.title("===Juegos de Esteban===")
root.iconbitmap("icons/chimuelo_icon.ico")
root.geometry("330x250")
root.resizable(0, 0)

#---------frame---------
miFrame = Frame(root)
miFrame.pack(fill= "both", expand=1)

#---------fondo---------
imagen = PhotoImage(file = "img/Mango.png")
fondo = Label (miFrame, image= imagen)
fondo.place(x= 0, y= 0, relwidth= 1, relheight= 1)

#---------label---------
label = Label(miFrame, text= "Elige una opción: ")
label.place(x= "10", y= "10")
label.config(bg= "#ffa751", font= ("Serif", 11))

#---------funciones---------
#--------------------------------------------------------------ahorcado----------------------------------
def ahorcado():
    os.system("cls")

    IMAGENES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

    palabra = getpass(Fore.BLUE + "Ingresa la palabra: " + Fore.RESET).lower()
    indice = random.randint(0, len(palabra)-1)
    letraInd = palabra[indice]
    espacios = ("_" * len(palabra[:indice])) + letraInd + ("_" * len(palabra[indice+1:]))
    espacios = list(espacios)
    intentos = 6
    
    init()

    while True:
        os.system("cls")

        for caracter in espacios:
            print(caracter, end=" ")
        print(IMAGENES[intentos])

        letra = input(Fore.BLUE + "Elige una letra: " + Fore.RESET).lower()[0]

        encontrado = False

        for idx, caracter in enumerate(palabra):
          if caracter == letra:
            espacios[idx] = letra
            encontrado = True
        if not encontrado:
          intentos -=1
        
        if "_" not in espacios:
          os.system("cls")
          print(Fore.GREEN + f"¡¡GANASTE, la palabra era '{palabra}'!!" + Fore.RESET)
          break
        
        if intentos == 0:
          os.system("cls")
          print(Fore.RED + f"Perdiste, la palabra era '{palabra}'" + Fore.RESET)
          break

#--------------------------------------------ta te ti-------------------------------------------

def taTeTi():
    os.system("cls")

    init()
    def printTablero(tablero):
        for i in range(0,7,3):
            print(tablero[i] + '|' + tablero[i+1] + "|" + tablero[i+2])

    tablero = [" "] * 9
    turnoX = True
    juegoTerminado = False

    while not juegoTerminado:
        posibleJugada = False

        while not posibleJugada:
            try:
                print(Fore.LIGHTBLUE_EX + "Ingrese celda (1-9): " + Fore.RESET)
                posicion = int(input())
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
            juegoTerminado = True

        if " " not in tablero:
            print(Fore.YELLOW + "Empate" + Fore.RESET)
            juegoTerminado = True
        turnoX = not turnoX

#-----------------------------------------------------piedra papel o tijera----------------------
puntoJugador = 0
puntoCPU = 0


def jugarPiedraPapelTijera(puntoJugador, puntoCPU):
    os.system("cls")

    init()
    
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
    os.system("cls")

    init()

    numero = randrange(1,101)

    print("Adivina el numero entre 1 y 100")

    dif = input("Elige la dificultad: facil o dificil \n").lower()

    if dif == "facil":

    	intentos = 10
    else:
    	intentos = 5

    print(f"Tienes {intentos} intentos")

    while True:
    	try:
    		valor = int(input())
    
    	except ValueError:
    		print(Fore.RED + "Ingresa un caracter valido" + Fore.RESET)
    
    	else:
        
    		if numero == valor:
    			print(Fore.GREEN + "Ganaste!!!" + Fore.RESET)
    			break
    		else:
            
    			intentos -=1
    
    			if numero < valor:
    				print(Fore.CYAN + "Mas chico" + Fore.RESET)
    				print(f"Intentos: {intentos}")
    			else:
                
    				if intentos > 0:
    					print(Fore.YELLOW + "Mas grande" + Fore.RESET)
    					print(f"Intentos: {intentos}")
    				else:
    					print(Fore.RED + "Perdiste! :(" + Fore.RESET)
    					print(f"El numero era {numero}")
    					break

#---------cara o cruz---------
def moneda():
    os.system("cls")
    caras = 0
    cruces = 0

    print(Fore.LIGHTBLUE_EX + 'Tirando moneda...')

    time.sleep(2)

    print('Moneda en el aire...')

    time.sleep(2)

    for i in range(1):
        tirada = random.choice(["cara", "cruz"])
        if tirada == "cara":
            caras += 1
        elif tirada == "cruz":
            cruces += 1

    if caras == 1:
        print('Ha salido cara' + Fore.RESET)
    elif cruces == 1:
        print('Ha salido cruz' + Fore.RESET)

#---------botonera---------
botonJuego1= Button(miFrame, text="Piedra, Papel o Tijeras", width=18, height=2, command=lambda:jugarPiedraPapelTijera(puntoJugador, puntoCPU))
botonJuego1.config(bg="#95a5a6")
botonJuego1.place(x= "20",y= "50")

botonJuego2= Button(miFrame, text="Ta-Te-Ti", width= 8, height= 2, command=lambda:taTeTi())
botonJuego2.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego2.place(x= "223", y= "50")

botonJuego3= Button(miFrame, text="Ahorcado", width= 10, height= 2, command=lambda:ahorcado())
botonJuego3.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego3.place(x= "20", y= "120")

botonJuego4= Button(miFrame, text="Encuentra el numero", width= 16, height= 2, command=lambda:encuentraElNumero())
botonJuego4.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego4.place(x= "153", y= "120")

botonJuego5= Button(miFrame, text="Cara o Cruz", width=10, height=2, command=lambda:moneda())
botonJuego5.config(bg="#95a5a6", font= ("Serif", 11))
botonJuego5.place(x= "20", y= "190")


root.mainloop()