# * Ejercicio de Variables Globales en Python
# Definimos variable global
contador = 0


def mostrado_contador():
    print(contador)


def modificar_contador(c):
    global contador
    contador = c


modificar_contador(5)

mostrado_contador()
