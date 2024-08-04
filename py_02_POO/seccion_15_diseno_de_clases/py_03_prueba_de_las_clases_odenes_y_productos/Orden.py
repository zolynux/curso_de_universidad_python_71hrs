from Producto import Producto


class Orden:
    contador_orden = 0

    @classmethod
    def generar_contador_orden(cls):
        cls.contador_orden += 1
        return cls.contador_orden

    def __init__(self, productos):
        self._id_orden = Orden.generar_contador_orden()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        producto_str = ""
        for producto in self._productos:
            producto_str += producto.__str__() + "|\n"
        return f"Orden: {self._id_orden} \nProductos: \n{producto_str}"


if __name__ == "__main__":
    producto1 = Producto("Camisa", 100.0)
    producto2 = Producto("Pantalón", 150.0)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
