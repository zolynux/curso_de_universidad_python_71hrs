from usuario_dao import UsuarioDAO
from logger_base import log
from usuario import Usuario

opcion = None

while opcion != 5:
    print(
        """
Opciones:
1. Listar usuarios
2. Agregar usuario
3. Modificar usuario
4. Eliminar usuario
5. Salir
-------------------------
"""
    )
    opcion = int(input("Escribe tu opción (1-5): "))
    print()
    match opcion:
        case 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        case 2:
            username_var = input("Escribe el nombre de usuario: ")
            password_var = input("Escribe el contraseña: ")
            usuario = Usuario(username=username_var, password=password_var)
            usuarios_insertados = UsuarioDAO.insertar(usuario)
            log.info(f"\nUsuario insertado: {usuarios_insertados}")
        case 3:
            if_usuario_var = int(input("Escribe el id_usuario a modificar: "))
            username_var = input("Escribe el nuevo username: ")
            password_var = input("Escribe el nuevo password: ")
            usuario = Usuario(if_usuario_var, username_var, password_var)
            usuarios_actualizados = UsuarioDAO.actualizar(usuario)
            log.info(f"\nUsuarios actualizados: {usuarios_actualizados}")
        case 4:
            id_usuario_var = int(input("Escribe el id_usuario a eliminar: "))
            usuario = Usuario(id_usuario=id_usuario_var)
            usuarios_eliminados = UsuarioDAO.eliminar(usuario)
            log.info(f"\nUsuarios eliminados: {usuarios_eliminados}")
        case 5:
            pass
        case _:
            log.error("\nIngresaste no es válida, deberías ingresar correctamente...\n")
else:
    log.info("Salimos de la aplicación.")
