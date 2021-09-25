import random
from colorama import Fore

puntoJugador = int(0)
puntoCPU = int(0)


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

#inicio al programa
#if __name__ == "__main__":
#   jugarPiedraPapelTijera(puntoJugador, puntoCPU)
jugarPiedraPapelTijera(puntoJugador, puntoCPU)


