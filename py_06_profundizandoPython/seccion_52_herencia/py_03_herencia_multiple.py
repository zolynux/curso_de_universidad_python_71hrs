# * Ejemplo de Herencia Simple en Parte 1
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._elementos!r})"


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()


# Lista solo acepta números
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f"No es un valor entero: {elemento}")

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)


# * Herencia Múltiple - Parte 1
# Lista de Enteros Ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


# * ------------------- Objectos ---------------------------

# * Lista Simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
print()

# * Lista Ordenada
lista_ordenada = ListaOrdenada([4, 3, 6, 9, 10, -1])
print(lista_ordenada)
lista_ordenada.agregar(-12)
print(lista_ordenada)
print(len(lista_ordenada))
print()

# * Lista Enteros
# ! Arroja un error no es número entero
# lista_entero = ListaEnteros(['hola', 1,3,4,-15])
lista_entero = ListaEnteros([1, 3, 4, -15])
print(lista_entero)
print()

# * Herencia Múltiple - Parte 1
# Lista enteros Ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4, 5, -1, 10, 14, -4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)

# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
print()
# * MRO - Method Resolution Order
"""nota:
Recuerden que también pueden ejecutar
paso a paso y verificar el mismo resultado
"""
print(ListaEnterosOrdenada.__mro__)
