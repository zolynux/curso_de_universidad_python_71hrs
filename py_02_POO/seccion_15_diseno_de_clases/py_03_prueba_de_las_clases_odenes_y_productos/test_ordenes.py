from Orden import Orden
from Producto import Producto

producto1 = Producto("Camisa", 100.0)
producto2 = Producto("Pantalón", 150.0)
producto3 = Producto("Calcetines", 50.0)
producto4 = Producto("Blusa", 70.0)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f"Total Orden: {orden1.calcular_total()}")
