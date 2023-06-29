from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self.alto = 0
            print(f'Valor erroneo alto: {alto}')

    #metodo get
    @property
    def ancho(self):
        return self._ancho

    #metodo set
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')
            self._ancho = 0
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')
            self._alto = 0

    # metodo abstracta
    @abstractmethod
    def calcular_area(self):
        pass

    #imprimir en consola
    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto:{self._alto}]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False #notacion simplificada





