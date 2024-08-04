# archivo = open('C:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
archivo = open("prueba.txt", "r", encoding="utf8")
# print(archivo.read())

# leer algunos caracteres

# print(archivo.read(5))
# print(archivo.read(3))

# Leer línea completa
# print(archivo.readline())
# print(archivo.readline())

# Iterar el archivo
# for linea in archivo:
#     print(linea)

# Leer multi-lineas
# print(archivo.readlines())

# acceder a una línea de la lista
# print(archivo.readlines()[0])

# Abrimos un nuevo archivo
# a = anexar información
archivo2 = open("copia.txt", "a", encoding="utf8")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print("Se ha terminado el proceso de leer y copiar archivos")
