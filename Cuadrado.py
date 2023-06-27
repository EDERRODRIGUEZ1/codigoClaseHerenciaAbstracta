from Color import Color
from FiguraGeometrica import FiguraGeometrica
class Cuadrado(FiguraGeometrica, Color):
    #inicializacion
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    #metodo de calcular el area
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

