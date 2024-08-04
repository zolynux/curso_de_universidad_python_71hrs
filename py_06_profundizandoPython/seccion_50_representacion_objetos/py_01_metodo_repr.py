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

    # * repr, más enfoacod a los programadores
    #
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})"


persona1 = Persona("juan", "Perez")
print(f"Mi objeto persona1: {persona1}")
