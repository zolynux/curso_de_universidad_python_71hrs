import inspect

# * Decoradores de clase en Python - Parte 1
# Permiten transformar de manera programática nuestra clase
# Es similar a los decoradores de funcion (es metaprogramación)


def decorador_repr(cls):
    print("1. Se ejecuta decorador")
    print(f"Recibimos el objeto de clase: {cls.__name__}")
    # * end - Parte 1

    # * Decoradores de clase en Python - Parte 2
    # Resivamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if "__init__" not in atributos:
        raise TypeError(f"{cls.__name__} no ha sobreescrito el método __init__")

    firma_init = inspect.signature(cls.__init__)
    print(f"Firma método __ini__: {firma_init}")

    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f"Parámetros init: {parametros_init}")
    # * end - Parte 2
    # * Decoradores de clase en Python - Parte 3
    # Resivamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in para preguntar si
        # se está utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(
                f"No existe un método property para el parámetro: {parametro}"
            )

    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # * end - Parte 3
        # * Decoradores de clase en Python - Parte 4
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f"Nombre clase: {nombre_clase}")

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresion Generadora, crear nombre_art=valor_atr
        generador_arg = (
            f"{nombre}={getattr(self, nombre)!r}" for nombre in parametros_init
        )
        # Lista del generador
        lista_arg = list(generador_arg)
        print(f"Lista del generador: {lista_arg}")
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ", ".join(lista_arg)
        print(f"Resultado de ejecutar método repr: {argumentos}")
        # Creamos la forma del método __repr__, sin su nombre,
        resultado_metodo_repr = f"{nombre_clase}({argumentos})"
        print(f"Resultado método repr: {resultado_metodo_repr}")
        return resultado_metodo_repr

    # * end - Parte 4

    # * Decoradores de clase en Python - Parte 3

    # Agrega dinámicamente el método repr a nuestra clase
    setattr(cls, "__repr__", metodo_repr)
    # * end - Parte 3

    # * Decoradores de clase en Python - Parte 1
    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print("2. Se ejecuta el inicializador")
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self) -> str:
    #     return f'{self.__class__.__name__}({self._nombre}, {self._apellido})'


# * end - Parte 1

print()

# * Decoradores de clase en Python - Parte 1
persona1 = Persona("Juan", "Perez", edad=23)
# * end - Parte 1

# * Decoradores de clase en Python - Parte 3
print(persona1)
# * end - Parte 3

print()

# * Decoradores de clase en Python - Parte 4
persona2 = Persona("Karla", "Gomez", edad=19)
print(persona2)
# * end - Parte 4

print()

# * Decoradores de clase en Python - Parte 5
# Tiene los métodos de propiedad nombre, apellido, edad, repr
print(dir(Persona))

print()

# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)
# * end - Parte 5
