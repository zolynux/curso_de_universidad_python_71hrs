# Ejemplo 1
# Se define una variable "condicion" con valor booleano True
condicion = True  # True o False

# Si la condición es verdadera, se ejecuta el bloque "if"
if condicion:
    print(f"condición verdadera: {condicion}")

# Si la condición es falsa, se ejecuta el bloque "else"
else:
    print(f"condición falsa: {condicion}")


# Ejemplo 2
# Se define una variable "condicion" con un valor no booleano
condicion = "Hola"

# Se comprueba si la condición es igual a True
if condicion == True:
    print(f"condición verdadera: {condicion}")

# Se comprueba si la condición es igual a False
elif condicion == False:
    print(f"condición falsa: {condicion}")

# Si la condición no es ni True ni False, se ejecuta el bloque "else"
else:
    print(f"condición no reconocida: {condicion}")
