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
            sentencia = "SELECT * FROM persona WHERE id_persona IN %s"

            # Solicitamos al usuario los valores de los ID
            entrada = input("Proporciona los id's a buscar (separado por comas): ")
            llaves_primarias = (tuple(entrada.split(",")),)

            # Ejecutamos la consulta, pasando los valores de los ID como parámetro
            cursor.execute(sentencia, llaves_primarias)

            # Recuperamos todos los registros
            registros = cursor.fetchall()

            # Imprimimos los registros
            for registro in registros:
                print(registro)

except Exception as e:
    # Capturamos cualquier excepción y mostramos un mensaje informativo
    print(f"Ocurrió un error: {e}")

finally:
    # Cerramos la conexión a la base de datos
    conexion.close()
