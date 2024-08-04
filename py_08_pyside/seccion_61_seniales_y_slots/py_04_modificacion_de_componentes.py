# Signals y slot
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Botón
        self.boton = QPushButton('Click Aquí')
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        # Publicamos el botón
        self.setCentralWidget(self.boton)

    def evento_click(self):
        # Cambiar el texto de botón y el título de la ventana
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo título de la Aplicación')
        print('Evento_clicked')


if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
