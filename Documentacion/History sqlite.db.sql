--- 13-06-2023 18:20:09
--- sqlite.db
INSERT INTO Alumnos (id_alumno, nombre, apellido, nªlegajo, contraseña, id_cursos)
VALUES (0001,'abel','villegas',001,'abel2005',01);

--- 13-06-2023 18:20:28
--- sqlite.db
/***** ERROR ******
near "Alumnos": syntax error
 ----- 
SELECT * FROM Alumnos;Alumnos;
*****/

--- 13-06-2023 18:20:38
--- sqlite.db
SELECT * FROM Alumnos;

--- 13-06-2023 18:20:48
--- sqlite.db
SELECT * FROM Alumnos WHERE id_alumno = '0002';

--- 13-06-2023 18:21:04
--- sqlite.db
INSERT INTO Cursos (id_cursos,id_materias)
VALUES (01,02);

--- 13-06-2023 18:21:12
--- sqlite.db
SELECT * FROM Cursos;

--- 13-06-2023 18:21:22
--- sqlite.db
SELECT * FROM Cursos WHERE id_cursos = '02';

--- 13-06-2023 18:21:45
--- sqlite.db
INSERT INTO Libro (id_libro, nombre, autor, manual, literario, materias, id_materias,
id_profesor)
VALUES (1, 'Curso de Matemáticas', 'John Smith', 'Sí', 'No', 'Matemáticas', 02, 013);

--- 13-06-2023 18:21:58
--- sqlite.db
INSERT INTO Materias (id_materias, nombre, cursos)
VALUES (02, 'Curso de Matemáticas', 'septimo');

--- 13-06-2023 18:22:09
--- sqlite.db
INSERT INTO Nom_cursos (nom_cursos, nombre, id_profesores, id_cursos)
VALUES ('sexto', 'Curso de Matemáticas', 018, 01);

--- 13-06-2023 18:22:43
--- sqlite.db
INSERT INTO Profesores (id_profesores, nombre, apellidos, dni, materias, contraseña, id_materias)
VALUES (018, 'Juan', 'Gomez', 44740499, 'Matematicas', 'juan2003', 02);

