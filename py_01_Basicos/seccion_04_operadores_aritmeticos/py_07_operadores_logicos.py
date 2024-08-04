# Demostración de operadores lógicos en Python

# Operador AND

# Ambos valores True
a = True
b = True
resultado = a and b
print(f"a = {a} y b = {b}.")
print(f"and: {resultado}")  # True (solo si ambos son True)

# Un valor False
a = True
b = False
resultado = a and b
print(f"a = {a} y b = {b}.")
print(f"and: {resultado}")  # False

# Ambos valores False
a = False
b = False
resultado = a and b
print(f"a = {a} y b = {b}.")
print(f"and: {resultado}")  # False (solo si ambos son True)

# Operador OR

# Ambos valores True
a = True
b = True
resultado = a or b
print(f"a = {a} y b = {b}.")
print(f"or: {resultado}")  # True (al menos uno debe ser True)

# Un valor True
a = True
b = False
resultado = a or b
print(f"a = {a} y b = {b}.")
print(f"or: {resultado}")  # True

# Ambos valores False
a = False
b = False
resultado = a or b
print(f"a = {a} y b = {b}.")
print(f"or: {resultado}")  # False (ninguno es True)

# Operador NOT

# Valor True
a = True
resultado = not a
print(f"a = {a}.")
print(f"not: {resultado}")  # False (invierte el valor)

# Valor False
a = False
resultado = not a
print(f"a = {a}.")
print(f"not: {resultado}")  # True (invierte el valor)
