#
# * Profundizando en tuplas en Python.

# Declarar variables
a, b = "Hola", "Adios"
print(a, b)
# swap (intercambio)
a, b = b, a
print(a, b)


# regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)


min, max = minmax([1, 2, 3, 4, 5])  # ejemplo list(ragne(1,6))
print(f"Valor min: {min}, valor max: {max}")

# Regresa la suma de una tupla
resultado = sum((1, 2, 3, 4, 5))
print(f"Resultado suma: {resultado}")


def sumar(*args):
    return sum(args)


resultado = sumar(1, 2, 3, 4, 5)
print(f"Resultado suma de función: {resultado}")
