# Uso del método format en Python

# Dar formato a un str
nombre = "Juan"
edad = 34
sueldo = 5000.00
# Placeholder = marcador de posición
mensaje = "Nombre {} Edad: {} Sueldo {:.2f}".format(nombre, edad, sueldo)
print(mensaje)

print("=" * 70)

mensaje = "Nombre {0} Edad: {1} Sueldo {2:.2f}".format(nombre, edad, sueldo)
print(mensaje)

print("=" * 70)

mensaje = "Sueldo {2:.2f} Edad: {1} Nombre {0}".format(nombre, edad, sueldo)
print(mensaje)

# Parte 2

print("=" * 70)

mensaje = "Nombre {n} Edad: {e} Sueldo {s:.2f}".format(n=nombre, e=edad, s=sueldo)
print(mensaje)

print("=" * 70)

diccionario = {"nombre": "Ivan", "edad": 35, "sueldo": 6000.00}
mensaje = "Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: {dic[sueldo]:.2f}.".format(
    dic=diccionario
)
print(mensaje)
