# -*- coding: utf-8 -*-
from cmath import *
from math import pi
import tkinter as tk
from src.ComplexNumber import ComplexNumber as cn
import re

regexBinomica = r"\(\s*((\d+(\.\d+)??)\s*,\s*(\d+(\.\d+)??))\s*\)"
regexPolarSinPi = r"\[\s*((\d+(\.\d+)??)\s*,\s*(\d+(\.\d+)??))\s*\]"
regexPolarConPi = r"\[\s*((\d+(\.\d+)??)\s*,\s*((\d+(\.\d+)??)\*\P\i))\s*\]"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nota = tk.Label(self)
        self.nota["text"] = "ingrese los complejos en forma *Binómica* y presione Sumar"
        self.nota.pack(side="top")
        self.ingresoCampo1 = tk.Entry(self)
        self.ingresoCampo1["text"] = "campo1"
        self.ingresoCampo1.pack(side="top")
        self.ingresoCampo2 = tk.Entry(self)
        self.ingresoCampo2["text"] = "campo2"
        self.ingresoCampo2.pack(side="top")
        self.suma = tk.Button(self)
        self.suma["text"] = "Sumar"
        self.suma["command"] = self.realizarOperacion
        self.suma.pack(side="top")
        self.quit = tk.Button(self, text="Salir", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")


    #EXPRESION REGULAR BINOMICA
    #\(\s*((\d+(\.\d+)??)\s*,\s*(\d+(\.\d+)??))\s*\)   -> USAR GROUP 2 Y GROUP 4
    
    #EXPRESION REGULAR POLAR SIN PI FACTOR
    #\[\s*((\d+(\.\d+)??)\s*,\s*(\d+(\.\d+)??))\s*\]   -> USAR GROUP 2 Y GROUP 4
    
     #EXPRESION REGULAR POLAR CON PI FACTOR
    #\[\s*((\d+(\.\d+)??)\s*,\s*((\d+(\.\d+)??)\*\P\i))\s*\]   -> USAR GROUP 2 Y GROUP 5 (SI QUIERO USAR EL PI PARA ALGO GROUP 4)
        
    
    def realizarOperacion(self):
        self.validarEstructuraExternaComplejo(self.ingresoCampo1.get())
        self.validarEstructuraExternaComplejo(self.ingresoCampo2.get())
    #   get_complex_from_entry(self.ingresoCampo1.get())
    #   get_complex_from_entry(self.ingresoCampo2.get())
            
       # suma =  complex(self.ingresoCampo1.get()) + complex(self.ingresoCampo2.get())
       # print(suma)
            
        
    def validarEstructuraExternaComplejo(self,complejoIngresado):
        primerCaracter = complejoIngresado[0]
        ultimoCaracter = complejoIngresado[-1]
        print(primerCaracter)
        print(ultimoCaracter)
        if primerCaracter == "[" and ultimoCaracter == "]":
            print("Forma polar detectada.")
            self.validarComplejoPolar(complejoIngresado)
        elif primerCaracter == "(" and ultimoCaracter == ")":
            print("Forma binómica detectada.")
            self.validarComplejoBinomica(complejoIngresado)
        else:
            print("Formato incorrecto.")
    
  
  
    def validarComplejoBinomica(self,complejoIngresado):
        resultado = re.search(regexBinomica, complejoIngresado)
        parteReal = resultado.group(2)
        parteImaginaria = resultado.group(4)
        print(parteReal)
        print(parteImaginaria)
        instanciaDeComplejo = cn.binomial(float(parteReal), float(parteImaginaria))
        #self.calcularDatosPolar(instanciaDeComplejo)
        
        
        
    def validarComplejoPolar(self,complejoIngresado):
        posesionDeFactorPi = self.contains_pi(complejoIngresado)
        if posesionDeFactorPi:
         resultado = re.search(regexPolarConPi, complejoIngresado)
         modulo = resultado.group(2)
         argumento = resultado.group(4)
         print(modulo)
         print(argumento)
         instanciaDeComplejo = cn.polar_with_decimal(float(modulo), float(argumento) * pi)
         #self.calcularDatosBinomica(instanciaDeComplejo)
        else:
         resultado = re.search(regexPolarSinPi, complejoIngresado)
         modulo = resultado.group(2)
         argumento = resultado.group(4)
         print(modulo)
         print(argumento)
         instanciaDeComplejo = cn.polar_with_decimal(float(modulo), float(argumento))
         #self.calcularDatosBinomica(instanciaDeComplejo)
    
    
    
    def contains_pi(self,complejoEnString): 
        resultado = re.search("Pi", complejoEnString)
        if resultado is not None:
            return True
        else:
            return False
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
