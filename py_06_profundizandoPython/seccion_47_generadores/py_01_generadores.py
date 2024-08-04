"""Generadores
Es un función especial, retorna una secuencia de valores
suspende la ejecución de la función 'yield' (producir) (no se usar 'return')
yield = producir
"""


def generador():
    yield 1
    print("Se reanuda la ejecución")
    yield 2
    print("Se reanuda la ejecución")
    yield 3


# Consumimos el generador a demada
gen = generador()
# Con cada llama consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
#! Si tratamos de consumir más valores de los que produce el generador
#! Lanza un error de StopItreation
# print(next(gen))

print()

# * Consumiendo los valores del generador con un ciclo 'for'
generador()
for valor in generador():
    print(f"Número generado: {valor}")
