class FiguraGeometrica:
    # Inicialización en los atributos
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    # Método el ancho en get
    @property
    def ancho(self):
        return self._ancho

    # Método el alto en set
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    # Método el alto en set
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f"FiguraGeometrica: [Ancho: {self._ancho}, Alto: {self._alto}]"
