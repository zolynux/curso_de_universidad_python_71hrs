# Se define la edad de un adulto
edadAdulto = 18

# Se solicita al usuario que ingrese su edad
edadPersona = int(input("Escribe tu edad: "))

# Se comprueba si la edad de la persona es mayor o igual a la edad adulta
if edadPersona >= edadAdulto:
    # Si la edad es mayor o igual, se imprime un mensaje indicando que la persona es un adulto
    print(f"La persona con edad {edadPersona} es un adulto")
else:
    # Si la edad es menor, se imprime un mensaje indicando que la persona es menor de edad
    print(f"La persona con edad {edadPersona} es menor de edad")
