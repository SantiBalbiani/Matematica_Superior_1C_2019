
from tkinter import *
from tkinter import ttk

def trans():
    print("Estoy transformando")

def calcular():
    # Capaz estaria bueno que el frame se lo pase
    # por parametro o "var. global" así el manejo
    # principal de la GUI puede controlar la creación
    # y borrado (para evitar que el bug de que se van
    # empujando)
    # [MATI]
    f = Frame()
    f.pack()
    f.config(bg="beige")
    f.config(width="650", height="400")
    texto1 = Label(f, text="Ingresar los datos"'\n') #label y su ubicacion
    texto1.place(x=0, y=0)
    # No hace falta dos espacios de ingreso,
    # si es polar o cartesiano se define
    # con el formato
    # (a;b) <- cartesiano
    # [r;phi] <- polar
    # [MATI]
    textoPolar = Label(f, text="Polar")
    textoPolar.place(x=10, y=25)
    campoP = Entry(f)
    campoP.place(x = 70, y=25)
    textoBin = Label(f, text="Binomica")
    textoBin.place(x=10, y=55)
    campoB = Entry(f)
    campoB.place(x=70, y=55)
    botonEnviar = Button(f, text="Tranformar", command=trans)
    botonEnviar.place(x=30, y=90)
    resultado = Label(f, text="La transfomacion es:")
    resultado.place(x=10, y=130)


raiz = Tk()

menu = Menu(raiz)
raiz.config(menu=menu)
raiz.config(width="650", height="400")
subMenu = Menu(menu)
menu.add_cascade(label="Calculos", menu=subMenu)
# Me gusta esto de que los botones reciban una función.
# Capaz seria mejor que el nombre fuera algo relacionado
# al modulo (tipo edt_gui) y que, o bien ya esten
# apuntando a la función correcta, o a None
# [MATI]
subMenu.add_command(label="EDT", command=calcular)
subMenu.add_command(label="OB", command=calcular)
subMenu.add_command(label="OA", command=calcular)
subMenu.add_command(label="SF", command=calcular)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=raiz.destroy)
textoMain = Label(raiz, text="TP MATEMATICA SUPERIOR"'\n' '\n' "GRUPO MIXTO 2", font=("Calibri", 20))
textoMain.place(x=100, y=0)

raiz.mainloop()
