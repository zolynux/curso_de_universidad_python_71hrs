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


# * Operaciones Algebraicas con Set - Parte 1
print(" Operaciones Algebraicas con Set - Parte 1 ".center(60, "-"))
# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {"Juan", "Karla", "Pedro", "María"}
pelo_rubio = {"Lorenzo", "Laura", "Marco"}
ojos_cafe = {"Karla", "Laura"}
menores_30 = {"Juan", "Karla", "María"}
# Todos con 'ojos_cafe y pelo_rubio' (Unión) (No se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# * Operaciones Algebraicas con Set - Parte 2
print(" Operaciones Algebraicas con Set - Parte 2 ".center(60, "-"))

# (Intersection) Sólo las personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# (difference) Pelo negro sin ojo cafe
# Las personas que se encuentran en el primer set pero No en el segundo
print(pelo_negro.difference(ojos_cafe))

# (differencia simétrica) Pelo negro u ojos vafes, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# * Preguntas Con Set

# Preguntar si un set está contenido en otro (subset)
# revisamos si los elementos del primer set están contenidos en el segundo set
print("subset:", menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set están contenidos en el segundo set
print("superset:", menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tiene pelo rubio (distjoint)
print("distjoint:", pelo_negro.isdisjoint(pelo_rubio))
