## Funciones Lambda en Python

Las funciones lambda, también conocidas como funciones anónimas, son una herramienta poderosa en Python que te permite crear funciones pequeñas y concisas en una sola línea. Son útiles para tareas simples que no requieren una definición completa de una función.

**Sintaxis:**

La sintaxis de una función lambda es la siguiente:

```python
lambda argumentos: expresión
```

**Ejemplo:**

```python
# Función normal
def sumar(a, b):
    return a + b

# Función lambda equivalente
sumar = lambda a, b: a + b

resultado = sumar(2, 3)

print(resultado)  # Salida: 5
```

**Ventajas de las funciones lambda:**

* **Simplicidad:** Permiten definir funciones en una sola línea, lo que las hace más concisas y fáciles de leer.
* **Rapidez:** Son ideales para tareas simples que no requieren una definición completa de una función.
* **Flexibilidad:** Se pueden utilizar como argumentos de otras funciones, dentro de expresiones y como valores de variables.

**Desventajas de las funciones lambda:**

* **Limitaciones:** No admiten todas las características de las funciones normales, como la definición de variables locales o la documentación.
* **Legibilidad:** Pueden ser difíciles de leer y entender si se utilizan para tareas complejas.

**Ejemplos de uso de funciones lambda:**

* **Filtrar una lista:**

```python
numeros = [1, 2, 3, 4, 5]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Salida: [2, 4]
```

* **Ordenar una lista:**

```python
nombres = ["Ana", "Juan", "Pedro", "María"]

nombres.sort(key=lambda x: x[0])

print(nombres)  # Salida: ['Ana', 'Juan', 'María', 'Pedro']
```

* **Calcular el máximo de dos valores:**

```python
maximo = lambda a, b: a if a > b else b

resultado = maximo(10, 5)

print(resultado)  # Salida: 10
```

**Recursos adicionales:**

* Documentación oficial de Python: [se quitó una URL no válida]
* Tutorial de Python: [https://www.w3schools.com/python/python_lambda.asp](https://www.w3schools.com/python/python_lambda.asp)
* Curso de Python para principiantes: [https://learn.microsoft.com/es-es/training/paths/beginner-python/](https://learn.microsoft.com/es-es/training/paths/beginner-python/)

**Espero que esta información te sea útil. Si tienes alguna pregunta, no dudes en preguntar.**

**Consejos adicionales:**

* Las funciones lambda son una herramienta poderosa, pero no se deben usar en exceso. 
* Es importante usarlas para tareas simples y que no requieran una definición completa de una función.
* Si necesitas una función más compleja, es mejor definirla de forma normal.

**Ejemplos adicionales de uso de funciones lambda:**

* Convertir una cadena a mayúsculas:

```python
mayusculas = lambda cadena: cadena.upper()

resultado = mayusculas("hola mundo")

print(resultado)  # Salida: HOLA MUNDO
```

* Obtener la longitud de una cadena:

```python
longitud = lambda cadena: len(cadena)

resultado = longitud("Hola Mundo")

print(resultado)  # Salida: 10
```

* Formatear una cadena:

```python
formato = lambda nombre, apellido: f"{nombre} {apellido}"

resultado = formato("Juan", "Pérez")

print(resultado)  # Salida: Juan Pérez
```
