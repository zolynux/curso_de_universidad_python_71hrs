# Copiando Listas en Python

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f"Lista original: {numeros1}")

# Obtener el valor min y max de una lista
print(f"Valor mínimo: {min(numeros1)}")
print(f"Valor máximo: {max(numeros1)}")

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
# help(list.copy)
print(numeros1)
print(numeros2)

print("num2 = num1.copy()".center(60, "-"))

# El operador 'is' nos permite preguntar si una variable apunta a la misma referencia
print(f"Misma referencia? {numeros1 is numeros2}")
print(f"Misma contenido? {numeros1 == numeros2}")

print("num2 = list(num1)".center(60, "-"))

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f"Misma referencia? {numeros1 is numeros2}")
print(f"Misma contenido? {numeros1 == numeros2}")

print("num2 = num1[:]".center(60, "-"))

# slicing
numeros2 = numeros1[:]
print(f"Misma referencia? {numeros1 is numeros2}")
print(f"Misma contenido? {numeros1 == numeros2}")
