class Aritmetica:
    # DocString = Documentación de la clase en Python
    """
    Clase Aritmética para realizar las operaciones de sumar, restar, etc.
    """

    # Método dunder = double underscore (doble guión bajo)
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Método de instancia

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def division(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 3)
print(f"Operando A es {aritmetica1.operandoA} y B es {aritmetica1.operandoB}")
print(f"Suma: {aritmetica1.sumar()}")
print(f"Resta: {aritmetica1.restar()}")
print(f"Multiplicación: {aritmetica1.multiplicar()}")
print(f"División: {aritmetica1.division():.2f}")
