def listarTermino(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave}: {valor}")


listarTermino(IDE="Integrated Development Environment", PK="Primary Key")
listarTermino(DBMS="Database Management System")
