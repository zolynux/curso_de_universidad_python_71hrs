# dict (key, value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System",
}

print(diccionario)
# largo
print(len(diccionario))  # Imprimir es 3
# Acceder a un elemento (key)
print(diccionario["IDE"])
# Otra forma de recuperar un elemento
print(diccionario.get("OOP"))
# Modificando elementos
diccionario["IDE"] = "integrated development environment"
print(diccionario)
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar existencia de algún elemento
print("IDE" in diccionario)

# agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# remove un elemento
diccionario.pop("DBMS")
print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
print(diccionario)
