## Profundizando en Funciones en Python

**Introducción:**

Las funciones en Python son bloques de código reutilizables que se pueden llamar desde otras partes del programa. Permiten modularizar el código y hacerlo más fácil de entender y mantener.

**Repaso rápido:**

* **Definición:** Se pueden definir funciones utilizando la palabra clave `def`.

```python
def mi_funcion():
    print("Hola Mundo")

mi_funcion()

# Salida: "Hola Mundo"
```

* **Parámetros:** Se pueden definir funciones con parámetros para recibir datos desde otras partes del programa.

```python
def mi_funcion(nombre):
    print(f"Hola {nombre}")

mi_funcion("Juan")

# Salida: "Hola Juan"
```

* **Valores por defecto:** Se pueden definir valores por defecto para los parámetros.

```python
def mi_funcion(nombre, saludo="Hola"):
    print(f"{saludo} {nombre}")

mi_funcion("Juan")

# Salida: "Hola Juan"

mi_funcion("Ana", "Buenos días")

# Salida: "Buenos días Ana"
```

* **Retorno de valores:** Se puede usar la palabra clave `return` para devolver un valor desde una función.

```python
def mi_funcion(numero):
    return numero * 2

resultado = mi_funcion(5)

print(resultado)  # Salida: 10
```

**Tipos de funciones:**

* **Funciones built-in:** Son funciones predefinidas que vienen con Python.

```python
print("Hola Mundo")

# La función print() es una función built-in
```

* **Funciones definidas por el usuario:** Son funciones que se definen en el propio programa.

```python
def mi_funcion():
    print("Hola Mundo")

mi_funcion()
```

* **Funciones lambda:** Son funciones anónimas que se pueden definir en una sola línea.

```python
resultado = lambda numero: numero * 2

print(resultado(5))  # Salida: 10
```

**Alcance de las variables:**

* **Variables locales:** Son variables que solo son accesibles dentro de la función en la que se definen.

```python
def mi_funcion():
    nombre = "Juan"
    print(nombre)

mi_funcion()

# La variable nombre no es accesible fuera de la función

```

* **Variables globales:** Son variables que son accesibles desde cualquier parte del programa.

```python
nombre = "Juan"

def mi_funcion():
    print(nombre)

mi_funcion()

# La variable nombre es accesible dentro de la función
```

**Decoradores:**

Los decoradores son funciones que se utilizan para modificar el comportamiento de otras funciones.

**Ejemplo:**

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

**Recursos adicionales:**

* Documentación oficial de Python: [https://pypi.org/project/wikipedia/](https://pypi.org/project/wikipedia/)
* Tutorial de Python: [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
* Curso de Python para principiantes: [https://learn.microsoft.com/es-es/training/paths/beginner-python/](https://learn.microsoft.com/es-es/training/paths/beginner-python/)

**Espero que esta información te sea útil. Si tienes alguna pregunta, no dudes en preguntar.**

**Consejos adicionales:**

* Las funciones son una herramienta poderosa que te permite organizar tu código y hacerlo más reutilizable.
* Es importante tener en cuenta el alcance de las variables al usar funciones.
* Los decoradores son una herramienta avanzada que se puede usar para modificar el comportamiento de otras funciones.

**Ejemplos de uso de funciones:**

* Realizar cálculos matemáticos.
* Procesar datos.
* Validar datos.
* Formatear texto.
* Mostrar información al usuario.
