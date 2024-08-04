# Uso de f-string (Template Literal) en Python

# Uso del método format-string en Python

# Dar formato a un str
nombre = "Juan"
edad = 34
sueldo = 5000
# A esto se le conoce como interpolación (agregar una expresión o variable en un placeholder)
mensaje = f"Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo:.2f}"
print(mensaje)

print("=" * 70)

# Método print
print(nombre, edad, sueldo, sep=", ")
