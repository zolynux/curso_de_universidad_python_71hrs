class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    # Méotodos de instancia
    # Método a mostrar Detalle
    def mostrar_detalle(self):
        print(
            f"Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}"
        )


persona1 = Persona("Juan", "Perez", 28, "345343453", 2, 3, 5, m="manzana", p="pera")
persona1.mostrar_detalle()

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrar_detalle()
