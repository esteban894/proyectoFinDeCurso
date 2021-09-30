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

ahorcadito()