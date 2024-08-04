## Manejo de archivos en Python

Python ofrece una amplia variedad de herramientas para trabajar con archivos de texto y binarios. A continuación se presenta un resumen de las principales funcionalidades:

**Lectura de archivos:**

* La función `open()` permite abrir un archivo en modo lectura (`"r"`) y obtener un objeto "file".
* El método `read()` del objeto "file" permite leer el contenido del archivo como una cadena.
* El método `readlines()` del objeto "file" permite leer el contenido del archivo como una lista de líneas.

**Escritura en archivos:**

* La función `open()` permite abrir un archivo en modo escritura (`"w"`) o escritura y lectura (`"w+"`) y obtener un objeto "file".
* El método `write()` del objeto "file" permite escribir una cadena en el archivo.
* El método `writelines()` del objeto "file" permite escribir una lista de líneas en el archivo.

**Otras funcionalidades:**

* La función `os.path.exists()` permite verificar si un archivo existe.
* La función `os.path.isfile()` permite verificar si un archivo es un archivo regular.
* La función `os.path.isdir()` permite verificar si un archivo es un directorio.
* La función `os.remove()` permite eliminar un archivo.

**Ejemplo:**

```python
# Lectura de un archivo

archivo = open("ejemplo.txt", "r")
contenido = archivo.read()
archivo.close()

print(contenido)

# Escritura en un archivo

archivo = open("ejemplo.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()
```

**Recursos adicionales:**

* Manejo de archivos en Python - El libro de Python: [se quitó una URL no válida]
* Tutorial: Manejo de archivos en Python: [se quitó una URL no válida]
* Documentación oficial de Python: [https://www.tutorialspoint.com/python/python_files_io.htm](https://www.tutorialspoint.com/python/python_files_io.htm)

**Consejos:**

* **Utiliza el modo adecuado al abrir un archivo:** Si solo necesitas leer el archivo, usa el modo `"r"`. Si necesitas escribir en el archivo, usa el modo `"w"` o `"w+"`.
* **Cierra los archivos después de usarlos:** Esto libera recursos del sistema y evita errores.
* **Maneja las excepciones:** Es importante manejar las excepciones que puedan ocurrir al trabajar con archivos, como errores de apertura o escritura.
* **Utiliza las herramientas adecuadas:** Python ofrece una amplia variedad de módulos y bibliotecas para trabajar con archivos específicos, como CSV, JSON o XML.