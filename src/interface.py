from tkinter import *
from src.ToComplex import *
from src.ComplexNumber import *


class Interface:
    @classmethod
    def start(cls):
        raiz = Tk()

        cls._frame_ = Frame()
        cls._complex1_ = None
        cls._complex2_ = None
        cls._result_label_ = None
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
        cls._complex1_ = Entry(f)
        cls._complex1_.place(x=70, y=25)
        botonEnviar = Button(f, text="Tranformar", command=cls.trans)
        botonEnviar.place(x=30, y=90)
        cls._result_label_ = Label(f, text="")
        cls._result_label_.place(x=10, y=130)

    @classmethod
    def trans(cls):
        complex_s = cls._complex1_.get()
        try:
            complex = to_complex(complex_s)
            result_text = "Resultado = " + str(complex.str_change_form())
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"
        cls._result_label_.config(text=result_text)


    @classmethod
    def ob(cls):
        cls.set_frame()
        f = cls._frame_
        titulo = Label(f, text="Operaciones Básicas"'\n')  # label y su ubicacion
        titulo.place(x=0, y=0)
        texto1 = Label(f, text="Numero 1: ")
        texto1.place(x=0, y=25)
        cls._complex1_ = Entry(f)
        cls._complex1_.place(x=70, y=25)        
        texto2 = Label(f, text="Numero 2: ")
        texto2.place(x=0, y=50)
        cls._complex2_ = Entry(f)
        cls._complex2_.place(x=70, y=50)
        botonSumar = Button(f, text="Sumar", command=cls.sumar)
        botonSumar.place(x=30, y=90)
        botonRestar = Button(f, text="Restar", command=cls.restar)
        botonRestar.place(x=100, y=90)        
        botonMul = Button(f, text="Multiplicar", command=cls.multiplicar)
        botonMul.place(x=170, y=90)        
        botonDiv = Button(f, text="Dividir", command=cls.dividir)
        botonDiv.place(x=280, y=90)        
        cls._result_label_ = Label(f, text="")
        cls._result_label_.place(x=30, y=120)
        
    @classmethod
    def sumar(cls):
        complex_s1 = cls._complex1_.get()
        complex_s2 = cls._complex2_.get()
        try:
            c1 = to_complex(complex_s1)
            c2 = to_complex(complex_s2)
            c3 = c1 + c2 
            result_text = "Resultado = " + str(c3)
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"
        cls._result_label_.config(text=result_text)
        
    @classmethod
    def restar(cls):
        complex_s1 = cls._complex1_.get()
        complex_s2 = cls._complex2_.get()
        try:
            c1 = to_complex(complex_s1)
            c2 = to_complex(complex_s2)
            c3 = c1 - c2 
            result_text = "Resultado = " + str(c3)
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"
        cls._result_label_.config(text=result_text)
        
    @classmethod
    def multiplicar(cls):
        complex_s1 = cls._complex1_.get()
        complex_s2 = cls._complex2_.get()
        try:
            c1 = to_complex(complex_s1)
            c2 = to_complex(complex_s2)
            c3 = c1 * c2 
            result_text = "Resultado = " + str(c3)
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"
        cls._result_label_.config(text=result_text)

    @classmethod
    def dividir(cls):
        complex_s1 = cls._complex1_.get()
        complex_s2 = cls._complex2_.get()
        try:
            c1 = to_complex(complex_s1)
            c2 = to_complex(complex_s2)
            c3 = c1 / c2 
            result_text = "Resultado = " + str(c3)
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"
        except DivideByZero:
            result_text = "Número 2 no puede ser nulo"
        cls._result_label_.config(text=result_text)

    @classmethod
    def oa(cls):
        cls.set_frame()
        f = cls._frame_
        titulo = Label(f, text="Operaciones Avanzadas"'\n')
        titulo.place(x=0, y=0)
        texto1 = Label(f, text="Numero: ")
        texto1.place(x=0, y=25)
        cls._complex_ = Entry(f)
        cls._complex_.place(x=70, y=25)        
        texto2 = Label(f, text="Exponente: ")
        texto2.place(x=0, y=50)
        cls._natural_ = Entry(f)
        cls._natural_.place(x=70, y=50)
        botonPot = Button(f, text="Potencia", command=cls.potencia)
        botonPot.place(x=30, y=90)
        botonRaiz = Button(f, text="Raiz", command=cls.raiz)
        botonRaiz.place(x=100, y=90)        
        botonRE = Button(f, text="Raices n-ésimas", command=cls.necimas)
        botonRE.place(x=200, y=45)     
        botonRP = Button(f, text="Primitivas n-ésimas", command=cls.necimasunity)
        botonRP.place(x=300, y=45) 
        cls._result_label_ = Label(f, text="")
        cls._result_label_.place(x=30, y=120)
        
    @classmethod
    def potencia(cls):
        complex1 = cls._complex_.get()
        natural = cls._natural_.get()
        try:
            c1 = to_complex(complex1)            
            n = float(natural)
            c2 = c1**n
            result_text = "Resultado = " + str(c2)
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"          
        cls._result_label_.config(text=result_text)        

    @classmethod
    def raiz(cls):
        complex1 = cls._complex_.get()
        natural = cls._natural_.get()
        try:
            c1 = to_complex(complex1)            
            n = int(natural)
            result_text = "Resultado = " + str(c1.n_th_root(n))
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"   
        except ValueError:
            result_text = "El exponente debe ser positivo"   
        cls._result_label_.config(text=result_text)   
        
    @classmethod
    def necimas(cls):
        natural = cls._natural_.get()
        try:            
            n = int(natural)
            result_text = "Resultado = " + str(ComplexNumber.roots_of_unity(n,False)) 
        except ValueError:
            result_text = "El exponente debe ser positivo"   
        cls._result_label_.config(text=result_text)

    @classmethod
    def necimasunity(cls):
        natural = cls._natural_.get()
        try:            
            n = int(natural)
            result_text = "Resultado = " + str(ComplexNumber.roots_of_unity(n,True)) 
        except ValueError:
            result_text = "El exponente debe ser positivo"   
        cls._result_label_.config(text=result_text)              

    @classmethod
    def sf(cls):
        None

