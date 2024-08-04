# GUI - Graphical User Interface
# * Introducción a Tkinter.
# Tkinter - TK Interface
import tkinter as tk

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry("600x400")
# Cambiamos el nombre de la ventana
ventana.title("Nueva ventana")
# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()
