from cmath import *

FULL_ROUND = pi * 2

#Error esperado de conversion: 1%

#Estuve vago y por eso tengo coordenadas cart. en lugar de _real y _imaginary,
#pero mi idea era usar esos para calcularlos lazy por separado

#To Do:
#   Cambiar exception genericas por especificas
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

    @classmethod
    def binomial(cls, real_part, imaginary_part):
        return cls(real_part, imaginary_part, 1)

    @classmethod
    def polar_with_pi(cls, module, pi_mult):
        if 0 > pi_mult or pi_mult >= 2:
            pi_mult %= 2
        return cls(module, pi_mult, 2)

    @classmethod
    def polar_with_decimal(cls, abs, phase):

        if 0 > phase or phase >= FULL_ROUND:
            phase %= FULL_ROUND
        return cls(abs, phase, 3)

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

    def _set_abs(self):
        self._abs = abs(self._rect)

    def _set_phase(self):
        if self._pi_mult is None:
            if self._rect.imag > 0:
                self._phase = phase(self._rect)
            else:
                self._phase = phase(self._rect) + FULL_ROUND
        else:
            self._phase = self._pi_mult * pi

    def _set_rect(self):
        self._rect = rect(self.abs(), self.phase())
