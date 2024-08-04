print(" Profundizando en Diccionario - Parte 1 ".center(60, "-"))
# Los diccionarios guardan un orden (a diferencia de un set)
diccionario = {"Nombre": "Juan", "Apellido": "Perez", "Edad": 28}
print(diccionario)

# Los diccionarios son mutables, pero las llaves deben ser inmutatbles
# diccionario = {[1,2]: 'valor1'} # es un error de ser la lista
# diccionario = {(1,2): 'valor1'} # es un correcto de ser la tupla
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario["Departamento"] = "Sistemas"
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplazo)
diccionario["Nombre"] = "Juan Carlos"
print(diccionario)

print(" Profundizando en Diccionario - Parte 2 ".center(60, "-"))

# Recuperar un valor indicando una llave
print(diccionario["Nombre"])
# Si no encuentra la llave lanza una excepción
# print(diccionario['nombre']) # es un error de ejecuta

# Método get recuperar una llave, y si no existe No lanza excepción
# Además podemos regresar un valor un case de que no exista la llave
print(diccionario.get("Nombres", "No se encontró la llave"))
print(diccionario)

# setdefault si modifica el diccionario, además se agregar un valor por default
nombre = diccionario.setdefault("Nombres", "Valor por default")
print(nombre)
print(diccionario)

# Imprimir coon pprint
from pprint import pprint as pp

# help(pp)
pp(diccionario, sort_dicts=False)
