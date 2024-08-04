class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    # Método de instancia
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


ancho = int(input("Proporciona el ancho de cubo: "))
alto = int(input("Proporciona el alto de cubo: "))
profundo = int(input("Proporciona el profundo de cubo: "))

cubo1 = Cubo(ancho, alto, profundo)
print(f"Volúmen Cubo: {cubo1.calcular_volumen()}")
