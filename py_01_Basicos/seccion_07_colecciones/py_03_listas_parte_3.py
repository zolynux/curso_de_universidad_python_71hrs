# Definir una lista de tipo str
nombres = ["Juan", "Karla", "Ricardo", "María"]
# Imprimir la lista nombres
print(nombres)
# Acceder a los elementos de un a lista
print(nombres[0])
print(nombres[1])
# Acceder a los elementos de manera invera
print(nombres[-1])
print(nombres[-2])
# Imprimir un rango
print(nombres[0:2])  # sin incluir el índice 2
# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
# Desde el índice indicando hasta el final
print(nombres[1:])
# Cambias un valor
nombres[3] = "Ivone"
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")

# Preguntar el largo de una lista
print(len(nombres))
# agregar un elementos
nombres.append("Lorenzo")
print(nombres)
# Insertar un elemento en un índice en específico
nombres.insert(1, "Octavio")
print(nombres)
# Remover un elemento
nombres.remove("Octavio")
print(nombres)
# remover el último valor agrega
nombres.pop()
print(nombres)
# Eliminar un índice
del nombres[0]
print(nombres)
# Limpiar la lista
nombres.clear()
print(nombres)
# Borrar la lista por completo
del nombres
print(nombres)
