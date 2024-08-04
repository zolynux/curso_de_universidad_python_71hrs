# Alcance de variables (scope) en Python
print(" Alcance de Variables - Parte 1 ".center(60, "-"))

var_global = "Variable global"


def imprimir():
    # Acceder a una variable global
    global var_global
    print(f"Variable global desde función: {var_global}")
    # Definición de variable local
    var_local = "Variables local"
    print(f"Variable local desde función: {var_local}")

    # var_global =  'Nuevo valor desde función' # arroja error sin global
    var_global = "Nuevo valor variable global"

    def funcion_anidada():
        print(f"Variable local dentro función anidada: {var_local}")

    funcion_anidada()


imprimir()

print(f"Van global fuera función: {var_global}")

# Es un error que no es definidio de variable de adentro de función
# print(f'Var local fuera función: {var_local}')

# No es posible acceder a variables locales fuera
# Del bloque donde se definierion
# print(f'Var locla fuera función: {var_local}')

print(" Alcance de Variables - Parte 2 ".center(60, "-"))
