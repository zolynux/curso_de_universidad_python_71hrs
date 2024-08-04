# Se solicita al usuario que introduzca su edad
edad = int(input("Introduce tu edad: "))

# Se comprueba si la edad está en el rango de 20 a 29 o de 30 a 39 años
if (20 <= edad < 30) or (30 <= edad < 40):
    # Si la edad está en el rango, se imprime un mensaje
    print("Dentro de rango (20's) o (30's)")
else:
    # Si la edad no está en el rango, se imprime un mensaje
    print("No está dentro de los 20's ni 30's")
