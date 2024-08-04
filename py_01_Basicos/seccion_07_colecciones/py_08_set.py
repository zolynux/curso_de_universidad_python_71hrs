# set
planetas = {"Marte", "Júpiter", "Venus"}
print(planetas)
# largo
print(len(planetas))
# Revisar  si un elemento está presente
print("Marte" in planetas)
print("Martes" in planetas)
# agregar un elemento
planetas.add("Tierra")
print(planetas)
# No se pueden duplicar elementos
planetas.add("Tierra")
print(planetas)
# Eliminar elemento
planetas.remove("Tierra")
print(planetas)
# Eliminar elemento posiblemente arrojando un error
# planetas.remove("Tierra")
# print(planetas)
# Eliminar elemento sin arrojar error
planetas.discard("Júpiters")
print(planetas)
# Limpiar set
planetas.clear()
print(planetas)
# Eliminar el set
del planetas
print(planetas)
