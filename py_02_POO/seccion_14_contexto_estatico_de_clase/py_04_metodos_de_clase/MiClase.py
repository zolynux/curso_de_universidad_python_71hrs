class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # Métodos estáticos
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # Métodos de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


MiClase.metodo_clase()
