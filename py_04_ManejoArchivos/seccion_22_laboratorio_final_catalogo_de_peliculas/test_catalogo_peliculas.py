from dominio.Pelicula import Peliculas
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print(
            """
Opciones:
1. Agregar Película
2. Listar Películas
3. Eliminar Catálogo Películas
4. Salir
        """
        )
        opcion = int(input("Escribe tu opción (1 - 4): "))

        match opcion:
            case 1:
                nombre_pelicula = input("Proporciona el nombre de película: ")
                pelicula = Peliculas(nombre_pelicula)
                cp.agregar_pelicula(pelicula)
            case 2:
                cp.listar_peliculas()
            case 3:
                cp.eliminar_peliculas()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        opcion = None
    else:
        pass

else:
    print("Ya salimos de programa...")
