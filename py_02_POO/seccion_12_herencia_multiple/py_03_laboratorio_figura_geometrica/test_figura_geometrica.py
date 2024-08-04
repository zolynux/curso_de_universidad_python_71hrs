from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, "Rojo")
print(f"Calcula área cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

rectangulo1 = Rectangulo(3, 8, "verde")
print(f"Cálculo área rectángulo: {rectangulo1.calcular_area()}")
print(rectangulo1)
