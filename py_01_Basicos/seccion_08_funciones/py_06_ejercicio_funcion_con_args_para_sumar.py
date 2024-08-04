"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos varaibles *args como parámetro en la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""


# Definimos nuestra función para sumar valor
def sumar_valores(*args):
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado


# LLamada la función
print(sumar_valores(3, 5, 9, 4, 6))
