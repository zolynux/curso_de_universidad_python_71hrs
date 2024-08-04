# :None: es ausencia de valor, o null en otros lenguajes
variable = None

if bool(variable):
    print("Se considera verdadera")
else:
    print("Se considera falsa")

print(type(variable))

"""
ocho formas de generar un bool False en Python
1. Comilla simple o doble ''/"" (cadena vacía)
2. Lista vacía []
2. Tupla vacía ()
2. Diccionario vacía {}
2. Entero 0
6. Flotante 0.0
7. bool False
8. None
"""
