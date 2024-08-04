class Orden:
    contando_ordenes = 0

    def __init__(self, computadoras):
        Orden.contando_ordenes += 1
        self._id_orden = Orden.contando_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadora_str = ""
        for computadora in self._computadoras:
            computadora_str += computadora.__str__()

        return f"""
        Orden: {self._id_orden}
        Computadoras: {computadora_str}
"""
