resultado = None

# a = '10'
a = 10
# b = 2
b = 0

try:
    resultado = a / b

except ZeroDivisionError as e:
    print(f"ZeroDivisionErro - Ocurrió un error: {e}, {type(e)}")
except TypeError as e:
    print(f"TypeError - Ocurrió un error: {e}, {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrió un error: {e}, {type(e)}")


print(f"Resultado: {resultado}")
print(f"Continuamos...")
