print(" Funciones lambda - Parte 1 ".center(60, "-"))
# * Funciones lambda
# Son funiones anónimas, y son pequeñas (una línea de código)

#! No es posible asignar una función a una variable
# mi_funcion = def sumar(a, b): return a + b #! Es un error que no puede acceder una variable a la función

"""_lambda
* Con una función lambda (anónima, sin nombre, y una sola línea de código)
* No se necesita agregar paréntesis para los parámetros
* No se necesita usar la palabra return, pero sí debe regresar una expresión
"""
mi_función_lambda = lambda a, b: a + b

resultado = mi_función_lambda(4, 6)
print(f"Resultado sumar con función lambda: {resultado}")

print(" Funciones lambda - Parte 2 ".center(60, "-"))

# Función lambda que no recibe argumentos (debemos regresar una expresión válida)
mi_función_lambda = lambda: "Funcion sin argumentos"
print(f"Llamar función lambda sin argumentos: {mi_función_lambda()}")

# Función lambda con parámetros por default
mi_función_lambda = lambda a=2, b=3: a + b
print(f"Resultado argumentos por default: {mi_función_lambda()}")
print(f"Resultado argumentos modificados: {mi_función_lambda(4, 6)}")

# Función lambda con argumentos variables *args y **kwargs
mi_función_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f"Resultado argumentos variables: {mi_función_lambda(1,2,3, a=5, b=6)}")

# * Funciones lambda con argumentos, argumentos variables y valores por default
mi_función_lambda = (
    lambda a, b, c=3, *args, **kwargs: a + b + c + len(args) + len(kwargs)
)
print(f"Resultado función lambda: {mi_función_lambda(1,2,4, 5,6,7, e=5,f=7)}")
