# Importamos la biblioteca psycopg2 para la conexión a PostgreSQL
import psycopg2

# Establecemos la conexión a la base de datos
conexion = psycopg2.connect(
    user="postgres",  # Usuario de la base de datos
    password="admin",  # Contraseña del usuario
    host="127.0.0.1",  # Dirección IP del servidor (localhost)
    port="5432",  # Puerto por defecto de PostgreSQL
    database="test_db",  # Nombre de la base de datos
)

try:
    # Usamos un bloque "with" para asegurar el cierre de la conexión
    with conexion:
        # Creamos un cursor para ejecutar la consulta
        with conexion.cursor() as cursor:
            # Preparamos la sentencia SQL INSERT
            sentencia = (
                "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
            )
            valores = (
                ("Marcos", "Cantu", "mcantu@mail.com"),
                ("Angel", "Quintana", "aquitana@mail.com"),
                ("Maria", "Gonzalez", "mgonzalez@mail.com"),
            )
            # Ejecutamos la sentencia INSERT
            cursor.executemany(sentencia, valores)
            # Obtenemos el número de registros insertados
            registros_insertados = cursor.rowcount
            # Mostramos un mensaje informativo con el número de registros insertados
            print(f"Registros Insertados: {registros_insertados}")

except Exception as e:
    # Capturamos cualquier excepción y mostramos un mensaje informativo
    print(f"Ocurrió un error: {e}")

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
