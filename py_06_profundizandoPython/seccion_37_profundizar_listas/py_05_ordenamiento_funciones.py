# Ordenamiento de funciones de tipo Built-in
print("Buitl-in".center(60, "-"))

# Ordenamiento listas
lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 61, 70]]
print(f"lista original: {lista_listas}")
lista_listas.sort(key=len)
print(f"Ordenar lista : {lista_listas}")

print("sorted built-in".center(60, "-"))

# sorted built-in
# help(sorted)
nombres1 = ["Juan Carlos", "Karla", "Pedro", "Esperanza"]
print(f"nombres original : {nombres1}")
print("usar a 'sorted(variables)'")
nombres1 = sorted(nombres1)
print(f"nombres ordenados (ascendente): {nombres1}")
nombres1 = sorted(nombres1, reverse=True)
print(f"nombres ordenados (descendente): {nombres1}")

print(" La cantidad de caracteres 'len()' (largo) ".center(60, "-"))

# Ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1, key=len)
print(f"Ordenar Por la cantidad de caracteres: \n{nombres1}")

print(" built-in reversed ".center(60, "-"))

# buitl-in reversed
nombres1 = reversed(nombres1)
print(f"lista inverta: {list(nombres1)}")
