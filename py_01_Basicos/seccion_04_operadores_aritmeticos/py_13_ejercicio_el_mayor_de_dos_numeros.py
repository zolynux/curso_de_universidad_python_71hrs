"""
Instrucciones de tareas:
solicitar al usuario dos valores, y determinar cuál número es el mayor
solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
"""

# Solicitar al usuario dos valores: numero1 y numero2 (enteros)

print("Solicitar al usuario dos valores:")
num1 = int(input("Proporciona el primer numero: "))
num2 = int(input("Proporciona el segundo numero: "))

# Comparar los dos números y determinar el mayor
# Se utiliza una estructura condicional "if"

if num1 > num2:
    # Imprimir si el primer número es mayor
    print(f"Primer número {num1} es mayor")
else:
    # Imprimir si el segundo número es mayor
    print(f"Segundo número {num2} es mayor")
