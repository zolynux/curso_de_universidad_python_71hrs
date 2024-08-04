import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de Grid")
# ventana.iconbitmap('img/icono.ico')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)


# Métodos de los eventos
def evento1():
    boton1.config(text="Botón 1 presionado")


def evento2():
    boton2.config(text="Botón 2 presionado")


def evento4():
    # fg = foreground (primer plano), bg = background (segundo plano)
    # Más adelante vamos a ver como cambiar a otro tema en Tkinter
    boton4.config(text="Botón 4 presionado", fg="blue", relief=tk.GROOVE, bg="yellow")


# Definimos los botones
boton1 = ttk.Button(ventana, text="Botón 1", command=evento1)
boton1.grid(row=0, column=0, sticky="NSWE")

# N (norte=arriba) , E (este=derecha), S (sur=abajo), W (oeste=izquierda)
boton2 = ttk.Button(ventana, text="Botón 2", command=evento2)
boton2.grid(row=1, column=0, sticky="NSWE")

# Botón 3
boton3 = ttk.Button(ventana, text="Botón 3")
boton3.grid(row=0, column=1, sticky="NSWE")

# Botón 4
boton4 = tk.Button(ventana, text="Botón 4", command="evento4")
boton4.grid(row=1, column=1, sticky="NSWE")

ventana.mainloop()
