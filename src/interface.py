from tkinter import *


class Interface:
    @classmethod
    def start(cls):
        raiz = Tk()

        cls._frame_ = Frame()
        menu = Menu(raiz)
        raiz.config(menu=menu)
        raiz.config(width="650", height="400")
        subMenu = Menu(menu)
        menu.add_cascade(label="Calculos", menu=subMenu)
        subMenu.add_command(label="EDT", command=cls.edt)
        subMenu.add_command(label="OB", command=cls.ob)
        subMenu.add_command(label="OA", command=cls.oa)
        subMenu.add_command(label="SF", command=cls.sf)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=raiz.destroy)
        textoMain = Label(raiz, text="TP MATEMATICA SUPERIOR"'\n' '\n' "GRUPO MIXTO 2", font=("Calibri", 20))
        textoMain.place(x=100, y=0)

        raiz.mainloop()

    @classmethod
    def set_frame(cls):
        cls._frame_.destroy()
        cls._frame_ = Frame()
        cls._frame_.pack()
        cls._frame_.config(bg="beige")
        cls._frame_.config(width="650", height="400")

    @classmethod
    def edt(cls):
        cls.set_frame()
        f = cls._frame_
        titulo = Label(f, text="Ingresar los datos"'\n')  # label y su ubicacion
        titulo.place(x=0, y=0)
        texto = Label(f, text="Numero")
        campo = Entry(f)
        campo.place(x=70, y=25)
        botonEnviar = Button(f, text="Tranformar", command=cls.trans)
        botonEnviar.place(x=30, y=90)

    @classmethod
    def trans(cls):
        cls.set_frame()

    @classmethod
    def ob(cls):
        cls.set_frame()

    @classmethod
    def oa(cls):
        cls.set_frame()

    @classmethod
    def sf(cls):
        None


Interface.start()
