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
            # Definimos la consulta con un placeholder para el ID
            sentencia = "SELECT * FROM persona WHERE id_persona = %s"

            # Solicitamos al usuario el valor del ID
            id_persona = input("Proporciona el valor id_persona: ")

            # Ejecutamos la consulta, pasando el valor del ID como parámetro
            cursor.execute(sentencia, (id_persona,))

            # Recuperamos el primer registro (fetchone)
            registros = cursor.fetchone()

            # Imprimimos el registro
            print(registros)

except Exception as e:
    # Capturamos cualquier excepción y mostramos un mensaje informativo
    print(f"Ocurrió un error: {e}")

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
