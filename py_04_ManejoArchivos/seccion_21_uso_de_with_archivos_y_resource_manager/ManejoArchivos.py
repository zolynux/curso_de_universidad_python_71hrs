class ManejoArchivos:  # Manejo Recursos
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print("Obtenemos el recurso".center(50, "-"))
        self.nombre = open(self.nombre, "r", encoding="utf8")

    # Traceback (traza) = Toda la lista de errores si es que ocurrió alguno
    # La firma del método son los parámetros que debemos agregar, de lo contrario marca error
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_excepcion):
        print("Cerramos el recurso".center(50, "-"))
        if self.nombre:
            self.nombre.close()
