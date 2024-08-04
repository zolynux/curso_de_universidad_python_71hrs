edad = int(input("Introduce tu edad: "))
"""
veintes = edad >= 20 and edad < 30
print(f"vientes: {veintes}")
treintas = edad >= 30 and edad < 40
print(f"treintas: {treintas}")

if veintes or treintas:
    # print("Dentro de rango (20's) o (30's)")
    if veintes:
        print("Dentro de los 20's")
    elif treintas:
        print("Dentro de los 30's")
    else:
        print("Fuera de rango")
else:
    print("No está dentro de los 20's ni 30's")

"""

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    # print("Dentro de rango (20's) o (30's)")
    if edad >= 20 and edad < 30:
        print("Dentro de los 20's")
    elif edad >= 30 and edad < 40:
        print("Dentro de los 30's")
    else:
        print("Fuera de rango")
else:
    print("No está dentro de los 20's ni 30's")
