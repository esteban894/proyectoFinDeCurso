def piPaTi():
    import random
    
    class jugador():
        def __init__(self, nombre):
            self.nombre = nombre
            self.puntaje = 0
            self.opcion = ""
    
        def elegir_opcion(self,opcion):
            self.opcion = opcion
            print("Elegiste: ", self.opcion)
    
        def sumar_punto(self):
            self.puntaje += 1
    
    
    class CPU():
        def __init__(self):
            self.nombre = "CPU"
            self.puntaje = 0
            self.opcion = ""
    
        def elegir_opcion(self):
            self.opcion = random.choice(["piedra", "papel", "tijera"])
            print("La opcion de la CPU es: ", self.opcion)
    
        def sumar_punto(self):
            self.puntaje += 1
    
    
    class juego():
        def __init__(self, J1: jugador, CPU: CPU):
            self.J1 = J1
            self.CPU = CPU
            self.termino = False
    
        def is_finished(self):
            return self.termino
    
        def comparar_opciones(self):
            if (self.CPU.opcion == self.J1.opcion):
                print("Empate")
            elif self.CPU.opcion == "piedra" and self.J1.opcion == "papel":
                self.J1.sumar_punto()
            elif self.CPU.opcion == "papel" and self.J1.opcion == "tijera":
                self.J1.sumar_punto()
            elif self.CPU.opcion == "tijera" and self.J1.opcion == "piedra":
                self.J1.sumar_punto()
    
            else:
                self.CPU.sumar_punto()
    
            self.comparar_punto()
    
        def comparar_punto(self):
            if self.J1.puntaje == 3:
                self.termino = not self.termino
                print("El ganador es ", self.J1.nombre)
            elif self.CPU.puntaje == 3:
                self.termino = not self.termino
                print("El ganador es ", self.CPU.nombre)
            else:
                pass
            
            
    jugador_1 = jugador("Esteban")
    
    _CPU = CPU()
    
    juego_PPT = juego(jugador_1, _CPU)
    
    while (not juego_PPT.is_finished()):
        jugador_1.elegir_opcion(input("Elegir piedra papel o tijera: "))
        _CPU.elegir_opcion()
        juego_PPT.comparar_opciones()
    