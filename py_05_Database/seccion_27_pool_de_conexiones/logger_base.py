import logging as log

# Handler = Manejador
# 'asctime' = Esto agrega el tiempo (fecha y hora) al mensaje de log
# 'levelname' = Esto agrega si fue Debug, Info, Warning, Error o Critical
# 'filename' = Esto agrega el nombre del archivo al mensaje del log
# 'lineno' = Esto agrega el número de línea al mensaje del log
# 'message' = Esto muestra el mensaje que hemos agregado al log
log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
    datefmt="%I:%H:%S %p",
    handlers=[log.FileHandler("./capa_datos.log"), log.StreamHandler()],
)


if __name__ == "__main__":
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel info")
    log.warning("Mensaje a nivel warning")
    log.error("Mensaje a nivel error")
    log.critical("Mensaje a nivel critico")
