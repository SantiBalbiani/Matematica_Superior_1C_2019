from enum import Enum


class TrigType(Enum):
    SIN = 1
    COS = 2


class FrecuenciaDiferenteException(Exception):
    pass


class TrigonometricFunction:
    def __init__(self, tipo, frecuencia, fasor):
        self.tipo = tipo
        self.frecuencia = frecuencia
        self.fasor = fasor

    # Funciones internas de python para que se imprima lindo
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.tipo == TrigType.SIN:
            return str(self.fasor.abs())+"SIN("+str(self.frecuencia)+"t+"+str(self.fasor.phase())+")"
        else:
            return str(self.fasor.abs()) + "COS(" + str(self.frecuencia) + "t+" + str(self.fasor.phase()) + ")"

    def sumar_fasores(self, otra):
        if not otra.misma_frecuencia(self.frecuencia):
            raise FrecuenciaDiferenteException
        if otra.mismo_tipo(self.tipo):
            return TrigonometricFunction(otra.tipo, otra.frecuencia, self.fasor + otra.fasor)
        else:
            return TrigonometricFunction(otra.tipo, otra.frecuencia, self.cambiar_tipo().fasor + otra.fasor)



    def cambiar_tipo(self):
        if self.tipo == TrigType.SIN:
            resultado = TrigonometricFunction(TrigType.COS, self.frecuencia, self.fasor.add_pi(-0.5))
        else:
            resultado = TrigonometricFunction(TrigType.SIN, self.frecuencia, self.fasor.add_pi(0.5))
        return resultado

    def misma_frecuencia(self, otra_frecuencia):
        return self.frecuencia == otra_frecuencia

    def mismo_tipo(self, otro_tipo):
        return self.tipo == otro_tipo