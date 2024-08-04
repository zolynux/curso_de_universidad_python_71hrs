class Persona:
    def __init__(self, nombre, apellido, edad):
        # Get = obtener/recuperar
        # Set = Colocar/modificar
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Méotodo el nombre en Get
    # Python es una herramienta incorporada que simplifica el uso de métodos getter y setter en programación orientada a objetos
    @property
    def nombre(self):
        print("Llamando método get nombre")
        return self._nombre

    # Método el nombre en Set
    # @nombre.setter
    # def nombre(self, nombre):
    #     print('Llamando método set nombre')
    #     self._nombre = nombre

    # Méotodos de instancia
    # Método a mostrar Detalle
    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


persona1 = Persona("Juan", "Perez", 28)
# Debemos evitar son atributos encapsulados
# Método en GET
# print(persona1._nombre)
# print(persona1.nombre)
# Método en SET
persona1.nombre = "Juan Carlos"
print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)
