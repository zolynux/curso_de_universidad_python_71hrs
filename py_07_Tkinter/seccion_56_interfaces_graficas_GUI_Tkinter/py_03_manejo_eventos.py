# GUI - Graphical User Interface
# * Manejo de Botones en Python
# Tkinter - TK Interface
import tkinter as tk

# Importamos el módulo del tema de tkinder
from tkinter import ttk

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry("600x400")
# Cambiamos el nombre de la ventana
ventana.title("Hola mundo")
# Configuramos el ícono de la aplicación
ventana.iconbitmap("img/icono.ico")


# Creamos un método evento_click
def evento_click():
    boton1.config(text="Botón presionado")
    print("Ejecución del evento_click")
    # Creamos un nuevo botón y los mostramos
    boton2 = ttk.Button(ventana, text="Nuevo botón")
    boton2.pack()


# Creamos un botón (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text="Dar click", command=evento_click)
# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()
# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()
