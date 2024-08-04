## Diseño de clases en Python

El diseño de clases es un proceso fundamental en la programación orientada a objetos (POO) en Python. Implica definir la estructura y el comportamiento de una clase, que es un modelo que representa un tipo de objeto en el mundo real.

**Componentes de una clase:**

* **Nombre:** Debe ser descriptivo y seguir las convenciones de nomenclatura de Python.
* **Atributos:** Representan las características o propiedades del objeto. Pueden ser públicos, privados o protegidos.
* **Métodos:** Representan las acciones que el objeto puede realizar.
* **Constructor:** Es un método especial que se ejecuta al crear una nueva instancia de la clase.
* **Destructor:** Es un método especial que se ejecuta al eliminar una instancia de la clase.

**Principios de diseño de clases:**

* **Encapsulamiento:** Ocultar los detalles de implementación de la clase y solo exponer una interfaz pública.
* **Reutilización:** Diseñar clases que se puedan reutilizar en diferentes programas.
* **Modularidad:** Dividir la clase en unidades más pequeñas y manejables.
* **Herencia:** Permitir que una clase herede de otra clase para reutilizar código y comportamiento.
* **Polimorfismo:** Permitir que diferentes clases respondan al mismo mensaje de diferentes maneras.

**Beneficios del diseño de clases:**

* **Mejora la organización del código.**
* **Facilita la reutilización del código.**
* **Hace que el código sea más fácil de entender y mantener.**
* **Permite crear aplicaciones más robustas y escalables.**

**Recursos adicionales:**

* Tutorial de Python: [https://docs.python.org/es/3/tutorial/](https://docs.python.org/es/3/tutorial/)

**Ejemplos de diseño de clases:**

* **Clase Persona:**

```python
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def __str__(self):
        return f"Persona [{self.nombre} {self.edad}]"

persona1 = Persona("Juan", 28)
persona2 = Persona("Karla", 30)

print(persona1)
print(persona2)

persona1.saludar()
persona2.saludar()
```

* **Clase Animal:**

```python
class Animal:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hablar(self):
        raise NotImplementedError

class Perro(Animal):

    def hablar(self):
        print("Guau!")

class Gato(Animal):

    def hablar(self):
        print("Miau!")

perro = Perro("Toby")
gato = Gato("Michi")

perro.hablar()
gato.hablar()
```

**En resumen:**

El diseño de clases es una parte importante de la programación en Python. Se pueden usar para crear clases reutilizables, modulares y extensibles.
