# Profundizando en Set en Python
# * Parte 1
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmatables
# conjunto = {[1,2], [3,4]}
conjunto = {"Juan", True, 18.0}  # Es un inmutable
print(conjunto)
# set vacío
conjunto = {}  # Genera un 'dict' vacío
# print(type(conjunto)) # es 'class dict'
# set vacío correcto
conjunto = set()
print(conjunto)  # set()
print(type(conjunto))  # <class 'set'>
# * Mutable
conjunto.add("Juan")
print(conjunto)  # {'Juan'}
# Contiene valores únicos
conjunto.add("Juan")
print(conjunto)  # {'Juan'}
conjunto = set([4, 5, 7, 8, 4])
print(conjunto)
# * Parte 2
# Podemos agregar más elementos on incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20, 30, 40, 40])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencia)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f"Es igual en contenido?: {conjunto == conjunto_copia}")
print(f"Es la misma  referencia?: {conjunto is conjunto_copia}")
