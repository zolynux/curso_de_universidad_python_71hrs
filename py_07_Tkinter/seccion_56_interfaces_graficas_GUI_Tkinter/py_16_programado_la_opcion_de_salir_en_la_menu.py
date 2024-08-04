# * Programado la opción de Salir en el Menú
# Padding = Espacio que se deja entre los elementos
# i = inner (interno)
import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de Componentes")
# ventana.iconbitmap('img/icono.ico')


entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text="Aquí se mostrará el contenido de la caja de texto")
etiqueta1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto de label
    etiqueta1.config(text=entrada1.get())
    # Messagebox (cajas mensajes)
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo("Mensaje Informativo", mensaje1 + " Informativo")


def salir():
    ventana.quit()
    ventana.destroy()
    print("Salimos...")
    sys.exit()


def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    # tearoff = False para evitar que se separe el menú de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al menú de archivo
    submenu_archivo.add_command(label="Nuevo")
    # Agregar un separador
    submenu_archivo.add_separator()
    # Agregamos la opción de salir
    submenu_archivo.add_command(label="Salir", command=salir)
    # Agregamos el submenú al menú principal
    menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
    # submenu ayuda
    # nota: submenú de Ayuda con la opción: Acerca De
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al submenu
    submenu_ayuda.add_command(label="Acerca De")
    # Agregamos al menu principal este nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda, label="Ayuda")
    # Mostramos el menú en la ventana principal
    ventana.config(menu=menu_principal)


boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()
