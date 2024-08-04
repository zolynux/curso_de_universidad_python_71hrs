# Más detalles de la función zip en python
# zip significa comprimir
# help(zip)
numeros = [1, 2, 3]
letras = ["a", "b", "c", "d"]
indenificadores = 321, 322, 323, 324, 325  # tupla sin ponerlo parentesis
conjunto = {6, 4, 0, 9, 8, 15, 10}
mezcla = zip(numeros, letras, indenificadores, conjunto)
# print(mezcla)
print(list(mezcla))
# print(tuple(zip(numeros, letras)))
# print(type(mezcla))
