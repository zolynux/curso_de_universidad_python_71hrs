# Signals y slot
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Botón
        boton = QPushButton('Click Aquí')
        # Conectamos el evento checado (por default es False)
        boton.setCheckable(True)
        # Conectamos otro slot al evento checar
        boton.clicked.connect(self.evento_checar)
        # Conectamos el evento (signal) click con el slot (evento_click)
        boton.clicked.connect(self.evento_click)
        # Publicamos el botón
        self.setCentralWidget(boton)

    def evento_click(self):
        print('Has hecho click')

    def evento_checar(self, checar):
        print('Checado?', checar)


if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
