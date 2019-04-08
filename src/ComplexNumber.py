from cmath import *

FULL_ROUND = pi * 2

#Error esperado de conversion: 1%
#(En realidad creo que es bastante menos, pero yo me considero feliz con 1%)

#Estuve vago y por eso tengo coordenadas cart. en lugar de _real y _imaginary,
#pero mi idea era usar esos para calcularlos lazy por separado


class ComplexNumber:
    _rect = None
    _abs = None
    _pi_mult = None
    _phase = None
    _saved_as = None

    def __init__(self, a, b, form):
        self._saved_as = form
        if form == 1:
            self._rect = complex(a, b)
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
            return "(" + str(self._rect.real) + ", " + str(self._rect.imag) + ")"
        elif self._saved_as == 2:
            return "[" + str(self._abs) + ", " + str(self._pi_mult) + "π]"
        else:
            return "[" + str(self._abs) + ", " + str(self._phase) + "]"

    #Getter, se asignan de manera lazy excepto pi_mult, porque no hay manera de calcularlo si no te lo dan de una
    def real(self):
        if self._rect is None:
            self._set_rect()
        return self._rect.real

    def imaginary(self):
        if self._rect is None:
            self._set_rect()
        return self._rect.imag

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
        self._abs = abs(self._rect)

    def _set_phase(self):
        if self._pi_mult is None:
            self._phase = phase(self._rect)
            # Python devuelve el angulo con valores entre [0, pi] si el valor imaginario es positivo
            # y entre [-pi, 0] si es negativo, este if lo modifica para que siempre en la primera vuelta +
            if self._phase < 0:
                self._phase += FULL_ROUND
        else:
            self._phase = self._pi_mult * pi

    def _set_rect(self):
        self._rect = rect(self.abs(), self.phase())
