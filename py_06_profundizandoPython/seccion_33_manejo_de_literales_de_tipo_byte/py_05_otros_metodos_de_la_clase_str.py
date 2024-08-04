# Otros métodos de la clase str
# Leer contenido online

# URL = Uniform Resource Locator

from urllib.request import urlopen

with urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt") as mensaje:
    contenido = mensaje.read().decode("utf-8")

# Contar ocurrencias de una cadena
print("Numeros veces Universidad", contenido.count("Universidad"))

# upper convierte a mayúsculas un str
print("upper convierte a mayúscula".center(50, "-"))
print(contenido.upper())

# lower convierte a minúsculas un str
print("lower convierte a minúsculas".center(50, "-"))
print(contenido.lower())

# Buscamos la cadena python en el contenido
print("python" in contenido)  # False
print("Existe python?:", "python".lower() in contenido.lower())  # True
print("Existe Python?:", "Python".upper() in contenido.upper())  # True

# startswith - inicia con
print("Inicia con:", contenido.startswith("En GlobalMentoring.com.mx"))

# endswith - termina con
print("Termina con:", contenido.endtswith("GlobalMentoring.com.mx"))
print("Termina con:", contenido.lower().endtswith("GlobalMentoring.com.mx".lower()))
