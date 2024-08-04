# Alineado a la izquierda y la derecha en Pytthon

# Center - centrar un str
titulo = "Sitio Web de GlobalMentoring.com.mx"
# print(len(titulo)) # es 35
# print(titulo.center(50, '*'))
# print(len(titulo.center(50, '*'))) # es 50
print(titulo.center(len(titulo) + 10, "-"))

# Alinear a la izquierda:
# ljust - justifica a la izquierda
# print(titulo.ljust(50, '*'))
print(titulo.ljust(len(titulo) + 10, "-"))

# Alinear a la derecha
# rjust - justifica a la derecha
# print(titulo.rjust(50, '*'))
print(titulo.rjust(len(titulo) + 10, "-"))
