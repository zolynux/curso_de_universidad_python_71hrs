import psycopg2

# Establecemos los parámetros de conexión
conexion = psycopg2.connect(
    user="postgres",  # Usuario de la base de datos
    password="admin",  # Contraseña del usuario
    host="127.0.0.1",  # Dirección IP del servidor (localhost)
    port="5432",  # Puerto por defecto de PostgreSQL
    database="test_db",  # Nombre de la base de datos
)

# Creamos un cursor para ejecutar consultas
cursor = conexion.cursor()

# Consulta para recuperar todos los registros de la tabla "persona"
sentencia = "SELECT * FROM persona"

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
