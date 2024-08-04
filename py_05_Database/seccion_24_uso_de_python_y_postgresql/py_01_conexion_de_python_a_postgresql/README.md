## Conexión a una base de datos PostgreSQL con Python

**Explicación del código:**

```python
import psycopg2

# Establecemos los parámetros de conexión
conexion = psycopg2.connect(
    user='postgres', # Usuario de la base de datos
    password='admin', # Contraseña del usuario
    host='127.0.0.1', # Dirección IP del servidor (localhost)
    port='5432', # Puerto por defecto de PostgreSQL
    database='test_db' # Nombre de la base de datos
)

# Creamos un cursor para ejecutar consultas
cursor = conexion.cursor()

# Consulta para recuperar todos los registros de la tabla "persona"
sentencia = 'SELECT * FROM persona'

# Ejecutamos la consulta
cursor.execute(sentencia)

# Recuperamos los registros en forma de lista de tuplas
registros = cursor.fetchall()

# Imprimimos los registros
print(registros)

# Cerramos el cursor
cursor.close()

# Cerramos la conexión a la base de datos
conexion.close()
```

**Comentarios:**

* Se importa la biblioteca `psycopg2` para la conexión a PostgreSQL.
* Se establecen los parámetros de conexión: usuario, contraseña, host, puerto y nombre de la base de datos.
* Se crea un cursor para ejecutar consultas.
* Se define la consulta `SELECT * FROM persona` para recuperar todos los registros de la tabla "persona".
* Se ejecuta la consulta con el método `execute()`.
* Se recuperan los registros en forma de lista de tuplas con el método `fetchall()`.
* Se imprimen los registros.
* Se cierra el cursor y la conexión a la base de datos para liberar recursos.

**Importancia de este código:**

Este código es un ejemplo básico de cómo conectar Python a una base de datos PostgreSQL y recuperar datos. Es importante por las siguientes razones:

* **Demuestra la conexión básica:** Muestra cómo establecer la conexión a una base de datos PostgreSQL utilizando la biblioteca `psycopg2`.
* **Ejecución de consultas:** Explica cómo ejecutar una consulta `SELECT` para recuperar datos de una tabla.
* **Recuperación de datos:** Muestra cómo obtener los datos de la consulta en forma de lista de tuplas.
* **Manejo de recursos:** Cierra el cursor y la conexión a la base de datos para evitar errores y fugas de memoria.

**Markdown:**

* Se ha utilizado markdown para resaltar los diferentes bloques de código y comentarios.
* Se han añadido títulos y subtítulos para mejorar la legibilidad.
* Se han utilizado listas para enumerar los pasos y las ventajas.