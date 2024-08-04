from mudno_pc.Monitor import Monitor
from mudno_pc.Teclado import Teclado
from mudno_pc.Raton import Raton
from mudno_pc.Computadora import Computadora
from mudno_pc.Orden import Orden


monitor1 = Monitor("HP", 24)
teclado1 = Teclado("HP", "USD")
raton1 = Raton("HP", "USB")
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

monitor2 = Monitor("LG", 28)
teclado2 = Teclado("Gamer", "Bluetooth")
raton2 = Raton("Logi", "Bluetooth")
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)
