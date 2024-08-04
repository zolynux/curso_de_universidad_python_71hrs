# Importamos la biblioteca psycopg2 para la conexión a PostgreSQL
import psycopg2

# Establecemos la conexión a la base de datos
conexion = psycopg2.connect(
    # Usuario de la base de datos
    user="postgres",
    # Contraseña del usuario
    password="admin",
    # Dirección IP del servidor (localhost)
    host="127.0.0.1",
    # Puerto por defecto de PostgreSQL
    port="5432",
    # Nombre de la base de datos
    database="test_db",
)

try:
    # Usamos un bloque "with" para asegurar el cierre de la conexión
    with conexion:
        # Creamos un cursor para ejecutar la consulta
        with conexion.cursor() as cursor:
            # Sentencia SQL para actualizar
            # Se actualiza la tabla "persona" con los nuevos valores para "nombre", "apellido"
            # y "email" donde el "id_persona" sea igual a 1.
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            # Preparamos los valores a actualizar
            # La posición de cada valor en la tupla debe coincidir con el orden de las columnas en la consulta.
            valores = ("Juan Carlos", "Juarez", "jcjuarez@mail", 1)
            # Ejecutamos la consulta con los valores
            cursor.execute(sentencia, valores)
            # Obtenemos el número de registros actualizados
            registros_actualizados = cursor.rowcount
            # Mostramos un mensaje informativo con el número de registros actualizados
            print(f"Registros Actualizados: {registros_actualizados}")

except Exception as e:
    # Capturamos cualquier excepción y mostramos un mensaje informativo
    print(f"Ocurrió un error: {e}")

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
