from py_06_NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    if a == b:
        # raise = nos permite lanzar o arrojar una excepción
        raise NumerosIdenticosException("número idénticos")
    resultado = a / b
except ZeroDivisionError as e:
    print(f"ZeroDivisionErro - Ocurrió un error: {e}, {type(e)}")
except TypeError as e:
    print(f"TypeError - Ocurrió un error: {e}, {type(e)}")
except ValueError as e:
    print(f"TypeError - Ocurrió un error: {e}, {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrió un error: {e}, {type(e)}")
else:
    print("No se arrojó ninguna excepción...")
finally:
    print("Ejecución del bloque finally")


print(f"Resultado: {resultado}")
print(f"Continuamos...")
