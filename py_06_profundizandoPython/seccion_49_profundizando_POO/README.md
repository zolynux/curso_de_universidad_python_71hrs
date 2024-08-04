## Profundizando en la Programación Orientada a Objetos en Python

**Introducción:**

La programación orientada a objetos (POO) es un paradigma de programación que se basa en la creación de objetos que encapsulan datos y comportamiento. Es una forma poderosa de organizar y estructurar código complejo, y puede ayudar a mejorar la legibilidad, la modularidad y la reutilización del código.

**Repaso rápido:**

* **Conceptos básicos:** Clases, objetos, atributos, métodos, herencia, polimorfismo.
* **Creación de clases:** Definición de atributos y métodos.
* **Creación de objetos:** Instanciación de clases.
* **Heredando de clases:** Reutilización de código y comportamiento.
* **Polimorfismo:** Redefinición de métodos en clases derivadas.

**Profundizando en los conceptos:**

* **Encapsulamiento:** Ocultar la implementación interna de un objeto y exponer solo una interfaz pública.
* **Abstracción:** Definir clases que representan conceptos generales sin especificar detalles de implementación.
* **Herencia:** Reutilizar código y comportamiento de una clase base en una clase derivada.
* **Polimorfismo:** Permitir que diferentes objetos respondan al mismo mensaje de diferentes maneras.

**Patrones de diseño:**

* **Singleton:** Garantizar que solo exista una instancia de una clase.
* **Factory:** Crear objetos de diferentes tipos de forma genérica.
* **Builder:** Crear objetos complejos paso a paso.
* **Observer:** Notificar a varios objetos cuando cambia el estado de un objeto.

**Ventajas de la POO:**

* **Mejora la legibilidad del código.**
* **Facilita la modularización del código.**
* **Promueve la reutilización del código.**
* **Facilita el mantenimiento del código.**

**Desventajas de la POO:**

* **Puede ser más compleja que la programación procedural.**
* **Puede ser menos eficiente que la programación procedural en algunos casos.**

**Recursos adicionales:**

* Curso de Python para principiantes: [https://learn.microsoft.com/es-es/training/paths/beginner-python/](https://learn.microsoft.com/es-es/training/paths/beginner-python/)

**Profundizando en algunos temas:**

* **Encapsulamiento:** Se pueden utilizar modificadores de acceso (public, private, protected) para controlar el acceso a los atributos y métodos de una clase.
* **Herencia:** Existen diferentes tipos de herencia, como la herencia simple, la herencia múltiple y la herencia jerárquica.
* **Polimorfismo:** Se pueden utilizar dos tipos de polimorfismo, el polimorfismo de sobrecarga y el polimorfismo de subtipo.

**Ejemplos adicionales de uso de la POO:**

* **Simulación de un sistema de inventario:**

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.cantidad})"

class SistemaInventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

sistema_inventario = SistemaInventario()

producto1 = Producto("Manzana", 100, 10)
producto2 = Producto("Naranja", 200, 5)

sistema_inventario.agregar_producto(producto1)
sistema_inventario.agregar_producto(producto2)

sistema_inventario.mostrar_productos()

producto_buscado = sistema_inventario.buscar_producto("Manzana")

if producto_buscado:
    print(f"Producto encontrado: {producto_buscado}")
else:
    print("Producto no encontrado")
```
