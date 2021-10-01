from tkinter import *
from colorama import Fore,init
from getpass import getpass
#---------raiz---------
raizA = Tk()
raizA.title("Ahorcado")
raizA.iconbitmap("icons/horca.ico")
raizA.geometry("400x300")
raizA.resizable(0, 0)

#---------frame---------
frameA = Frame(raizA)
frameA.pack(fill= "both", expand= 1)

#---------fondo---------
#piedra papel o tijera
imagen3 = PhotoImage(file= "img/BurningOrange.png")
fondo3 = Label(frameA, image= imagen3)
fondo3.place(x= 0, y= 0, relwidth= 1, relheight= 1)

#---------funciones---------

def ahorcadito():

    init()

    oportunidades = 7
    palabraAdivinar = getpass("Ingrese la palabra a adivinar: ").lower()
    adivinado = ["_"]* len(palabraAdivinar)
    
    print(Fore.YELLOW + f"Oportunidades: {oportunidades}" + Fore.RESET)
    while oportunidades > 0:
        print("".join(adivinado))
    
        encontrado = False
        ganado = False
    
        letraValida= False
        while not letraValida:
            letra = input("Ingrese letra: ").lower()[0]
            if not letra.isalpha():
                print(Fore.RED + "Caracter invalido, vuelve a intentar." + Fore.RESET)
            else:
                letraValida = True
    
        for i in range(0,len(palabraAdivinar)):
            if letra == palabraAdivinar[i]:
                adivinado[i] = letra
                encontrado = True
        if not encontrado:
            oportunidades -=1
            print(Fore.YELLOW + f"Letra no encontrada, te quedan {oportunidades} oportunidades" + Fore.RESET)
        if "".join(adivinado) == palabraAdivinar:
            ganado = True
            oportunidades = 0
    
    if ganado:
        print(Fore.GREEN + f"Ganaste!\nLa palabra era {palabraAdivinar}" + Fore.RESET)
    else:
        print(Fore.RED + f"Perdiste!\nLa palabra era {palabraAdivinar}" + Fore.RESET)

boton = Button(frameA, text="Jugar", command=lambda:ahorcadito())
boton.pack()

raizA.mainloop()