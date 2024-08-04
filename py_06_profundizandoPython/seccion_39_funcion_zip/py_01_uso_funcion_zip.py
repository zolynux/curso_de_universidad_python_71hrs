# Uso de la Función zip
# zip significa comprimir
# help(zip)
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
mezcla = zip(numeros, letras)
print(mezcla)
print(list(mezcla))
print(tuple(zip(numeros, letras)))
