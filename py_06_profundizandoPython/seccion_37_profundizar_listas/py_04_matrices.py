# Matrices en Python

print("Matrices".center(60, "-"))

# Matricees en Python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f"Matriz original: {matriz}")
print("Ejemplo de matrices: matriz[renglón][columna]")
print(f"Renglón 0, Columna 0: {matriz[0][0]}")
print(f"Renglón 2, Columna 2: {matriz[2][2]}")

print(f"Matriz original   : {matriz}")
matriz[2][0] = 65
print(f"Matriz modificado : {matriz}")
