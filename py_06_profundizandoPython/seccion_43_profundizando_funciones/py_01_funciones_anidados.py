# Funciones Anidados


def calculadora(a, b, operacion="suma"):
    # Función anidado
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # Llamamos a la función anidado
    match operacion:
        case "sumar":
            print(f"Resultado sumar {sumar(a, b)}")
        case "restar":
            print(f"Resultado restar: {restar(a, b)}")
        case _:
            print("Ingresaste incorrecta")


calculadora(5, 6, "restar")
