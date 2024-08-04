class Producto:
    contador_producto = 0

    @classmethod
    def generar_contador_producto(cls):
        cls.contador_producto += 1
        return cls.contador_producto

    def __init__(self, nombre, precio):
        self._id_producto = Producto.generar_contador_producto()
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    # @precio.setter
    # def precio(self, precio):
    #     self._precio = precio

    def __str__(self):
        return (
            f"ID: {self._id_producto} | Nombre: {self._nombre} | Precio: {self._precio}"
        )


if __name__ == "__main__":
    producto1 = Producto("Camisa", 100.0)
    print(producto1)
    producto2 = Producto("Pantalón", 120.0)
    print(producto2)
