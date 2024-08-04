# Dada la siguente tupla,
# Crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

# Definir la lista
lista = []

# Filtramos los elementos menores a 5 de la lista
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
