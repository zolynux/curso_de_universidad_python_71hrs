# Acceso a atributos en python
# * Ejemplo atributos publicos, protegidos, privados


class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objecto = MiClase("Valor público", "Valor protegido", "Valor privado")
# Acceso al atributo público
print(objecto.publico)
# Modificar el valor público
objecto.publico = "Nuevo valor público"
print(objecto.publico)

# Acceso al atributo protegido
# solo dentro de la misma clase o clases hijas
print(objecto._protegido)
# Modificar atributo protegido
objecto._protegido = "Nuevo valor protegido"
print(objecto._protegido)

# Acceder al atributo privado
# print(objecto.__privado)
# Pero, convierte: objecto._MiClase__privado
print(objecto._MiClase__privado)
# Modificar atributo privado
objecto._MiClase__privado = "Nuevo valor privado"
print(objecto._MiClase__privado)


"""
Recordemos que para ellos hemos usado los decoradores
@property y @setter.nombre_propiedad
"""
