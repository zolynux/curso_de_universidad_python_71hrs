"""
Imprimir números de 5 a 1 manera descendente usando funciones recursivos.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir.
3
2
1

Si se paran valores negativos no imprime nada
"""


def imprimir_numero_recursivo(numeros):
    if numeros >= 1:
        print(numeros)
        imprimir_numero_recursivo(numeros - 1)
    elif numeros == 0:
        return
    elif numeros <= 0:
        print("El valor incorrecto...")


numeros = int(input("Propociona el valor del número: "))
imprimir_numero_recursivo(5)
