class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Méotodos de instancia
    # Método a mostrar Detalle
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")


persona1 = Persona("Juan", "Perez", 28)
persona1.mostrar_detalle()
persona1.telefono = "3335544"
print(persona1.telefono)
# Persona.mostrar_detalle(persona1)

persona2 = Persona("Karla", "Gomez", 30)
persona2.mostrar_detalle()
print(persona2.telefono)
