# Se solicita al usuario un valor entre 1 y 3
numero = int(input("Proporciona un valor entre 1 y 3: "))

# Se declara una variable para almacenar el texto del número
numeroTexto = ""

# Se evalúa el valor de "numero"
if numero == 1:
    # Se asigna el texto "Número uno" a "numeroTexto"
    numeroTexto = "Número uno"
elif numero == 2:
    # Se asigna el texto "Número dos" a "numeroTexto"
    numeroTexto = "Número dos"
elif numero == 3:
    # Se asigna el texto "Número tres" a "numeroTexto"
    numeroTexto = "Número tres"
else:
    # Se asigna el texto "Valor fuera de rango" a "numeroTexto"
    numeroTexto = "Valor fuera de rango"

# Se imprime el valor de "numero" y "numeroTexto"
print(f"Número proporcionado: {numero} - {numeroTexto}")
