# with open('prueba.txt', 'r', encoding='utf8') as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo:
    # Esto se conoce como Context Manager o
    # Administrador de Recursos
    print(archivo.read())
