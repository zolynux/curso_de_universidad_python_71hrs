"""
Este programa solicita al usuario su edad y muestra un mensaje
de acuerdo a la etapa de vida en la que se encuentra:

0 - 10: la infancia es increíble
10 - 20: Muchos cambios y mucho estudio
20 - 30: Amor y comienza el trabajo

cualquier otro valor: Etapa de vida no reconocida.
"""

# Se imprime un mensaje al usuario
print("Proporciona las etapas de vida según edad...")

# Se solicita al usuario que ingrese su edad
edad = int(input("Proporciona el número de edad (0 - 30): "))

# Se define una variable para almacenar el mensaje
mensaje = None

# Se utiliza una estructura condicional para determinar el mensaje
# de acuerdo a la edad ingresada
if 0 <= edad < 10:
    mensaje = "La infancia es increíble..."
elif 10 <= edad < 20:
    mensaje = "Muchos cambios y mucho estudio"
elif 20 <= edad <= 30:
    mensaje = "Amor y comienza el trabajo"
else:
    mensaje = "Etapa de vida no reconocida"

# Se imprime la edad y el mensaje al usuario
print(f"Tu edad es: {edad}, {mensaje}")
