import random
from colorama import Fore

puntoJugador = 0
puntoCPU = 0


def jugarPiedraPapelTijera(puntoJugador, puntoCPU):
    
    jugador = input("Elegí una opción: piedra, papel o tijera \n").lower()
    compu = random.choice(["piedra", "papel", "tijera"])

    if jugador == compu:
        return Fore.YELLOW + f"Empate! \nVan {puntoJugador} a {puntoCPU}\n" + Fore.RESET

    if gano_el_jugador(jugador, compu):
        puntoJugador += 1
        return Fore.GREEN + f"Ganaste! \nVan {puntoJugador} a {puntoCPU}\n" + Fore.RESET
    else:
        puntoCPU += 1
        return Fore.RED + f"Perdiste! \nVan {puntoJugador} a {puntoCPU}\n" + Fore.RESET


def gano_el_jugador(jugador, oponente):
    if ((jugador == "piedra" and oponente == "tijera") or
        (jugador == "tijera" and oponente == "papel") or
        (jugador == "papel" and oponente == "piedra")):
        return True
    else:
        return False


while True:
    print(jugarPiedraPapelTijera(puntoJugador, puntoCPU))
    if puntoJugador != 3 or puntoCPU != 3:
        if puntoJugador == 3:
            print("Ganaste la partida!!")
        elif puntoCPU == 3:
            print("la CPU ganó la partida :'(")
    else:
        break