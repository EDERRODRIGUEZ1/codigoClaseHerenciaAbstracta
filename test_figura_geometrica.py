from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

#Instancia de cuadrado
print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado = Cuadrado(-3, 'rojo')
cuadrado.alto = 10
print(f'Calculo area cuadrado: {cuadrado.calcular_area()}')
print(cuadrado)

#Instancia de rectangulo
print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo = Rectangulo(-2, 5, 'Verde')
rectangulo.ancho = 15
print(f'Calculo area rectangulo: {rectangulo.calcular_area()}')
print(rectangulo)

#Method Resolution Order
print(Cuadrado.mro())




