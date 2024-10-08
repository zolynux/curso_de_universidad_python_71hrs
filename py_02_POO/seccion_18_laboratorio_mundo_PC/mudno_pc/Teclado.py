from DispositvoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"ID: {self._id_teclado}, {super().__str__()}"


if __name__ == "__main__":
    teclado1 = Teclado("Genius", "USB")
    print(teclado1)
    teclado2 = Teclado("Gamer", "Bluetooth")
    print(teclado2)
