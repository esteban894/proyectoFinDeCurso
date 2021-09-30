from random import randrange
from colorama import Fore, init

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
