class Persona:
    # * El profundizanod en la programación Orientada a Objetos en Python
    # * Atritubos de clases y objetos en PYthon
    contandor_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Mostrar los atributos de un objeto
persona1 = Persona("Juan", "Perez")
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contandor_personas)  # Accediento al atributo de clase
#! Pero no es posible modificado con el objeto, sino con la clase
persona1.contandor_personas = 10
print(persona1.__dict__)
# * El atributo anterior oculta al atributo de clase
print(Persona.contandor_personas)  # Atributo clase
print(persona1.contandor_personas)  # Atributo del objeto 1

# Un segundo objeto
persona2 = Persona("Karla", "Gomez")
print(persona2.__dict__)
print(persona2.contandor_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)

"""
Este nuevo atributo de clase se puede acceder ahora
desde los objetos, persona1.contador2 y persona2.contador2

Recordar que los atributos de clase se comparten con todos los objetos creados de dicha clase
"""
