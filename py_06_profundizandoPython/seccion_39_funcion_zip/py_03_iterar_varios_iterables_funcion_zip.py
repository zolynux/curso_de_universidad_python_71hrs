# Iterar varios iterables con la función zip en Python
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


for numero, letra, id, aleatorio in zip(numeros, letras, indenificadores, conjunto):
    print(f"Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}")

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, indenificadores, conjunto):
    nueva_lista.append(f"{id}-{numero}-{letra}-{aleatorio}")

print(nueva_lista)
