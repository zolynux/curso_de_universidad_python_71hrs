def listarNombres(
    # *args,  # args = argumentos
    *nombres,  # argumento *nombres puede convertir tupla en función
):  # y recordar que una tupla es inmutable (no se pueden modificar)
    for nombre in nombres:
        print(nombre)


listarNombres("Juan", "Karla", "María", "Ernesto")
listarNombres("Laura", "Carlos")
