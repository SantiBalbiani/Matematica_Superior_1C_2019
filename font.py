
from tkinter import *
from tkinter import ttk

def trans():
    print("Estoy transformando")

def calcular():
    f = Frame()
    f.pack()
    f.config(bg = "beige")
    f.config(width = "650", height = "400")
    texto1 = Label(f,text = "Ingresar los datos"'\n') #label y su ubicacion
    texto1.place(x=0,y=0)
    textoPolar = Label(f,text = "Polar")
    textoPolar.place(x=10,y=25)
    campoP = Entry(f)
    campoP.place(x = 70, y = 25)
    textoBin = Label(f,text = "Binomica")
    textoBin.place(x=10,y=55)
    campoB = Entry(f)
    campoB.place(x=70,y=55)
    botonEnviar = Button(f,text = "Tranformar", command=trans)
    botonEnviar.place(x = 30, y = 90)
    resultado = Label(f,text = "La transfomacion es:")
    resultado.place(x=10, y =130)

raiz = Tk()

menu = Menu(raiz)
raiz.config(menu=menu)
raiz.config(width = "650", height = "400")
subMenu = Menu(menu)
menu.add_cascade(label = "Calculos", menu = subMenu)
subMenu.add_command(label = "EDT",command=calcular)
subMenu.add_command(label = "OB",command=calcular)
subMenu.add_command(label = "OA",command=calcular)
subMenu.add_command(label = "SF",command=calcular)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command=raiz.destroy)
textoMain = Label(raiz,text = "TP MATEMATICA SUPERIOR"'\n' '\n' "GRUPO 2" ,font=("Calibri",20))
textoMain.place(x=100, y=0)

raiz.mainloop()
