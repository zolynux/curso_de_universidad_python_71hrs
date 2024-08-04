# Expresión generadora (es un generador anónimo)
multiplicacion = (valor * valor for valor in range(4))

print(type(multiplicacion))

print()

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
#! Arroja error como StopIteration
# print(next(multiplicacion))

print()

# * También se puede pasar una expresión  generadora a una función (sin paréntesis)
import math

suma = sum(valor * valor for valor in range(4))
print(f"Resultado suma: {suma}")

print()

# * Expresiones Generadores con Listas en Python
# También podemos usar una lista o cualquier otro iterador
lista = ["Juan", "Perez"]
generador = (valor for valor in lista)
# Mostrar el Tipo de datos con generador
print(f"Tipo de datos generador: {type(generador)}")

print()

# Imprimimos a iterator el generador
print(next(generador))
print(next(generador))

print()

# Crear un string a partir de un generador creado a partir de una lista
lista = ["Karla", "Gomez"]
contador = 0


# Definimos una función para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador


# La primera para es el yield, la segunda es el for, entre paréntesis
generador = (f"{incrementar()}. {nombre}" for nombre in lista)
lista = list(generador)
print(lista)
cadena = ", ".join(lista)
print(f"Cadena generada: {cadena}")
