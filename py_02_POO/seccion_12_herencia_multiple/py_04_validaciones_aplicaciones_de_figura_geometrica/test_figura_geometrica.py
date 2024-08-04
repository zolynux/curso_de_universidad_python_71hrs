from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creación Objeto Cuadrado".center(50, "="))
cuadrado1 = Cuadrado(lado=-5, color="Rojo")
cuadrado1.alto = -2
print(f"Calcula área cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

print("Creación Objeto Rectángulo".center(50, "="))
rectangulo1 = Rectangulo(ancho=13, alto=8, color="verde")
rectangulo1.ancho = 15
print(f"Cálculo área rectángulo: {rectangulo1.calcular_area()}")
print(rectangulo1)
