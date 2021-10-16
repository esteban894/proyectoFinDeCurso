"""posiciones:
1 2 3
4 5 6
7 8 9
"""
def taTeTi():

    def printTablero():
        for i in range(0,7,3):
            print(tablero[i] + '|' + tablero[i+1] + "|" + tablero[i+2])

    tablero = [" "] * 9
    turnoX = True
    juegoTerminado = False

    while not juegoTerminado:
        posibleJugada = False

        while not posibleJugada:
            try:
                posicion = int(input("Ingrese celda (1-9): "))
                if tablero[posicion - 1] == " ":
                    posibleJugada = True            
                else:
                    print("Esa posicion ya está ocupada")

            except (ValueError, IndexError):
                print("Valor ingresado incorrecto")

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
            print("El ganador es: " + "x" if turnoX else "El ganador es: o")
            juegoTerminado = True

        if " " not in tablero:
            print("Empate")
            juegoTerminado = True
        turnoX = not turnoX

taTeTi()