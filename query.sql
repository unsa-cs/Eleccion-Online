INSERT INTO eleccion
    (fecha, hora_inicio, hora_fin, estado, descripcion)
VALUES
    ('2024-07-22', '08:00:00', '17:00:00', 'abierto', 'Elección General'),
    ('2024-07-23', '09:00:00', '18:00:00', 'cerrado', 'Elección Local');
insert into lista_candidato (nombre, id_eleccion) 
values ('Podemos', 1), ('arriba Peru', 1), ('be Like', 2);
INSERT INTO candidato (nombres, apellido_paterno, apellido_materno, id_lista_candidato) VALUES
('Juan', 'Perez', 'Lopez', 1),
('Maria', 'Gomez', 'Sanchez', 2),
('Luis', 'Martinez', 'Garcia', 1),
('Ana', 'Hernandez', 'Rodriguez', 2),
('Carlos', 'Diaz', 'Fernandez', 1);
