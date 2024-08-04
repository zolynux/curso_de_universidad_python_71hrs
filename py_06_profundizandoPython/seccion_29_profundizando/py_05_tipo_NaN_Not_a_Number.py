import math
from decimal import Decimal

# Tipo NaN (Not a Number) en Python
# NaN - Not a Number (no es un número)
# NaN no es sensible a mayúsculas/minúsculas
# NaN no es un tipo de dato numérico indefinido

print("Módulo Math".center(50, "-"))

a = float("NaN")
print(f"a: {a}")
print(f"Es NaN (Not a Number)?: {math.isnan(a)}")

print("Módulo Decimal".center(50, "-"))

a = Decimal("NaN")
print(f"a: {a}")
print(f"Es NaN (Not a Number)?: {math.isnan(a)}")
