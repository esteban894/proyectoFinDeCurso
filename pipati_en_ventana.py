from tkinter import *

raizP = Tk()
raizP.title("Piedra papel o tijera")
raizP.iconbitmap("chimuelo_icon.ico")
raizP.geometry("400x300")
raizP.resizable(0, 0)

frameP = Frame(raizP)
frameP.pack(fill= "both", expand= 1)

#piedra papel o tijera
imagen2 = PhotoImage(file= "img/Mojito.png")
fondo2 = Label(frameP, image= imagen2)
fondo2.place(x= 0, y= 0, relwidth= 1, relheight= 1)



raizP.mainloop()