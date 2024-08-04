#
# * Manejo de Etiquetas (Labels) en Tkinter
# Padding = Espacio que se deja entre los elementos
# i = inner (interno)
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de Componentes")
# ventana.iconbitmap('img/icono.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada_var1 = tk.StringVar(value="Valor por default")
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)


# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text="Aquí se mostrará el contenido de la caja de texto")
etiqueta1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto de label
    etiqueta1.config(text=entrada_var1.get())


# Creamos un botón
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
