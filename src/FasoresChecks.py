from src.InvalidSintaxError import InvalidSintaxError
from src.ComplexNumber import *
from src.TrigonometricFunction import *


def to_fasor(txt_amp, txt_cor):
    txt_amplitud = txt_amp.replace(" ", "")
    txt_corrimiento = txt_cor.replace(" ", "")
    has_pi = txt_corrimiento.endswith("pi")
    if has_pi:
        txt_corrimiento = txt_corrimiento.replace("pi", "")

    try:
        amplitud = float(txt_amplitud)
        corrimiento = float(txt_corrimiento)
    except ValueError:
        raise InvalidSintaxError

    if has_pi:
        return ComplexNumber.polar_with_pi(amplitud, corrimiento)
    else:
        return ComplexNumber.polar_with_decimal(amplitud, corrimiento)


def to_frecuencia(text):
    try:
        frecuencia = float(text)
    except ValueError:
        raise InvalidSintaxError
    return frecuencia


def to_tipo(posicion):
    return TrigType(posicion)