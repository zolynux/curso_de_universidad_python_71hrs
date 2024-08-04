# Se solicita al usuario que ingrese un valor
valor = int(input("Escribe el valor: "))

# Se definen los valores mínimo y máximo del rango
valorMinimo = 0
valorMaximo = 5

# Se evalúa si el valor está dentro del rango
dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

# Se imprime un mensaje según el resultado de la evaluación
if dentroRango:
    print(f"El valor {valor} está dentro de rango")
else:
    print(f"El valor {valor} está fuera de rango")
