# Leer el archivo de contenido online en Bytes en Python
# Leer contenido online

# URL = Uniform Resource Locator
"""
URL es la dirección específica que se asigna a
cada uno de los recursos disponibles en internet
"""

from urllib.request import urlopen

with urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt") as mensaje:
    # contenido = mensaje.read()
    contenido = mensaje.read().decode("utf-8")
    print(contenido)

with open("nuevo_archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)
