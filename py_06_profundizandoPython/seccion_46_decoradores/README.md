## Profundizando en Decoradores en Python

**Introducción:**

Los decoradores en Python son funciones que se utilizan para modificar el comportamiento de otras funciones. Son una herramienta poderosa que puede ayudarte a escribir código más modular, reutilizable y elegante.

**Repaso rápido:**

* **Definición:** Se pueden definir decoradores utilizando la arroba (@) seguida del nombre de la función decoradora.

```python
def mi_decorador(funcion):
    def wrapper():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return wrapper

@mi_decorador
def mi_funcion():
    print("Hola Mundo")

mi_funcion()

# Salida:
# Antes de la función
# Hola Mundo
# Después de la función
```

* **Parámetros:** Los decoradores pueden recibir parámetros.

```python
def mi_decorador(parametro):
    def wrapper(funcion):
        def inner_wrapper(*args, **kwargs):
            print(f"Parámetro: {parametro}")
            funcion(*args, **kwargs)
        return inner_wrapper
    return wrapper

@mi_decorador("Hola")
def mi_funcion():
    print("Hola Mundo")

mi_funcion()

# Salida:
# Parámetro: Hola
# Hola Mundo
```

* **Decoradores con argumentos:** Los decoradores pueden recibir argumentos al ser aplicados.

```python
def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        funcion(*args, **kwargs)
        print("Después de la función")
    return wrapper

@mi_decorador
def mi_funcion(nombre):
    print(f"Hola {nombre}")

mi_funcion("Juan")

# Salida:
# Antes de la función
# Hola Juan
# Después de la función
```

**Tipos de decoradores:**

* **Decoradores de funciones:** Se utilizan para modificar el comportamiento de otras funciones.
* **Decoradores de métodos:** Se utilizan para modificar el comportamiento de métodos de clase.
* **Decoradores de clases:** Se utilizan para modificar el comportamiento de clases.

**Decoradores y functools:**

La biblioteca `functools` de Python proporciona algunas funciones útiles para trabajar con decoradores.

* **`wraps`:** Se utiliza para que un decorador conserve el nombre, la documentación y la firma de la función decorada.

```python
from functools import wraps

def mi_decorador(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        funcion(*args, **kwargs)
        print("Después de la función")
    return wrapper

@mi_decorador
def mi_funcion(nombre):
    print(f"Hola {nombre}")

help(mi_funcion)

# Salida:
# Ayuda para mi_funcion():

#   Hola a la persona indicada

#   Parámetros:
#     nombre: El nombre de la persona a saludar
```

* **`partial`:** Se utiliza para crear una nueva función con un conjunto predefinido de argumentos.

```python
from functools import partial

def mi_funcion(nombre, apellido):
    print(f"Hola {nombre} {apellido}")

mi_funcion_parcial = partial(mi_funcion, nombre="Juan")

mi_funcion_parcial("Pérez")

# Salida:
# Hola Juan Pérez
```

**Recursos adicionales:**

* Documentación oficial de Python: [https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html)
* Tutorial de Python: [se quitó una URL no válida]
* Curso de Python para principiantes: [https://learn.microsoft.com/es-es/training/paths/beginner-python/](https://learn.microsoft.com/es-es/training/paths/beginner-python/)

**Espero que esta información te sea útil. Si tienes alguna pregunta, no dudes en preguntar.**

**Consejos adicionales:**

* Los decoradores son una herramienta poderosa, pero no se deben usar en exceso.
* Es importante usarlos para tareas que realmente los necesiten.
* Si no necesitas modificar el comportamiento de una función, es mejor no usar un decorador.

**Ejemplos adicionales de uso de decoradores:**

* **Validar datos:**

```python
def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
