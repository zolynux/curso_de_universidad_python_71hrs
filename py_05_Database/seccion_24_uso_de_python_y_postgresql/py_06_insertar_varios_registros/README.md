## Explicación del código Python para insertar múltiples datos en PostgreSQL con comentarios:

**1. Importación de la biblioteca:**

```python
# Importamos la biblioteca psycopg2 para la conexión a PostgreSQL
import psycopg2
```

- Se importa la biblioteca `psycopg2` que nos permite conectarnos y ejecutar operaciones en una base de datos PostgreSQL desde Python.

**2. Establecimiento de la conexión:**

```python
# Establecemos la conexión a la base de datos
conexion = psycopg2.connect(
    user='postgres',# Usuario de la base de datos
    password='admin',# Contraseña del usuario
    host='127.0.0.1',# Dirección IP del servidor (localhost)
    port='5432',# Puerto por defecto de PostgreSQL
    database='test_db'# Nombre de la base de datos
)
```

- Se crea una variable `conexion` que almacena la conexión a la base de datos. Se especifican los parámetros de conexión:
    - `user`: Usuario de la base de datos (por defecto 'postgres').
    - `password`: Contraseña del usuario (por defecto 'admin').
    - `host`: Dirección IP del servidor (localhost por defecto).
    - `port`: Puerto de la base de datos (5432 por defecto).
    - `database`: Nombre de la base de datos a la que se desea conectar.

**3. Bloque "with" para la conexión:**

```python
try:
# Usamos un bloque "with" para asegurar el cierre de la conexión
with conexion:
..
except Exception as e:
...
finally:
    conexion.close()
```

- Se utiliza un bloque `with` para asegurar que la conexión a la base de datos se cierre correctamente, incluso si se produce una excepción.

**4. Creación del cursor:**

```python
# Creamos un cursor para ejecutar la consulta
with conexion.cursor() as cursor:
```

- Se crea un cursor que nos permite ejecutar consultas y obtener resultados de la base de datos. El cursor se cierra automáticamente al finalizar el bloque `with`.

**5. Preparación de la sentencia INSERT:**

```python
# Preparamos la sentencia SQL INSERT
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
```

- Se define la sentencia SQL `INSERT INTO` que se utilizará para insertar datos en la tabla `persona`. La sentencia especifica:
    - La tabla (`persona`) donde se insertarán los datos.
    - Las columnas (`nombre`, `apellido`, `email`) donde se insertarán los valores.
    - Los marcadores de posición (`%s`) que se reemplazarán por los valores dinámicos.

**6. Definición de los valores:**

```python
# Definimos los valores que se insertarán
valores = (
  ('Marcos', 'Cantu', 'mcantu@mail.com'),
  ('Angel', 'Quintana', 'aquitana@mail.com'),
  ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
)
```

- Se define una tupla de tuplas que contiene los valores que se insertarán en las columnas de la tabla. La posición de cada tupla interna en la tupla externa debe coincidir con la posición del marcador de posición en la sentencia `INSERT`.

**7. Ejecución de la sentencia INSERT:**

```python
# Ejecutamos la sentencia INSERT
cursor.executemany(sentencia, valores)
```

- Se ejecuta la sentencia `INSERT` utilizando el cursor. Se pasan como argumentos la sentencia y la tupla de valores. La función `executemany` permite insertar múltiples registros de forma eficiente.

**8. Obtención del número de registros insertados:**

```python
# Obtenemos el número de registros insertados
registros_insertados = cursor.rowcount
```

- Se obtiene el número de registros que fueron insertados exitosamente en la base de datos.

**9. Mensaje informativo:**

```python
# Mostramos un mensaje informativo con el número de registros insertados
print(f'Registros Insertados: {registros_insertados}')
```

- Se muestra un mensaje informativo con el número de registros insertados.

**10. Manejo de excepciones:**

```python
except Exception as e:
# Capturamos cualquier excepción y mostramos un mensaje informativo
print(f'Ocurrió un error: {e}')
```

- Se captura cualquier excepción que pueda ocurrir durante la ejecución del código y se muestra un mensaje informativo con el error.

