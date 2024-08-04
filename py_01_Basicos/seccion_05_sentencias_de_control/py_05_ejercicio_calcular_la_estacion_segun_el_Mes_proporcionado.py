# Se solicita al usuario que ingrese el número del mes (entre 1 y 12).
mes = int(input("Proporciona mes del año (1-12): "))

# Se inicializa la variable "estacion" a un valor vacío (similar a "null" en otros lenguajes).
estacion = None

# Se utiliza una serie de condicionales "if" para determinar la estación del año en función del mes ingresado.
if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "Mes incorrecto"

# Se imprime un mensaje con el mes y la estación correspondiente.
print(f"Para el mes {mes} la estación es: {estacion}")
