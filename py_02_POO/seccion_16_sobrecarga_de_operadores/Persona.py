class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método suma
    def __add__(self, otro):
        #            obj1           obj2
        return f"{self.nombre} {otro.nombre}"

    # Método resta
    def __sub__(self, otro):
        return self.edad - otro.edad


""" Por ejemplo.
# obj
obj1 + obj2
obj1.__add__(obj2)
"""

persona1 = Persona("Juan", 28)
persona2 = Persona("Carlos", 20)
print(persona1 + persona2)
print(persona1 - persona2)
