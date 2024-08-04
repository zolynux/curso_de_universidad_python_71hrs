class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    """    
    Python es una herramienta incorporada que 
    simplifica el uso de métodos getter y setter 
    en programación orientada a objetos
    """

    # Método el nombre en GET
    @property
    def nombre(self):
        print("Llamando método get nombre")
        return self._nombre

    # Método el nombre en SET
    @nombre.setter
    def nombre(self, nombre):
        print("Llamando método set nombre")
        self._nombre = nombre

    # Método el apellido en GET
    @property
    def apellido(self):
        return self._apellido

    # Método el apellido en SET
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # Método la edad en GET
    @property
    def edad(self):
        return self._edad

    # Método la edad en SET
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Métodos de instancia
    # Método a mostrar Detalle
    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")

    # Método para eliminar objetos
    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido}")


# Ya no ejecución con aquí
if __name__ == "__main__":
    persona1 = Persona("Juan", "Perez", 28)
    persona1.nombre = "Juan Carlos"
    persona1.apellido = "Lara"
    persona1.edad = 30
    persona1.mostrar_detalle()

    print(__name__)  # Imprimir es 'main' # main = principal
