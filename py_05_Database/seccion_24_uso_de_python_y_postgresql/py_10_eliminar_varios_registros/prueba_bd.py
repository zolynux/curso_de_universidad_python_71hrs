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
            # Sentencia SQL para eliminar
            # Elimina uno o más registros de la tabla "persona" por "id_persona"
            sentencia = "DELETE FROM persona WHERE id_persona IN %s"
            # Se solicita al usuario los id_persona a eliminar (separados por coma)
            entrada = input(
                "Proporciona el id_persona a eliminar (separados por coma): "
            )
            # Se convierten los valores a una tupla
            valores = (tuple(entrada.split(",")),)
            # Ejecutamos la consulta con los valores
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
