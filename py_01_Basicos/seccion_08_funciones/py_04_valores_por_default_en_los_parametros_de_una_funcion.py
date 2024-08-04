# def suma(a=0, b=0) -> int:
# def suma(a: int = 0, b: int = 0) -> int:
def suma(a=0, b=0):
    # return 'Saludo'
    return a + b


resutlado = suma()
print(f"Resultado sumar: {resutlado}")

print(f"Resultado sumar: {suma(2, 8)}")
