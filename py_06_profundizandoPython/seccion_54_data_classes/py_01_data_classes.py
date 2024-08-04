# * Data Classes en Python
# * Data Classes en Python - Parte 1
from dataclasses import dataclass
from typing import ClassVar


# * End - Parte 1

# * Data Classes en Python - Parte 2


@dataclass
class Domicilio:
    calle: str
    numero: int = 0


# frozen = congelado (No modificable o la mutable)
@dataclass(eq=True, frozen=True)
# * End - Parte 2
# * Data Classes en Python - Parte 1
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f"Valor nombre vacío: {self.nombre}")


# * End - Parte 1
# * Data Classes en Python - Parte 2
domicilio1 = Domicilio("Saturno", 15)
# * End - Parte 2
# * Data Classes en Python - Parte 1
persona1 = Persona("Juan", "Perez", domicilio1)
print(f"{persona1!r}")
# Variable de clase
print(f"Variable clase: {Persona.contador_personas}")
# Variables de instancia
print(f"Variables de instancia: {persona1.__dict__}")
# Variable con valores vacíos
persona_vacia = Persona("Karla", "", None)
print(f"Persona vacía: {persona_vacia}")
# * End - Parte 1
# * Data Classes en Python - Parte 2
# Revisamos igualdad entre objetos (__eq__)
persona2 = Persona("Juan", "Perez", Domicilio("Saturno", 15))
print(f"Objetos iguales? {persona1 == persona2}")
# Agregar esta clase a una colecciones
coleccion = {persona1, persona2}
print(coleccion)
# * Frozen = True
# ! Arroja un error en el TypeError: 'set' object is not subscriptable
# coleccion[0].nombre = "Juan Carlos"
# ! No se pueden modificar o que son elementos inmutables.
# persona1.nombre = 'Juan Carlos'

# * End - Parte 2
