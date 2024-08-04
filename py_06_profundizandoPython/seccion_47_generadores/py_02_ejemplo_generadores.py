# * Generador de números del 1 al 5
def generador_numeros():
    for numero in range(1, 6):
        yield numero
        print("Se reanuda la ejecución de la función")


# * Utilizamos el generador
generador = generador_numeros()
print(f"Objeto generador: {generador}")
print(type(generador))

print()

# Consumimos los valores del generador
for valor in generador:
    print(f"Número producido: {valor}")

print()

# Consumir a demanda
generador = generador_numeros()
try:
    print(f"Consumimos a demada: {next(generador)}")
    print(f"Consumimos a demada: {next(generador)}")
    print(f"Consumimos a demada: {next(generador)}")
    print(f"Consumimos a demada: {next(generador)}")
    print(f"Consumimos a demada: {next(generador)}")
    print(f"Consumimos a demada: {next(generador)}")
except StopIteration as e:
    print(f"Error al consumir generador {e}")

print()

# Otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f"Impresión valor generador desde while: {valor}")
    except StopIteration as e:
        print("Se terminó de iterar el generado")
        break
