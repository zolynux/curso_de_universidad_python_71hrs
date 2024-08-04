## Contexto estático (de clases) en Python

El contexto estático en Python se refiere al **entorno en el que se ejecuta una función o método**. Este entorno está
definido por la clase a la que pertenece la función o método, y no por la instancia de la clase en la que se ejecuta.

**En otras palabras:**

* Cuando se llama a una función o método desde una clase, el contexto estático es la clase en sí misma.
* Cuando se llama a una función o método desde una instancia de una clase, el contexto estático sigue siendo la clase,
  no la instancia.

**¿Por qué es importante?**

El contexto estático es importante porque te permite acceder a **atributos y métodos de la clase** desde una función o
método, incluso si no se está ejecutando en una instancia de la clase.

**Ejemplo:**

```python
class Persona:
    nombre = "Juan"

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

```

En este ejemplo, el método `saludar` tiene acceso al atributo `nombre` de la clase `Persona`, incluso si no se está
ejecutando en una instancia de la clase.

**¿Cómo usarlo?**

Para usar el contexto estático, puedes usar la palabra clave `self`. `self` hace referencia a la instancia actual de la
clase, pero también se puede usar para acceder a **atributos y métodos de la clase**.

**Ejemplo:**

```python
class Persona:
    nombre = "Juan"

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


persona = Persona()

persona.saludar()  # Imprime "Hola, mi nombre es Juan"

persona.cambiar_nombre("Ana")

persona.saludar()  # Imprime "Hola, mi nombre es Ana"
```

En este ejemplo, el método `cambiar_nombre` modifica el atributo `nombre` de la clase `Persona`, que es accesible a
todas las instancias de la clase.

**Ventajas del contexto estático:**

* **Reutilización de código:** Puedes evitar escribir el mismo código una y otra vez para diferentes clases.
* **Organización del código:** Puedes crear una estructura de clases más organizada y fácil de entender.
* **Extender la funcionalidad:** Puedes agregar nuevas funcionalidades a una clase existente.

**Desventajas del contexto estático:**

* **Dificultad de comprensión:** El código puede ser más difícil de entender si no se comprende bien el contexto
  estático.
* **Acoplamiento fuerte:** Las clases pueden estar demasiado acopladas entre sí, lo que dificulta la modificación del
  código.