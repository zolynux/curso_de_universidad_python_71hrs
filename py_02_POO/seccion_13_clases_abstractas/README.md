# Clases abstractas en Python 🐍

**Clases abstractas** en Python son una herramienta importante en la **programación orientada a objetos**. Permíteme
explicarte cómo funcionan y cómo puedes utilizarlas.

1. **¿Qué son las clases abstractas?**
    - Una **clase abstracta** es un modelo para otras clases relacionadas.
    - No se puede crear una instancia directamente de una clase abstracta, pero solo se puede acceder a ella a través de
      la herencia.
    - Las clases abstractas proporcionan una **interfaz** para las subclases derivadas, evitando así la duplicación de
      código.

2. **¿Por qué usar clases abstractas?**
    - En ocasiones, queremos definir una clase que contenga métodos que **deben ser implementados por las subclases**.
    - Las clases abstractas nos permiten establecer un **contrato** entre la clase base y sus subclases.

3. **Creando clases abstractas en Python:**
    - Python no tiene clases abstractas de forma nativa, pero podemos utilizar el módulo `abc` (Abstract Base Classes)
      para definirlas.
    - Aquí tienes un ejemplo práctico:

```python
import abc
from abc import ABC


class Animal(ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def set_name(self, name):
        """Asigna un nombre al animal."""
        self.name = name

    @abc.abstractmethod
    def get_name(self):
        """Retorna el nombre del animal."""
        return self.name


# Ejemplo de uso
class Perro(Animal):
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return f"¡Guau! Soy {self.name}."


mi_perro = Perro()
mi_perro.set_name("Firulais")
print(mi_perro.get_name())  # Salida: ¡Guau! Soy Firulais.
```

En este ejemplo:

- `Animal` es una clase abstracta con dos métodos abstractos: `set_name` y `get_name`.
- La clase `Perro` hereda de `Animal` e implementa los métodos abstractos.

4. **Resumen:**
    - Las clases abstractas nos ayudan a definir una estructura común y aseguran que las subclases cumplan con ciertos
      requisitos.
    - Utiliza el módulo `abc` para crear clases abstractas en Python.

Claro, **`ABC`** y **`abstractmethod`** son dos elementos importantes del módulo **`abc`** (Abstract Base Classes) en Python. Permíteme explicarte su función:

1. **`ABC` (Abstract Base Class)**:
   - La clase **`ABC`** es una **clase abstracta** proporcionada por el módulo `abc`.
   - Se utiliza como base para definir otras clases abstractas.
   - No se puede crear una instancia directamente de una clase que hereda de **`ABC`**.
   - Su principal función es establecer una **interfaz común** para las subclases.

2. **`abstractmethod`**:
   - El **decorador `abstractmethod`** se utiliza para **definir métodos abstractos** en una clase.
   - Un método abstracto es aquel que **debe ser implementado por las subclases**.
   - Al utilizar este decorador, estamos estableciendo un **contrato** entre la clase base y sus subclases.
   - Ejemplo de uso:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        """Método abstracto para hacer un sonido."""
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Crear objetos
mi_perro = Perro()
mi_gato = Gato()

print(mi_perro.hacer_sonido())  # Salida: ¡Guau!
print(mi_gato.hacer_sonido())   # Salida: ¡Miau!
```

3. **Resumen**:
   - **`ABC`** proporciona una base para crear clases abstractas.
   - **`abstractmethod`** define métodos abstractos que deben ser implementados por las subclases.
   - Juntos, nos permiten crear una jerarquía de clases con una estructura clara y coherente.

[Documentación oficial de Python - Módulo `abc`](https://docs.python.org/3/library/abc.html)

[Real Python - Python's property(): Add Managed Attributes to Your Classes](https://realpython.com/python-property/)

[Programiz - Python @property Decorator (With Examples)](https://www.programiz.com/python-programming/property)

[Mi Diario Python - Clases Abstractas - Ejemplos Prácticos con Python y ABC](https://pythondiario.com/2018/08/clases-abstractas-ejemplos-practicos.html)

[Education Wiki - Clase abstracta en Python](https://es.education-wiki.com/5967155-abstract-class-in-python)

[Analytics Lane - Clases abstractas en Python](https://www.analyticslane.com/2020/10/05/clases-abstractas-en-python/)

[Tecnoloco - Clases abstractas en Python: una guía para principiantes](https://tecnoloco.istocks.club/clases-abstractas-en-python-una-guia-para-principiantes/2021-09-12/)