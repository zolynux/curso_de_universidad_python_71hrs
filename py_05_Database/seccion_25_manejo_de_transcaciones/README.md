## Manejo de transacciones con Python y PostgreSQL

**Introducción:**

Una transacción es una unidad de trabajo que agrupa una serie de operaciones en una sola unidad lógica. En el contexto de una base de datos, una transacción debe cumplir con las propiedades ACID:

* **Atomicidad:** Todas las operaciones de la transacción se ejecutan juntas o ninguna.
* **Consistencia:** La transacción debe mantener la integridad de la base de datos.
* **Aislamiento:** Las transacciones se ejecutan de forma independiente y no interfieren entre sí.
* **Durabilidad:** Los cambios realizados por la transacción son permanentes.

**Manejo de transacciones en Python con psycopg2:**

La biblioteca `psycopg2` proporciona funcionalidades para manejar transacciones en PostgreSQL desde Python. 

**A continuación se presenta un ejemplo de cómo realizar una transacción en Python con psycopg2:**

```python
import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db',
)

try:
    # Iniciamos una transacción
    with conexion.cursor() as cursor:
        cursor.execute('BEGIN')

        # Sentencia SQL para actualizar
        sentencia_update = 'UPDATE persona SET nombre=%s WHERE id_persona=%s'
        valores_update = ('Juan Carlos', 1)
        cursor.execute(sentencia_update, valores_update)

        # Sentencia SQL para insertar
        sentencia_insert = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
        valores_insert = ('Ana', 'Gutierrez', 'anagutierrez@mail.com')
        cursor.execute(sentencia_insert, valores_insert)

        # Si no hay errores, confirmamos la transacción
        cursor.execute('COMMIT')

except Exception as e:
    # Si hay un error, deshacemos la transacción
    cursor.execute('ROLLBACK')
    print(f'Ocurrió un error: {e}')

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
```

**Explicación del código:**

1. Se importa la biblioteca `psycopg2`.
2. Se establece la conexión a la base de datos.
3. Se inicia una transacción utilizando el comando `BEGIN`.
4. Se ejecutan las sentencias SQL dentro de la transacción.
5. Si no hay errores, se confirma la transacción utilizando el comando `COMMIT`.
6. Si hay un error, se deshace la transacción utilizando el comando `ROLLBACK`.
7. Se cierra la conexión a la base de datos.

**Recursos adicionales:**

* Documentación de psycopg2: [https://www.psycopg.org/docs/](https://www.psycopg.org/docs/)
* Tutorial de PostgreSQL con Python: https://se quitó una URL no válida

**Manejo de excepciones:**

Es importante manejar las excepciones que puedan ocurrir durante la ejecución de una transacción. En el ejemplo anterior, se captura la excepción `Exception` y se deshace la transacción si se produce un error.

**Puntos clave:**

* Las transacciones son importantes para garantizar la integridad de la base de datos.
* La biblioteca `psycopg2` proporciona funcionalidades para manejar transacciones en PostgreSQL desde Python.
* Se debe utilizar `BEGIN` para iniciar una transacción, `COMMIT` para confirmarla y `ROLLBACK` para deshacerla.
* Es importante manejar las excepciones que puedan ocurrir durante la ejecución de una transacción.