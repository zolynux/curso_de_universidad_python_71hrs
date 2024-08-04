# Definir una tupla

frutas = ("Naranja", "Platáno", "Guayaba")
print(frutas)
# saber el largo
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Navegación inversa
print(frutas[-1])
# Acceder a un rango
print(frutas[0:2])  # sin incluir el último índice
for fruta in frutas:
    print(fruta, end=" ")
# Cambiar valor tupla
# frutas[0] = 'Pera' # es un error en tupla
# print(frutas)
frutaLista = list(frutas)
frutaLista[0] = "Pera"
frutas = tuple(frutaLista)
print("\n", frutas)
# Eliminar la tupla
del frutas
print(frutas)
