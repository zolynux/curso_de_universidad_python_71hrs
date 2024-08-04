# Leer las palabras de un archivo online en Bytes en Python
# Leer contenido online

# URL = Uniform Resource Locator
"""
URL es la dirección específica que se asigna a
cada uno de los recursos disponibles en internet
"""

from urllib.request import urlopen

palabras = []
with urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt") as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode("utf-8").split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)

print(palabras)
print(f"la cantidad de palabras son: {len(palabras)}")
