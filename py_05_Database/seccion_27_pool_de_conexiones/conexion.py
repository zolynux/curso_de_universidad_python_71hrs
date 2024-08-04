from logger_base import log
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CON = 1  # mínimo conexion
    _MAX_CON = 5  # Máximo conexion
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE,
                )
                log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrió un error al obtenido el pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    # Liberar una Conexión del Pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)  # put - poner o colocar
        log.debug(f"Regresamos la conexión al pool: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    # conexion3 = Conexion.obtenerConexion()
    # conexion4 = Conexion.obtenerConexion()
    # conexion5 = Conexion.obtenerConexion()
    # conexion6 = Conexion.obtenerConexion() # esta marcado un error que conexión a máximos son 5 conexiones

# Pool De Conexiones con python y PostgreSQL
