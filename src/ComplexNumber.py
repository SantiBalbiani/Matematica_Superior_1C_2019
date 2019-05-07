from math import *

FULL_ROUND = pi * 2

#Error esperado de conversion: 1%
#(En realidad creo que es bastante menos, pero yo me considero feliz con 1%)

class DivideByZero(Exception):
    pass

class ComplexNumber:

    def __init__(self, a, b, form):
        self._saved_as = form
        self._real = None
        self._imag = None
        self._abs = None
        self._pi_mult = None
        self._phase = None
        if form == 1:
            self._real = a
            self._imag = b
        elif form == 2:
            self._abs = a
            self._pi_mult = b
        else:
            self._abs = a
            self._phase = b

#   Factory methods para la creación de instancias, usar estos y no el init
    @classmethod
    def binomial(cls, real_part, imaginary_part):
        return cls(real_part, imaginary_part, 1)

    @classmethod
    def polar_with_pi(cls, module, pi_mult):
        #Si el angulo está fuera del primer giro positivo, lo convierto en su equivalente del primer giro
        #Ej: 2.25 (9/4) se convierte en 0.25 (1/4)
        if 0 > pi_mult or pi_mult >= 2:
            pi_mult %= 2
        return cls(module, pi_mult, 2)

    @classmethod
    def polar_with_decimal(cls, abs, phase):
        # Mismo que con el multiplo de pi, pero incluyendo a pi en el calculo.
        if 0 > phase or phase >= FULL_ROUND:
            phase %= FULL_ROUND
        return cls(abs, phase, 3)
    

    #Funciones internas de python para que se imprima lindo
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self._saved_as == 1:
            return "(" + str(self._real) + ", " + str(self._imag) + ")"
        elif self._saved_as == 2:
            return "[" + str(self._abs) + ", " + str(self._pi_mult) + "π]"
        else:
            return "[" + str(self._abs) + ", " + str(self._phase) + "]"

    #Getter, se asignan de manera lazy excepto pi_mult, porque no hay manera de calcularlo si no te lo dan de una
    def real(self):
        if self._real is None:
            self._set_real()
        return self._real

    def imaginary(self):
        if self._imag is None:
            self._set_imag()
        return self._imag

    def abs(self):
        if self._abs is None:
            self._set_abs()
        return self._abs

    def pi_mult(self):
        return self._pi_mult

    def phase(self):
        if self._phase is None:
            self._set_phase()
        return self._phase

    # Metodos privados para settear los valores de los atributos
    def _set_abs(self):
        self._abs = sqrt(pow(self._real, 2) + pow(self._imag, 2))

    def _set_phase(self):
        if self._pi_mult is None:
            self._phase = atan2(self._imag, self._real)
            # Python devuelve el angulo con valores entre [0, pi] si el valor imaginario es positivo
            # y entre [-pi, 0] si es negativo, este if lo modifica para que siempre en la primera vuelta +
            if self._phase < 0:
                self._phase += FULL_ROUND
        else:
            self._phase = self._pi_mult * pi

    def _set_real(self):
        self._real = self.abs() * cos(self.phase())

    def _set_imag(self):
        self._imag = self.abs() * sin(self.phase())

    # Retorna una string con el formato opuesto al que se creo
    def str_change_form(self):
        if self._saved_as == 1:
            return "[" + str(self.abs()) + ", " + str(self.phase()) + "]"
        else:
            return "(" + str(self.real()) + ", " + str(self.imaginary()) + ")"
            
    def __add__(self, other):
        return ComplexNumber.binomial(self.real()+other.real(), self.imaginary()+other.imaginary())
    
    def __radd__(self, other):
        return ComplexNumber.binomial(self.real()+other.real(), self.imaginary()+other.imaginary())
    
    def __sub__(self, other):
        return ComplexNumber.binomial(self.real()-other.real(), self.imaginary()-other.imaginary())
    
    def __mul__(self, other):
        #Estoy completamente al tanto de que tira un warning por acceder a una variable protegia
        #Despues veo de ponerlo mejor
        #[MATI]
        if self._saved_as == 1 and other._saved_as == 1:
            return ComplexNumber.binomial(
                        self.real()*other.real() - self.imaginary()*other.imaginary(),
                        self.real()*other.imaginary() + self.imaginary()*other.imaginary())
        elif self.pi_mult() is not None and other.pi_mult() is not None:
            return ComplexNumber.polar_with_pi(
                        self.abs()*other.abs(),
                        self.pi_mult()+other.pi_mult())
        else:
            return ComplexNumber.polar_with_decimal(
                        self.abs()*other.abs(),
                        self.phase()+other.phase())
        
    def __truediv__(self, other):
        if self.pi_mult() is not None and other.pi_mult() is not None:
            return ComplexNumber.polar_with_pi(
                        self.abs()/other.abs(),
                        self.pi_mult()-other.pi_mult())
        else:
            return ComplexNumber.polar_with_decimal(
                        self.abs()/other.abs(),
                        self.phase()-other.phase())
