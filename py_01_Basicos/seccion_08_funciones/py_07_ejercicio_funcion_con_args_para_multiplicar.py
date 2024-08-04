"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos varaibles *args como parámetro en la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""


def multiplicar_valor(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


print(f"resultado: {multiplicar_valor(2,3,4,5)}")
