"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y vicevera.
"""


# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Realizamos algunos pruebas de conversión

celsius = float(input("Proporciona su valor en celsius: "))
resultado = celsius_fahrenheit(celsius)
# Imprimimos el resultado
print(f"{celsius} C a F: {resultado:.2f}")

# Realizamos la prueba de grado fahrenheit a celsius
fahrenheit = float(input("Proporcione su valor en fahrenheit: "))
# Imprimimos el resultado
print(f"{fahrenheit} F a C: {resultado:.2f}")
