"""
Definir una clase padre llamada Vehículo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehículo.
La clase padre debe tener los siguientes atributos y métodos

Vehículo (Clase Padre):
- Atributos (color, ruedas)
- Métodos (__init__ y __str__)

Coche (Clase hija de vehícula) (Además de los atributos y métodos heredados de Vehículo):
- Atributos (Velocidad (km/hr))
- Métodos (__init__ y __str__)

Bicicleta (Clase hija de vehícula) (Además de los atributos y métodos heredados de Vehículo):
- Atributos (Tipo (urbana/montaña/etc.))
- Métodos (__init__ y __str__)
"""


class Vehiculo:
    def __init__(self, color, rueda):
        self.color = color
        self.rueda = rueda

    def __str__(self):
        return f"Color: {self.color}, Rueda: {str(self.rueda)}"


class Coche(Vehiculo):
    def __init__(self, color, rueda, velocidad):
        super().__init__(color, rueda)
        self.velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()}, Velocidad (km/hr): {str(self.velocidad)}] "


class Bicicleta(Vehiculo):
    def __init__(self, color, rueda, tipo):
        super().__init__(color, rueda)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo (urbana/montaña/etc.): {str(self.tipo)}] "
