# bool contiene los valores de True y False

# Tipos numéricos, False para 0, True demás valores
print(" Modulo bool con int y float ".center(50, "-"))

valor = 0
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = 15
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

# Tipo str, False para '', True demás valores
print(" Modulo bool con str ".center(50, "-"))

valor = ""
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = "Hola"
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

# Tipo colecciones, False para colecciones, True para todas las demás colecciones
print(" Modulo bool con list ".center(50, "-"))

# Lista
valor = []
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = [2, 3, 4]
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

print(" Modulo bool con tuple ".center(50, "-"))

# Tupla
valor = ()
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = (2, 3, 4)
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

print(" Modulo bool con dict ".center(50, "-"))

# Diccionario
valor = {}
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

valor = {"nombre": "juan", "apellido": "Perez"}
resultado = bool(valor)
print(f"Valor: {valor}, resultado: {resultado}")

# Tipo bool y sentencias de control
print(" Sentencias de control ".center(50, "-"))
print(" Sentencias IF/ELSE ".center(50, "-"))

variable = ""
if bool(variable):
    print("Regreso verdadero")
else:
    print("Regreso falso")

if variable:
    print("Regreso verdadero")
else:
    print("Regreso falso")

print(" Sentencias WHILE ".center(50, "-"))

while bool(variable):
    print("ejecuta ciclo while regreso verdadero y debe usar el break")
    break
else:
    print("Fin ciclo while regreso falso")
