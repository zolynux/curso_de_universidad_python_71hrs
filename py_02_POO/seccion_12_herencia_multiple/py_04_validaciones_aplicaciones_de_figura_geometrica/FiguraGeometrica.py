class FiguraGeometrica:
    # Inicialización en los atributos
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erróneo ancho: {ancho} ")
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erróneo alto: {alto} ")

    # Método el ancho en get
    @property
    def ancho(self):
        return self._ancho

    # Método el alto en set
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erróneo ancho: {ancho}")

    @property
    def alto(self):
        return self._alto

    # Método el alto en set
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erróneo alto: {alto}")

    def __str__(self):
        return f"FiguraGeometrica: [Ancho: {self._ancho}, Alto: {self._alto}]"

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
