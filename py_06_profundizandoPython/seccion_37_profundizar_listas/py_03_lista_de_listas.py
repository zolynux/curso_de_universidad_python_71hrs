# Lista de listas en python

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f"Lista original: {numeros1}")

print(" Lista de Listas ".center(60, "-"))

# Multiplicación listas
listas_multiplicacion = 5 * [[2, 5]]
print(f"lista multiplicación: {listas_multiplicacion}")
print(f"Misma referencia: {listas_multiplicacion[0] is listas_multiplicacion[1]}")
print(f"Misma contenido: {listas_multiplicacion[0] == listas_multiplicacion[1]}")
listas_multiplicacion[2].append(10)
print(listas_multiplicacion)
