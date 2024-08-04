# Profundizando en el método split para cadenas

# split - separar o dividir
# help(str.split)

cursos = "Java Python JavaScript Angular Spring Excel"
lista_cursos = cursos.split()
print(f"lista cursos: {lista_cursos}")
print(type(lista_cursos))

cursos_separados_coma = "Java,Python,JavaScript,Angular,Spring,Excel"
lista_cursos = cursos_separados_coma.split()
print(f"lista cursos: {lista_cursos}")
print(len(lista_cursos))

print("-" * 60)

cursos_separados_coma = "Java,Python,JavaScript,Angular,Spring,Excel"
lista_cursos = cursos_separados_coma.split(",")
print(f"lista cursos: {lista_cursos}")
print(len(lista_cursos))

print("-" * 60)

cursos_separados_coma = "Java, Python, JavaScript, Angular, Spring, Excel"
lista_cursos = cursos_separados_coma.split(", ")
print(f"lista cursos: {lista_cursos}")
print(len(lista_cursos))

print("-" * 60)

cursos_separados_coma = "Java, Python, JavaScript, Angular, Spring, Excel"
lista_cursos = cursos_separados_coma.split(", ", 3)
print(f"lista cursos: {lista_cursos}")
print(len(lista_cursos))
