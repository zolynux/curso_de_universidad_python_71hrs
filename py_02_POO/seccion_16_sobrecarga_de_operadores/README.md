# Sobrecarga de Operadores en PYthon 

## ¿Qué es la sobrecarga de operadores?

Es la capacidad de modificar el comportamiento de los operadores predefinidos en Python para que funcionen con objetos personalizados.

## ¿Por qué usarla?

* **Mejora la legibilidad del código:** Permite usar operadores conocidos con objetos personalizados.
* **Hace el código más intuitivo:** Los usuarios pueden interactuar con objetos personalizados de forma natural.
* **Evita la escritura de código redundante:** Permite reutilizar la lógica de los operadores predefinidos.

## ¿Cómo funciona?

Python define métodos especiales para cada operador. Al sobrecargar estos métodos en una clase, se puede modificar el comportamiento del operador para esa clase.

## Tabla de métodos por operador:



### Operadores binarios

| **Operador** | **Método**                |
| ------------ | ------------------------- |
| +            | __add__(self, other)      |
| -            | __sub__(self, other)      |
| *            | __mul__(self, other)      |
| /            | __truediv__(self, other)  |
| //           | __floordiv__(self, other) |
| %            | __mod__(self, other)      |
| **           | __pow__(self, other)      |


### Operadores de comparación:

| **Operador** | **Método**          |
| ------------ | ------------------- |
| <            | __lt__(self, other) |
| >            | __gt__(self, other) |
| <=           | __le__(self, other) |
| >=           | __ge__(self, other) |
| ==           | __eq__(self, other) |
| !=           | __ne__(self, other) |

### Operadores de Asignación:

| **Operador** | **Método**                 |
| ------------ | -------------------------- |
| +=           | __iadd__(self, other)      |
| -=           | __isub__(self, other)      |
| *=           | __imul__(self, other)      |
| /=           | __idiv__(self, other)      |
| //=          | __ifloordiv__(self, other) |
| %=           | __imod__(self, other)      |
| **=          | __ipow__(self, other)      |

### Operadores unarios

| **Operador** | **Método**              |
| ------------ | ----------------------- |
| +            | __neg__(self, other)    |
| -            | __pos__(self, other)    |
| ~            | __invert__(self, other) |

**Consejos para memorizar:**

* **Relaciona los operadores con sus métodos:** Observa cómo el nombre del método refleja el operador.
* **Practica la sobrecarga de operadores:** Crea ejemplos para cada tipo de operador.
* **Utiliza recursos online:** Hay muchos tutoriales y ejemplos disponibles.
* **Crea mnemotécnicas:** Frases o palabras que te ayuden a recordar la asociación entre operador y método.

**Ejemplo:**

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector ({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2

print(v3)
```

**Salida:**

```
Vector (4, 6)
```

**Recuerda:** La sobrecarga de operadores es una herramienta poderosa, pero úsala con cuidado para evitar confusiones en tu código.

