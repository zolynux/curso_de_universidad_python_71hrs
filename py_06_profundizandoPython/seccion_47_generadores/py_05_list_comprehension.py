numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si misma
for numero in numeros:
    # Revisamos si es un número par
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(f"Lista Pares: {lista_pares}")

# * Hacemos lo mismo pero con list comprehensión
# [expresión for var in colección if condicional]
# La condición de if es opcional
lista_pares = []
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f"Lista pares con list comprehensions: {lista_pares}")
