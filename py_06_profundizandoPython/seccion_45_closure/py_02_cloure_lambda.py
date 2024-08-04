# * Un closure es una función que defina a otra, y además la regresa
# * la función anidada puede acceder a las variables locales definidas
# * en la función principal o externa


# Función principal
def operacion(a, b):
    # 1. Definimos una función lambda interna o anidada y la retornamos
    return lambda: a + b


mi_función_closure = operacion(5, 2)
print(f"Resultado de la función closure: {mi_función_closure()}")

# Llamar la función regresada al vuelo
print(f"Resultado de la función closure al vuelo: {operacion(5, 4)()}")
