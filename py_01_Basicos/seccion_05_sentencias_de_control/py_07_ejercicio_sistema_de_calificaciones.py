"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está 9 y 10: imprimir una A
Si está 8 y menor a 9: imprimir una B
Si está 7 y menor a 8: imprimir una C
Si está 6 y menor a 7: imprimir una D
Si está 0 y menor a 6: imprimir una F
Cualquier otro valor dee imprimir: Valor incorrecto
Por ejemplo
Proporciona un valor entre 0 y 10:
A
"""

"""
Sistema de calificaciones:
- 9-10: A
- 8-9: B
- 7-8: C
- 6-7: D
- 0-6: F
- Cualquier otro valor: Incorrecto
"""

# Se solicita al usuario una calificación
calificacion = int(input("Proporciona una calificación entre 0 y 10: "))

# Se define una variable para el mensaje
mensaje = None

# Se utiliza una estructura condicional para determinar la calificación
if 9 <= calificacion <= 10:
    mensaje = "A"
elif 8 <= calificacion < 9:
    mensaje = "B"
elif 7 <= calificacion < 8:
    mensaje = "C"
elif 6 <= calificacion < 7:
    mensaje = "D"
elif 0 <= calificacion < 6:
    mensaje = "F"
else:
    mensaje = "El valor incorrecto. Debes proporcionar entre 0 y 10."

# Se imprime la calificación y el mensaje
print(f"Proporcionado la calificación {calificacion} es {mensaje}")
