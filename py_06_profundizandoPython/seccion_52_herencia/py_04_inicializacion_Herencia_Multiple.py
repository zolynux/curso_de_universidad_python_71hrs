#
# * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 1
class Clase1:
    def __init__(self):
        print("Clase1.__init__")

    def metodo(self):
        print("Método clase1")


class Clase2(Clase1):
    def __init__(self):
        print("Clase2.__init__")
        # * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 3
        super().__init__()

    def metodo(self):
        print("Método clase2")
        # * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 3
        super().metodo()


class Clase3(Clase1):
    def __init__(self):
        print("Clase3.__init__")
        # * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 3
        super().__init__()

    def metodo(self):
        print("Método clase3")
        # * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 3
        super().metodo()


class Clase4(Clase2, Clase3):
    def metodo(self):
        print("Método clase4")
        # * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 3
        super().metodo()


# * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 2
# Creamos objectos clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)

print()

# MRO
print(Clase4.__mro__)
# Cual método se ejecuta
clase4.metodo()

# * Ejemplo de Inicialización en Herencia Múltiple en Python - Parte 3
