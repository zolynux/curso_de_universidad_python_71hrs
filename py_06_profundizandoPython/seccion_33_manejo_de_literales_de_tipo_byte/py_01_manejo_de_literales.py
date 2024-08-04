# Manejo de Literales de tipo Byte en Python

"""
Un byte es un conjunto de 8 bits y constituye
el mínimo elemento de memoria direccionable
en una computadora.
"""

# Caracteres bytes
caracteres_en_bytes = b"Hola mundo"
print(caracteres_en_bytes)

mensaje = b"Universidad Python"
print(mensaje[0])
print(chr(mensaje[0]))
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)
