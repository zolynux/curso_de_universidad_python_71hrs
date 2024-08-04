# Se definen las variables "vacaciones" y "diadescanso" como booleanas.
vacaciones = False
diadescanso = True

# Se comprueba si no se está de vacaciones o de descanso.
if not (vacaciones or diadescanso):
    # Si no se cumple la condición, se imprime un mensaje indicando que hay deberes.
    print("Tiene deberes por hacer")

else:
    # Si se cumple la condición, se imprime un mensaje indicando que se puede asistir al juego.
    print("Puede asistir al juego")
