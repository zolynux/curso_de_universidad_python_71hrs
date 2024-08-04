# sección 32: Profundizando más en la clase str en Python
# Caracteres de Escape en Python

# Caracteres de escape
resultado = "Hola ' Mundo"
print(f"Resultado: {resultado}")

# Backspace = retroceso de caracter
resultado = "Se va a eliminar el punto.\b\b\b"
print(f"Resultado: {resultado}")

# Caracter \ = retroceso de caracter
resultado = "c:\\directorio\\juan"
print(f"Resultado: {resultado}")

# raw string
resultado = r"Cadena con \n salto de línea"
print(f"Resultado: {resultado}")
resultado = r"c:\directorio\juan"
print(f"Resultado: {resultado}")
