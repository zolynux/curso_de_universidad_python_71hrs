# Se solicita al usuario que proporcione los datos del libro.
print("Proporcione los siguientes datos del libro:")

# Se captura el nombre del libro como cadena de caracteres.
nombre = str(input("Proporciona el nombre del libro: "))

# Se captura el ID del libro como número entero.
id = int(input("Proporciona el ID: "))

# Se captura el precio del libro como número decimal.
precio = float(input("Proporciona el precio: "))

# Se captura si el envío es gratuito como cadena de caracteres.
gratuitos = str(input("Indica si el envío es gratuito (s/n): "))

# Se valida el valor de "gratuitos" y se asigna un mensaje según corresponda.
if gratuitos == "s" or gratuitos == "S":
    gratuitos = "Si disponible"
elif gratuitos == "n" or gratuitos == "N":
    gratuitos = "No disponible"
else:
    gratuitos = "No es válido, revise la información proporcionada."

# Se imprime un resumen de los datos del libro con formato.
print(
    f"""===============================
Nombre: {nombre}
ID: {id}
Precio: {precio}
Envío gratuito: {gratuitos}
==============================="""
)
