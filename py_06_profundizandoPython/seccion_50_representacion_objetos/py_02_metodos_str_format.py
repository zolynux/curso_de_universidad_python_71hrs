# Representación de objetos (str, repr, format)
# * Método repre en Python

# print(dir(object))


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    """repr
	* repr, más enfocado a los programadores.
	- La implementación por default de 'str' manda
	a llamar a 'repr'.
	- Por ello se dice que al menos este método
	debemos sboreescribir.
	"""

    # * repr
    # * repr, más enfoacod a los programadores
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})"

    # * str
    # str es más para el usuario final u otros sistemas
    # la implementación por default llama al método repr
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} {self.apellido}"

    # * format
    # format su implementación por default es str
    # se manda a llamar al usar f-string
    def __format__(self, formta_spec):
        return f"{self.__class__.__name__} con nombe {self.nombre} y apellido {self.apellido}"


persona1 = Persona("juan", "Perez")
# * repr (!r)
print(f"Mi objeto persona1: {persona1}")

# * Métodos str y format en Python
# * str (de manera automática el método print llama al método str)
print(persona1)

# * format
print(f"{persona1}")
