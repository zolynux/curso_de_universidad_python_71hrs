# * Un ejemplo simila con dos condiciones (las condiones son opcionales)
# Solo se agregar el valor a la lista cuando el valor cumple ambas condiciones
# es decir, debe ser divisble entre 2  y divisible entre 6
pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]

print()

# * Agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f"Pares: {lista_pares}\nImpares: {lista_impares}")

print()

# El mismo ejercicio usando list comprehension
lista_pares = []
lista_impares = []
[
    lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero)
    for numero in range(10)
]
print(f"Pares: {lista_pares}\nImpares: {lista_impares}")
