# Manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float("inf")
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_negativo = float("-inf")
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito?: {math.isinf(infinito_negativo)}")

print("Módulo math.inf".center(50, "-"))

infinito_positivo = math.inf
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_negativo = -math.inf
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito: {math.isinf(infinito_negativo)}")

print("Módulo Decimal".center(50, "-"))

infinito_positivo = Decimal("Infinity")
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_negativo = Decimal("-Infinity")
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito: {math.isinf(infinito_negativo)}")
