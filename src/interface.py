from tkinter import *
import tkinter.ttk as tkk
from src.ToComplex import *
from src.ComplexNumber import *
from src.FasoresChecks import *
from PIL import ImageTk, Image

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
        raiz.config(width="650", height="400", bg='white')
        subMenu = Menu(menu)
        menu.add_cascade(label="Calculos", menu=subMenu)
        subMenu.add_command(label="EDT", command=cls.edt)
        subMenu.add_command(label="OB", command=cls.ob)
        subMenu.add_command(label="OA", command=cls.oa)
        subMenu.add_command(label="SF", command=cls.sf)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=raiz.destroy)
        textoMain = Label(raiz, text="Trabajo Práctico Matemática Superior"'\n' '\n' "Operaciones con Nros Complejos" '\n' "Grupo Mixto 2", font=("Arial, 25"))
        textoMain.config(bg='white')
        textoMain.place(x=325, y=250, anchor="center")
        
        
        imagen = Image.open("logo_utn.ico")
        ph = ImageTk.PhotoImage(imagen)
        panel = Label(raiz, image = ph)
        panel.image=ph
        panel.pack(side = "bottom", fill = "both", expand = "no")
        panel.place(x=325, y=30, anchor="n")
        raiz.mainloop()

    @classmethod
    def set_frame(cls):
        cls._frame_.destroy()
        cls._frame_ = Frame()
        cls._frame_.pack()
        cls._frame_.config(bg="beige")
        cls._frame_.config(width="650", height="500")

    @classmethod
    def edt(cls):
        cls.set_frame()
        f = cls._frame_
        titulo = Label(f, text="Ingrese en el cuadro de texto al número complejo que desea transformar:"'\n', font=("Arial, 14"))  # label y su ubicacion
        titulo.place(x=15, y=25)
        titulo.config(font=("Arial", 12), bg='beige')
        texto = Label(f, text="Número:" , font=("Arial, 12"))
        texto.place(x=180,y=90)
        texto.config(bg='beige')
        cls._complex1_ = Entry(f)
        cls._complex1_.place(x=325, y=100, anchor="center")
        botonEnviar = Button(f, text="Transformar", font=("Arial, 16"), command=cls.trans)
        botonEnviar.place(x=250, y=150)
        cls._result_label_ = Label(f, text="", font=("Arial, 18"))
        cls._result_label_.place(x=80, y=220)

    @classmethod
    def trans(cls):
        complex_s = cls._complex1_.get()
        try:
            complex = to_complex(complex_s)
            result_text = "Resultado = " + str(complex.str_change_form())
            cls._result_label_.config(bg="beige", fg="black")
        except InvalidSintaxError:
            result_text = "El formato de ingreso no es valido"
            cls._result_label_.config(bg="red", fg="white")
        
        cls._result_label_.config(text=result_text)


    @classmethod
    def ob(cls):
        cls.set_frame()
        f = cls._frame_
        titulo = Label(f, text="Operaciones Básicas"'\n')  # label y su ubicacion
        titulo.place(x=0, y=0)
        titulo.config(font=("Arial", 16), bg='beige')
        texto1 = Label(f, text="Numero 1: ")
        texto1.place(x=0, y=25)
        texto1.config(bg="beige")
        cls._complex1_ = Entry(f)
        cls._complex1_.place(x=70, y=25)        
        texto2 = Label(f, text="Numero 2: ")
        texto2.place(x=0, y=50)
        texto2.config(bg="beige")
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
        titulo.config(font=("Arial", 16), bg='beige')
        texto1 = Label(f, text="Numero: ")
        texto1.place(x=0, y=25)
        texto1.config(bg="beige")
        cls._complex_ = Entry(f)
        cls._complex_.place(x=70, y=25)        
        texto2 = Label(f, text="Exponente: ")
        texto2.place(x=0, y=50)
        texto2.config(bg="beige")
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
        cls.set_frame()
        f = cls._frame_
        titulo = Label(f, text="Suma de fasores"'\n')
        titulo.place(x=0, y=0)
        titulo.config(font=("Arial", 16), bg='beige')
        
        texto1 = Label(f, text="Funcion A: ")
        texto1.place(x=0, y=25)
        texto1.config(bg='beige')
        
        cls._amplitudA_ = Entry(f)
        cls._amplitudA_.place(x=70, y=25)
        cls._amplitudA_.config(width=5)
        
        cls._funcionA_ = tkk.Combobox(f, state="readonly", width=4)
        cls._funcionA_["values"] = ["SIN", "COS"]
        cls._funcionA_.set("SIN")
        cls._funcionA_.place(x=110, y=25)
        
        parentesis7 = Label(f, text="(")
        parentesis7.place(x=155, y=25)
        parentesis7.config(font=("Courier", 10), bg='beige')
        
        cls._frecuenciaA_ = Entry(f)
        cls._frecuenciaA_.place(x=170, y=25)
        cls._frecuenciaA_.config(width=5)
        
        parentesis6 = Label(f, text=" t + ")
        parentesis6.place(x=205, y=25)
        parentesis6.config(font=("Courier", 10), bg='beige')
        
        cls._corrimientoA_ = Entry(f)
        cls._corrimientoA_.place(x=255, y=25)
        cls._corrimientoA_.config(width=5)

        parentesis6 = Label(f, text=")")
        parentesis6.place(x=280, y=25)
        parentesis6.config(font=("Courier", 10), bg='beige')
        
        # Segunda función
        texto2 = Label(f, text="Funcion B: ")
        texto2.place(x=0, y=50)
        texto2.config(bg='beige')
        cls._amplitudB_ = Entry(f)
        cls._amplitudB_.place(x=70, y=50)
        cls._amplitudB_.config(width=5)
        
        cls._funcionB_ = tkk.Combobox(f, state="readonly", width=4)
        cls._funcionB_["values"] = ["SIN", "COS"]
        cls._funcionB_.set("SIN")
        cls._funcionB_.place(x=110, y=50)
        
        parentesis3 = Label(f, text="(")
        parentesis3.place(x=155, y=50)
        parentesis3.config(font=("Courier", 10), bg='beige')
        
        cls._frecuenciaB_ = Entry(f)
        cls._frecuenciaB_.place(x=170, y=50)
        cls._frecuenciaB_.config(width=5)
        
        parentesis4 = Label(f, text=" t + ")
        parentesis4.place(x=205, y=50)
        parentesis4.config(font=("Courier", 10), bg='beige')
        
        cls._corrimientoB_ = Entry(f)
        cls._corrimientoB_.place(x=255, y=50)
        cls._corrimientoB_.config(width=5)
        
        parentesis5 = Label(f, text=")")
        parentesis5.place(x=280, y=50)
        parentesis5.config(font=("Courier", 10), bg='beige')
        
        
        boton = Button(f, text="Sumar", command=cls.sumaFasores)
        boton.place(x=0, y=70)
        cls._result_label_ = Label(f, text="")
        cls._result_label_.place(x=30, y=120)

    @classmethod
    def sumaFasores(cls):
        try:
           
            fasorA = to_fasor(cls._amplitudA_.get(), cls._corrimientoA_.get())
            fasorB = to_fasor(cls._amplitudB_.get(), cls._corrimientoB_.get())
            frecuenciaA = to_frecuencia(cls._frecuenciaA_.get())
            frecuenciaB = to_frecuencia(cls._frecuenciaB_.get())
            tipoA = to_tipo(cls._funcionA_.current()+1)
            tipoB = to_tipo(cls._funcionB_.current()+1)
            funcionA = TrigonometricFunction(tipoA, frecuenciaA, fasorA)
            funcionB = TrigonometricFunction(tipoB, frecuenciaB, fasorB)
            result_text = "Resultado = " + str(funcionA.sumar_fasores(funcionB))
            l = Label(text='Hello world')
        except InvalidSintaxError:
            result_text = "Los numeros ingresados no son numero validos"
        except FrecuenciaDiferenteException:
            result_text = "Las funciones no tienen misma frecuencia"

        cls._result_label_.config(text=result_text)
