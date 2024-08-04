## Explicación del código Python para insertar datos en PostgreSQL:

**1. Importación de la biblioteca:**

```python
import psycopg2
```

- Se importa la biblioteca `psycopg2` que nos permite conectarnos y ejecutar operaciones en una base de datos PostgreSQL
  desde Python.

**2. Establecimiento de la conexión:**

```python
conexion = psycopg2.connect(
    user='postgres',  # Usuario de la base de datos
    password='admin',  # Contraseña del usuario
    host='127.0.0.1',  # Dirección IP del servidor (localhost)
    port='5432',  # Puerto por defecto de PostgreSQL
    database='test_db'  # Nombre de la base de datos
)
```

- Se crea una variable `conexion` que almacena la conexión a la base de datos. Se especifican los siguientes parámetros:
    - `user`: Usuario de la base de datos.
    - `password`: Contraseña del usuario.
    - `host`: Dirección IP del servidor (localhost por defecto).
    - `port`: Puerto de la base de datos (5432 por defecto).
    - `database`: Nombre de la base de datos a la que se desea conectar.

**3. Bloque "with" para la conexión:**

```python
try:
    # Usamos un bloque "with" para asegurar el cierre de la conexión
    with conexion:
        ...
except Exception as e:
    ...
finally:
    conexion.close()
```

- Se utiliza un bloque `with` para asegurar que la conexión a la base de datos se cierre correctamente, incluso si se
  produce una excepción.

**4. Creación del cursor:**

```python
with conexion.cursor() as cursor:
    ...
```

- Se crea un cursor que nos permite ejecutar consultas y obtener resultados de la base de datos. El cursor se cierra
  automáticamente al finalizar el bloque `with`.

**5. Preparación de la sentencia INSERT:**

```python
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
```

- Se define la sentencia SQL `INSERT INTO` que se utilizará para insertar datos en la tabla `persona`. La sentencia
  especifica:
    - La tabla (`persona`) donde se insertarán los datos.
    - Las columnas (`nombre`, `apellido`, `email`) donde se insertarán los valores.
    - Los marcadores de posición (`%s`) que se reemplazarán por los valores dinámicos.

**6. Definición de los valores:**

```python
valores = ('Carlos', 'Lara', 'clara@mail.com')
```

- Se define una tupla que contiene los valores que se insertarán en las columnas de la tabla. La posición de cada valor
  en la tupla debe coincidir con la posición del marcador de posición en la sentencia `INSERT`.

**7. Ejecución de la sentencia INSERT:**

```python
cursor.execute(sentencia, valores)
```

- Se ejecuta la sentencia `INSERT` utilizando el cursor. Se pasan como argumentos la sentencia y los valores.

**8. Commit de los cambios:**

```python
# commit guarda los cambios en la base de datos
# conexion.commit()
# Al usar with, el commit se ejecuta en automático, así que no hay que colocarlo manualmente
```

- Se guarda la transacción en la base de datos. El commit se realiza automáticamente al usar un bloque `with`, por lo
  que no es necesario llamarlo manualmente.

**9. Obtención del número de registros insertados:**

```python
registros_insertados = cursor.rowcount
```

- Se obtiene el número de registros que fueron insertados exitosamente en la base de datos.

**10. Mensaje informativo:**

```python
print(f'Registros Insertados: {registros_insertados}')
```

- Se muestra un mensaje informativo con el número de registros insertados.

**11. Manejo de excepciones:**

```python
except Exception as e:
print(f'Ocurrió un error: {e}')
```

- Se captura cualquier excepción que pueda ocurrir durante la ejecución del código y se muestra un mensaje informativo
  con el error.

**12. Cierre de la conexión:**

```python
finally:
conexion.close()
```

- Se cierra la conexión a la base de datos al final del código para liberar recursos.

**Comentarios adicionales:**

- Se han añadido comentarios en el código para explicar cada sección y mejorar la legibilidad.
- Se ha utilizado la función `f-string` para formatear el mensaje informativo con el número de registros insertados.

## Sintaxis y comentarios en Python del código para insertar datos en PostgreSQL:

```python
# Importamos la biblioteca psycopg2 para la conexión a PostgreSQL
import psycopg2

# Establecemos la conexión a la base de datos
conexion = psycopg2.connect(
    user='postgres',  # Usuario de la base de datos
    password='admin',  # Contraseña del usuario
    host='127.0.0.1',  # Dirección IP del servidor (localhost)
    port='5432',  # Puerto por defecto de PostgreSQL
    database='test_db'  # Nombre de la base de datos
)

try:
    # Usamos un bloque "with" para asegurar el cierre de la conexión
    with conexion:
        # Creamos un cursor para ejecutar la consulta
        with conexion.cursor() as cursor:
            # Preparamos la sentencia SQL INSERT
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            # Definimos los valores que se insertarán
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            # Ejecutamos la sentencia INSERT
            cursor.execute(sentencia, valores)
            # Guardamos los cambios en la base de datos
            conexion.commit()
            # Obtenemos el número de registros insertados
            registros_insertados = cursor.rowcount
            # Mostramos un mensaje informativo con el número de registros insertados
            print(f'Registros Insertados: {registros_insertados}')

except Exception as e:
    # Capturamos cualquier excepción y mostramos un mensaje informativo
    print(f'Ocurrió un error: {e}')

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
```

**Comentarios:**

- Se han añadido comentarios al código para explicar cada sección y mejorar la legibilidad.
- Se ha utilizado la función `f-string` para formatear el mensaje informativo con el número de registros insertados.

**Explicación de la sintaxis:**

- `import psycopg2`: Importa la biblioteca `psycopg2` que nos permite conectarnos y ejecutar operaciones en una base de
  datos PostgreSQL desde Python.
- `conexion = psycopg2.connect(...)`: Crea una variable `conexion` que almacena la conexión a la base de datos. Se
  especifican los parámetros de conexión.
- `with conexion:`: Bloque `with` para asegurar el cierre de la conexión.
- `with conexion.cursor() as cursor:`: Crea un cursor que nos permite ejecutar consultas y obtener resultados de la base
  de datos. Se cierra automáticamente al finalizar el bloque `with`.
- `sentencia = 'INSERT INTO ... VALUES(...)'`: Define la sentencia SQL `INSERT INTO` que se utilizará para insertar
  datos en la tabla `persona`.
- `valores = (...)`: Define una tupla que contiene los valores que se insertarán en las columnas de la tabla.
- `cursor.execute(sentencia, valores)`: Ejecuta la sentencia `INSERT` utilizando el cursor. Se pasan como argumentos la
  sentencia y los valores.
- `conexion.commit()`: Guarda la transacción en la base de datos.
- `registros_insertados = cursor.rowcount`: Obtiene el número de registros que fueron insertados exitosamente en la base
  de datos.
- `print(f'Registros Insertados: {registros_insertados}')`: Muestra un mensaje informativo con el número de registros
  insertados.
- `except Exception as e:`: Captura cualquier excepción que pueda ocurrir durante la ejecución del código y muestra un
  mensaje informativo con el error.
- `finally:`: Bloque `finally` para asegurar que la conexión a la base de datos se cierra correctamente, incluso si se
  produce una excepción.
- `conexion.close()`: Cierra la conexión a la base de datos.
