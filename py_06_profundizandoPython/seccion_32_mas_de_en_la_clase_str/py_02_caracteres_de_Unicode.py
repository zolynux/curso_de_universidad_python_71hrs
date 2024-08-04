# sección 32: Profundizando más en la clase str en Python
# Caracteres de Unicode en Python - parte 1
"""
Unicode es un set de caracteres universal, es decir,
un estándar en el que se definen todos los caracteres
necesarios para la escritura de la mayoría de los idiomas
hablados en la actualidad que se usan en la computadora.
"""

# Caracter de Unicode
# ASCII - American Standard Code for Information Interchange
"""
El código ASCII es un estándar para la representación
de caracteres en cualquier dispositivo electrónico

Unicode soporta muchos más caracteres que ASCII,
por ello Python utiliza Unicode para representar
sus caracteres
"""
print("Hola\u0020Mundo")
print("Notación simple", "\u0041")
print("Notación extendida", "\U00000041")
print("Notación hexadecimal", "\x41")

# Caracteres de Unicode en Python - Parte 2
print("Corazón:", "\u2665")
print("Cara sonriendo:", "\U0001f600")
print("Serpiente:", "\U0001f40d")
