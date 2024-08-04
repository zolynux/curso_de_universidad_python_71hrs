## Contexto estático y dinámico en Python

En Python, el contexto estático y dinámico se refiere al **entorno en el que se ejecuta una función o método**. Este entorno define qué variables y métodos son accesibles desde la función o método.

**Contexto estático:**

* Se define por la clase a la que pertenece la función o método.
* No cambia durante la ejecución del programa.
* Permite acceder a **atributos y métodos de la clase** desde una función o método, incluso si no se está ejecutando en una instancia de la clase.

**Ejemplo:**

```python
class Persona:

    nombre = "Juan"

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

```

En este ejemplo, el método `saludar` tiene acceso al atributo `nombre` de la clase `Persona`, incluso si no se está ejecutando en una instancia de la clase.

**Contexto dinámico:**

* Se define por la instancia de la clase en la que se ejecuta la función o método.
* Puede cambiar durante la ejecución del programa.
* Permite acceder a **atributos y métodos de la instancia** desde una función o método.

**Ejemplo:**

```python
class Persona:

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

persona1 = Persona()
persona1.nombre = "Ana"

persona2 = Persona()
persona2.nombre = "Pedro"

persona1.saludar()  # Imprime "Hola, mi nombre es Ana"
persona2.saludar()  # Imprime "Hola, mi nombre es Pedro"
```

En este ejemplo, el método `saludar` tiene acceso al atributo `nombre` de la instancia en la que se está ejecutando.

**Diferencias:**

| Contexto     | Se define por | Cambia durante la ejecución | Accesibilidad                       |
| ------------ | ------------- | --------------------------- | ----------------------------------- |
| **Estático** | La clase      | No                          | Atributos y métodos de la clase     |
| **Dinámico** | La instancia  | Sí                          | Atributos y métodos de la instancia |

**Ventajas del contexto estático:**

* **Reutilización de código:** Puedes evitar escribir el mismo código una y otra vez para diferentes clases.
* **Organización del código:** Puedes crear una estructura de clases más organizada y fácil de entender.
* **Extender la funcionalidad:** Puedes agregar nuevas funcionalidades a una clase existente.

**Desventajas del contexto estático:**

* **Dificultad de comprensión:** El código puede ser más difícil de entender si no se comprende bien el contexto estático.
* **Acoplamiento fuerte:** Las clases pueden estar demasiado acopladas entre sí, lo que dificulta la modificación del código.

**Ventajas del contexto dinámico:**

* **Flexibilidad:** El código puede ser más flexible y adaptable a diferentes situaciones.
* **Facilidad de comprensión:** El código puede ser más fácil de entender si se comprende el contexto dinámico.

**Desventajas del contexto dinámico:**

* **Dificultad de depuración:** Los errores pueden ser más difíciles de identificar y corregir.
* **Acoplamiento débil:** Las clases pueden estar demasiado desacopladas entre sí, lo que dificulta la reutilización del código.
