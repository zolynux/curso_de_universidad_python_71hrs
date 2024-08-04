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
