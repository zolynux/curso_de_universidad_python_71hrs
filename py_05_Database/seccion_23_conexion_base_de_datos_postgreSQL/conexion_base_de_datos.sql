-- Mostrar detalles de persona en base de datos
-- SELECT * FROM persona in (1,2)

-- Crear un dato de persona 
-- INSERT INTO persona(nombre, apellido, email) VALUES('Susana', 'Lara', 'slara@mail.com')

-- Se creó un dato y mostrar un dato de donde en ID
-- SELECT * FROM persona WHERE id_persona = 3

-- Modificar un dato de persona con nombre, apellido y/o email
-- Ten mucho cuidado que actualizar todos los valores de datos de una persona
-- Es lo muy importante que debes usar 'WHERE' y luego escribo los datos de una persona existenta
-- con nombre_columna = 'valor'
-- UPDATE persona SET nombre = 'Ivone', email = 'iseparaz@mail.com' WHERE id_persona = 3

-- Eliminar tener mucho cuidado que debe filtra con WHERE
-- para que no borra todos los datos de usuarios.
-- DELETE FROM persona WHERE id_persona in (3,2,1)
-- DELETE FROM persona WHERE id_persona = 3
SELECT * FROM persona 

-- SELECT = Seleccionar REgistros
-- INSERT = Agregar Registros
-- UPDATE = Actualizar Registros
-- DELETE = Eliminar Registros