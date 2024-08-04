class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método de instancia
    def calcular_area(self):
        return self.base * self.altura


base = int(input("Proporciona la base del rectangulo: "))
altura = int(input("Proporciona la altura del rectangulo: "))

rectangulo1 = Rectangulo(base, altura)
print(
    f"Área Rectángulo: {rectangulo1.base} x {rectangulo1.altura} es {rectangulo1.calcular_area()}"
)

base = int(input("Proporciona la base del rectangulo: "))
altura = int(input("Proporciona la altura del rectangulo: "))

rectangulo2 = Rectangulo(base, altura)
print(
    f"Área Rectángulo: {rectangulo2.base} x {rectangulo2.altura} = {rectangulo2.calcular_area()}"
)
