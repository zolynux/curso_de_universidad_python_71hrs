import psycopg2

# Establecemos la conexión a la base de datos
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
            # Sentencia SQL para eliminar
            # Elimina un registro de la tabla "persona" por "id_persona"
            sentencia = "DELETE FROM persona WHERE id_persona = %s"
            # Se solicita al usuario el id_persona a eliminar
            entrada = input("Proporciona el id_persona a eliminar: ")
            # Preparamos el valor a eliminar
            valores = (entrada,)
            # Ejecutamos la consulta con el valor
            cursor.execute(sentencia, valores)
            # Obtenemos el número de registros eliminados
            registros_eliminados = cursor.rowcount
            # Mostramos un mensaje informativo con el número de registros eliminados
            print(f"Registros Eliminados: {registros_eliminados}")

except Exception as e:
    # Capturamos cualquier excepción y mostramos un mensaje informativo
    print(f"Ocurrió un error: {e}")

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
