# Unpacking de Argumentos en Python
# *arg
numeros = [1, 2, 3]
print(numeros)
print(*numeros)

# **kwarg


# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f"Resultado suma: {a + b + c }")


sumar(*numeros)

# Desempaquetar con Variables
# Extrear algunas partes de unalista
mi_lista = [1, 2, 3, 4, 5, 6]
a, *b, c, d = mi_lista

print(a, b, c, d)

# Crear listas con el operador Unpacking
print(" Crear listas con el operador Unpacking ".center(60, "-"))

# Unir lista
lista1 = [1, 2, 3]
lista2 = [4, 5.6]
lista3 = [lista1, lista2]
print(f"Lista de listas: {lista3}")
lista3 = [*lista1, *lista2]
print(f"Unir listas: {lista3}")

# Unicr diccionario
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"D": 4, "E": 5, "F": 6}
dic3 = {**dic1, **dic2}
print(f"Unir diccionario: {dic3}")

# Construir una lista a partir de un str
lista = [*"HolaMundo"]
print(lista)
print(*lista, sep="")
