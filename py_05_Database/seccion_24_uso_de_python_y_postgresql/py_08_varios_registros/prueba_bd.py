import psycopg2

# Establecemos la conexión a la base de datos (una sola línea para ahorrar espacio)
conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_db",
)

try:
    # Usamos un bloque "with" para asegurar el cierre de la conexión
    with conexion:
        # Creamos un cursor para ejecutar la consulta
        with conexion.cursor() as cursor:
            # Sentencia SQL para actualizar (actualiza "nombre", "apellido" y "email" por "id_persona")
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            # Preparamos los valores a actualizar (lista de tuplas)
            valores = (
                ("Juan", "Perez", "jperez@mail", 1),
                ("Ivonne", "Guiterrez", "iguiterrez@mail", 2),
            )
            # Ejecutamos la consulta con los valores (para múltiples filas)
            cursor.executemany(sentencia, valores)
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
