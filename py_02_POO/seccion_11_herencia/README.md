# Herencia en Python

## Herencia en Python

**Introducción:**

La herencia en Python es un mecanismo que permite a una clase **heredar** los atributos y métodos de otra clase. La clase que hereda se llama **clase hija** o **subclase**, y la clase de la que se hereda se llama **clase padre** o **superclase**.

**¿Qué es?**

En términos más simples, la herencia te permite crear clases que **reutilizan** código de otras clases. Esto te ayuda a evitar la duplicación de código y a crear una estructura de clases más organizada.

**¿Para qué sirve?**

La herencia sirve para:

* **Reutilizar código:** Puedes evitar escribir el mismo código una y otra vez para diferentes clases.
* **Organizar el código:** Puedes crear una estructura de clases más organizada y fácil de entender.
* **Extender la funcionalidad:** Puedes agregar nuevas funcionalidades a una clase existente.

**¿Cómo usarla?**

Para usar la herencia en Python, se utiliza la palabra clave `class`. La sintaxis básica es la siguiente:

```python
class ClaseHija(ClasePadre):

    # Atributos y métodos de la clase hija

```

En este ejemplo, la clase `ClaseHija` hereda de la clase `ClasePadre`. La clase `ClaseHija` puede tener sus propios atributos y métodos, además de los que hereda de la clase `ClasePadre`.

**Ejemplo:**

```python
class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

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

En este ejemplo, las clases `Perro` y `Gato` heredan de la clase `Animal`. La clase `Animal` tiene un método `hablar` que es abstracto (no tiene una implementación). Las clases `Perro` y `Gato` implementan el método `hablar` de forma diferente.

**Tipos de Herencia:**

* **Herencia simple:** Una clase hereda de una sola clase padre.
* **Herencia múltiple:** Una clase hereda de dos o más clases padre.
* **Herencia jerárquica:** Una clase padre tiene una o más clases hijas.

**Recursos adicionales:**

* Herencia en Python - El libro de Python: [https://ellibrodepython.com/herencia-en-python](https://ellibrodepython.com/herencia-en-python)
* Herencia y polimorfismo en Python - Apuntes de Python: [https://apuntes.de/python/herencia-y-polimorfismo-en-python-amplia-la-flexibilidad-de-tus-clases/](https://apuntes.de/python/herencia-y-polimorfismo-en-python-amplia-la-flexibilidad-de-tus-clases/)
* Herencia en Python: [https://m.youtube.com/watch?v=uMfxoErGUS8](https://m.youtube.com/watch?v=uMfxoErGUS8)
