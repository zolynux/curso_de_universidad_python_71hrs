class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


# print(type(Persona))
persona1 = Persona("Juan", "Perez", 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
