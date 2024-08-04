# Se solicita al usuario que ingrese un valor numérico
a = int(input("Escribe un valor numérico: "))

# Se comprueba si el valor es par
if a % 2 == 0:
    # Se imprime un mensaje indicando que el valor es par
    print(f"El valor de a = {a} es número par")
else:
    # Se imprime un mensaje indicando que el valor es impar
    print(f"El valor de a = {a} es número impar")
