# Métodos replace y strip en Pytthon

from urllib.request import urlopen

with urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt") as mensaje:
    contenido = mensaje.read().decode("utf-8")

# reemplazar contenido en un str
print(contenido.replace(" ", "-"))

# Eliminar caracteres al inicio y final de un str - strip
titulo = " *** GlobalMentoring.com.mx *** "
print("Cadena original:", titulo, len(titulo))
titulo = titulo.strip()
print("Cadena modificada:", titulo, len(titulo))

titulo = "***GlobalMentoring.com.mx***".strip("*")
print("Cadena modificada:", titulo)

titulo = "***GlobalMentoring.com.mx***".lstrip("*")
print("Cadena modificada:", titulo)

titulo = "***GlobalMentoring.com.mx***".rstrip("*")
print("Cadena modificada:", titulo)

titulo = " *** GlobalMentoring.com.mx *** ".split().split("*").split()
print("Cadena modificada:", titulo)
