# Profundizando en el método join para cadenas

# help(str.join)

tupla_str = ("Hola", "Mundo", "Universidad", "Python")
mensaje = " ".join(tupla_str)
print(f"mensaje: {mensaje}")

lista_cursos = ["Java", "Python", "Angular", "Spring"]
mensaje = ", ".join(lista_cursos)
print(f"mensaje: {mensaje}")

cadena = "HolaMundo"
mensaje = ".".join(cadena)
print(f"mensaje: {mensaje}")

diccionario = {"nombre": "Juan", "apellido": "perez", "edad": "19"}
llaves = "-".join(diccionario.keys())
valores = "-".join(diccionario.values())
print(f"llaves: {llaves} Type: {type(llaves)}")
print(f"valores: {valores} Type: {type(valores)}")
