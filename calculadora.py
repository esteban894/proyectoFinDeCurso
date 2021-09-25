from tkinter import *

raiz = Tk()
raiz.title("Calculadora")
raiz.config(bg="#7f8c8d")

miFrame = Frame()
miFrame.config(bg="#7f8c8d")
miFrame.pack()

operacion = ""

reset_pantalla = False

resultado = 0

# -----------pantalla-------------

numeroEnPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroEnPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

# ----------pulsaciones teclado-----


def numeroPulsado(num):

    global operacion
    global reset_pantalla

    if reset_pantalla != False:

        numeroEnPantalla.set(num)
        reset_pantalla = False
    else:
        numeroEnPantalla.set(numeroEnPantalla.get() + num)

# ---------funcion suma----------

def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroEnPantalla.set(resultado)

# ----------funcion resta--------

num1 = 0
contador_resta = 0


def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    global num1
    global contador_resta

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)

        numeroEnPantalla.set(resultado)
        resultado = numeroEnPantalla.get()

    contador_resta += 1
    operacion = "resta"
    reset_pantalla = True

# -------------funcion multiplicacion---------------------

contador_mult = 0


def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_mult
    global reset_pantalla

    if contador_mult == 0:
        num1 = int(num)
        resultado = num1

    else:
        if contador_mult == 1:
            resultado = num1*int(num)

        else:
            resultado = int(resultado)*int(num)

        numeroEnPantalla.set(resultado)
        resultado = numeroEnPantalla.get()

    contador_mult += 1
    operacion = "multiplicacion"
    reset_pantalla = True

# -----------------funcion division---------------------

contador_div = 0


def divide(num):
    global operacion
    global resultado
    global num1
    global contador_div
    global reset_pantalla

    if contador_div == 0:
        num1 = float(num)
        resultado = num1

    else:
        if contador_div == 1:
            resultado = num1/float(num)

        else:
            resultado = float(resultado)/float(num)

        numeroEnPantalla.set(resultado)
        resultado = numeroEnPantalla.get()

    contador_div += 1
    operacion = "division"
    reset_pantalla = True

# ----------funcion el_resultdo--

def elResultado():
    global resultado
    global operacion
    global contador_resta
    global contador_mult
    global contador_div

    if operacion == "suma":
        numeroEnPantalla.set(resultado+int(numeroEnPantalla.get()))
        resultado = 0

    elif operacion == "resta":
        numeroEnPantalla.set(int(resultado)-int(numeroEnPantalla.get()))
        resultado = 0
        contador_resta = 0

    elif operacion == "multiplicacion":
        numeroEnPantalla.set(int(resultado)*int(numeroEnPantalla.get()))
        resultado = 0
        contador_mult = 0

    elif operacion == "division":
        numeroEnPantalla.set(int(resultado)/int(numeroEnPantalla.get()))
        resultado = 0
        contador_div = 0

# ----------fila1----------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.config(bg="#95a5a6")
boton7.grid(row=2, column=1, pady=2, padx=2)

boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.config(bg="#95a5a6")
boton8.grid(row=2, column=2, pady=2, padx=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.config(bg="#95a5a6")
boton9.grid(row=2, column=3, pady=2, padx=2)

botonDiv = Button(miFrame, text="/", width=3,
                  command=lambda: divide(numeroEnPantalla.get()))
botonDiv.config(bg="#95a5a6")
botonDiv.grid(row=2, column=4, pady=2, padx=2)

# ----------fila2----------------
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.config(bg="#95a5a6")
boton4.grid(row=3, column=1, pady=2, padx=2)

boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.config(bg="#95a5a6")
boton5.grid(row=3, column=2, pady=2, padx=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.config(bg="#95a5a6")
boton6.grid(row=3, column=3, pady=2, padx=2)

botonMult = Button(miFrame, text="x", width=3,
                   command=lambda: multiplica(numeroEnPantalla.get()))
botonMult.config(bg="#95a5a6")
botonMult.grid(row=3, column=4, pady=2, padx=2)

# ----------fila3----------------
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.config(bg="#95a5a6")
boton1.grid(row=4, column=1, pady=2, padx=2)

boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.config(bg="#95a5a6")
boton2.grid(row=4, column=2, pady=2, padx=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.config(bg="#95a5a6")
boton3.grid(row=4, column=3, pady=2, padx=2)

botonRes = Button(miFrame, text="-", width=3,
                  command=lambda: resta(numeroEnPantalla.get()))
botonRes.config(bg="#95a5a6")
botonRes.grid(row=4, column=4, pady=2, padx=2)

# ----------fila4----------------
botonComa = Button(miFrame, text=",", width=3,
                   command=lambda: numeroPulsado("."))
botonComa.config(bg="#95a5a6")
botonComa.grid(row=5, column=1, pady=2, padx=2)

boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.config(bg="#95a5a6")
boton0.grid(row=5, column=2, pady=2, padx=2)

botonIgual = Button(miFrame, text="=", width=3, command=lambda: elResultado())
botonIgual.config(bg="#95a5a6")
botonIgual.grid(row=5, column=3, pady=2, padx=2)

botonSuma = Button(miFrame, text="+", width=3,
                   command=lambda: suma(numeroEnPantalla.get()))
botonSuma.config(bg="#95a5a6")
botonSuma.grid(row=5, column=4, pady=2, padx=2)


raiz.mainloop()
