class Persona:
    def __init__(self, nombre, apellido, edad):
        # Encapsulamiento que puede acceder al atributo
        # como variable de privado con modificado.
        self._nombre = nombre
        # Encapsulamiento que ya no puede acceder al atributo
        # que no pueden modificar al atributo
        # self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Méotodos de instancia
    # Método a mostrar Detalle
    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


persona1 = Persona("Juan", "Perez", 28)
persona1._nombre = "Juan Carlos"
persona1.mostrar_detalle()
