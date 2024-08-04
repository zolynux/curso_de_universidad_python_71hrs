"""
Calcula el área y el perímetro de un rectángulo.

**Instrucciones:**

1. El usuario ingresa el alto y ancho del rectángulo.
2. Se calcula el área y el perímetro.
3. Se imprime el área y el perímetro en formato legible.

**Fórmulas:**

* Área: alto * ancho
* Perímetro: (alto + ancho) * 2
"""

# Se solicita el alto del rectángulo al usuario
alto = int(input("Proporciona el alto del rectángulo: "))

# Se solicita el ancho del rectángulo al usuario
ancho = int(input("Proporciona el ancho del rectángulo: "))

# Se calcula el área del rectángulo
area = alto * ancho

# Se calcula el perímetro del rectángulo
perimetro = (alto + ancho) * 2

# Se imprime el área y el perímetro del rectángulo
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
