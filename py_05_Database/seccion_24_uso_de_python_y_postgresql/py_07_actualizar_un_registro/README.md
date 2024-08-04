## Explicación detallada del código Python para actualizar datos en PostgreSQL:

**Importación de la biblioteca:**

```python
import psycopg2
```

Se importa la biblioteca `psycopg2` que permite conectar y ejecutar comandos en PostgreSQL desde Python.

**Establecimiento de la conexión:**

```python
conexion = psycopg2.connect(
    user='postgres',  # Usuario de la base de datos
    password='admin',  # Contraseña del usuario
    host='127.0.0.1',  # Dirección IP del servidor (localhost)
    port='5432',  # Puerto por defecto de PostgreSQL
    database='test_db'  # Nombre de la base de datos
)
```

Se crea una variable `conexion` que establece la conexión a la base de datos. Reemplaza los valores por defecto con la
información de tu servidor y base de datos.

**Explicación de los argumentos:**

* `user`: Nombre de usuario de la base de datos.
* `password`: Contraseña del usuario.
* `host`: Dirección IP del servidor donde se encuentra la base de datos (localhost si está en el mismo equipo).
* `port`: Puerto por defecto de PostgreSQL (5432).
* `database`: Nombre de la base de datos a la que se desea conectar.

**Bloque `with` para la conexión:**

```python
try:
    # Usamos un bloque "with" para asegurar el cierre de la conexión
    with conexion:
# ...
```

Se utiliza un bloque `with` para garantizar que la conexión se cierre correctamente, incluso si se produce una
excepción.

**Creación del cursor:**

```python
with conexion.cursor() as cursor:
# ...
```

Dentro del bloque `with`, se crea un cursor que permite ejecutar consultas y obtener resultados. El cursor se cierra
automáticamente al finalizar el bloque.

**Sentencia SQL para actualizar:**

```python
sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
```

Se define la consulta SQL `UPDATE` que se utilizará para actualizar los datos. La consulta actualiza la tabla `persona`
con los nuevos valores para `nombre`, `apellido` y `email` donde el `id_persona` sea igual a 1.

**Explicación de la consulta:**

* `UPDATE`: Indica que se desea actualizar una tabla.
* `persona`: Nombre de la tabla a actualizar.
* `SET`: Indica que se van a modificar valores.
* `nombre=%s, apellido=%s, email=%s`: Columnas y nuevos valores (los valores se asignarán dinámicamente).
* `WHERE id_persona=%s`: Condición para determinar qué filas se actualizarán (en este caso, solo se actualizará la fila
  con `id_persona` igual a 1).

**Preparación de los valores:**

```python
valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail', 1)
```

Se define una tupla `valores` que contiene los nuevos valores que se asignarán a las columnas en la consulta `UPDATE`.
La posición de cada valor en la tupla debe coincidir con el orden de las columnas en la consulta.

**Ejecución de la consulta:**

```python
cursor.execute(sentencia, valores)
```

Se ejecuta la consulta SQL `UPDATE` con los valores proporcionados. El método `execute` del cursor recibe la consulta y
los valores como argumentos.

**Obtención del número de registros actualizados:**

```python
registros_actualizados = cursor.rowcount
```

Se obtiene el número de registros que fueron afectados por la consulta `UPDATE` utilizando la propiedad `rowcount` del
cursor.

**Mensaje informativo:**

```python
print(f'Registros Actualizado: {registros_actualizados}')
```

Se imprime un mensaje informativo que muestra el número de registros actualizados.

**Manejo de excepciones:**

```python
except Exception as e:
  # Capturamos cualquier excepción y mostramos un mensaje informativo
  print(f'Ocurrió un error: {e}')
```

Se utiliza un bloque `except` para capturar cualquier excepción que pueda ocurrir durante la ejecución del código. En
este caso, se muestra un mensaje informativo con la descripción del error.

**Cierre de la conexión:**

```python
finally:
  # Cerramos la conexión a la base de datos
  conexion.close()
```

Finalmente, se asegura el cierre de la conexión a la base de datos mediante el método `close`.
