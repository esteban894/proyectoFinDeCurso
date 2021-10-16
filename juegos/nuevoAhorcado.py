import random
import os
from getpass import getpass
from colorama import Fore, init

def run():

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

      letra = input(Fore.BLUE + "Adivina una letra: " + Fore.RESET).lower()[0]
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

              


if __name__ == "__main__":
    run()