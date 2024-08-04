# Se define la variable "condicion" con un valor booleano (True o False)
condicion = True  # True o False

# Se evalúa la condición
if condicion:
    # Si la condición es True, se ejecuta este bloque
    print(f"condición verdadera: {condicion}")
else:
    # Si la condición es False, se ejecuta este bloque
    print(f"condición falsa: {condicion}")


# Se define la variable "condicion" con un valor de tipo cadena
condicion = "Hola"

# Se evalúa la condición
if condicion == True:
    # Si la condición es True, se ejecuta este bloque
    print(f"condición verdadera: {condicion}")
elif condicion == False:
    # Si la condición es False, se ejecuta este bloque
    print(f"condición falsa: {condicion}")
else:
    # Si la condición no es True ni False, se ejecuta este bloque
    print(f"condición no reconocida: {condicion}")
