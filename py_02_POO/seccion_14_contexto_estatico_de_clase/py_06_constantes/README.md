## Constantes en Python

En Python, no hay una forma nativa de declarar constantes como en otros lenguajes. Sin embargo, existen algunas prácticas comunes para definir valores que no deben cambiar durante la ejecución del programa.

**Formas de definir constantes:**

* **Usando variables con nombres en mayúsculas:**

```python
NOMBRE_CONSTANTE = "Valor constante"
```

* **Usando la función `const` del módulo `builtins`:**

```python
from builtins import const

PI = const(3.141592653589793)
```

* **Usando módulos:**

```python
import math

GRAVEDAD = math.pi * math.pi
```

**Recomendaciones:**

* **Utiliza nombres descriptivos para las constantes.**
* **Evita usar guiones bajos en los nombres de las constantes.**
* **Documenta las constantes en tu código.**

**Ventajas de usar constantes:**

* **Mejora la legibilidad del código.**
* **Evita errores al modificar valores importantes.**
* **Facilita el mantenimiento del código.**

**Desventajas de usar constantes:**

* **No son completamente seguras, ya que se pueden modificar manualmente.**
* **Pueden hacer que el código sea menos flexible.**

**En resumen:**

Aunque Python no tiene una forma nativa de declarar constantes, existen algunas prácticas comunes para definir valores que no deben cambiar. El uso de constantes puede mejorar la legibilidad, seguridad y mantenimiento del código.