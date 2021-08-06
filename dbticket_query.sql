-- SQLite
-- CREATE TABLE tickets(
--     Noticket INTEGER PRIMARY KEY AUTOINCREMENT,
--     Estado text NOT NULL,
--     Prioridad text NOT NULL,
--     Descripcion text NOT NULL,
--     AbiertoDia text NOT NULL,
--     Informado text NOT NULL,
--     CerradoDia int,
--     Resuelto text
-- );

-- CREATE TABLE Users(
--     Cedula text PRIMARY KEY,
--     Nombre text NOT NULL,
--     Usuario text,
--     Equipo text,
--     Ext text
-- );

-- CREATE TABLE resueltos{
--     Noticket INTEGER,
--     DescripResuelto text NOT NULL,
--     FOREIGN KEY(Noticket) REFERENCES tickets(Noticket)
-- }

SELECT * FROM resueltos
INSERT INTO tickets (Estado, Prioridad, Descripcion, AbiertoDia, Informado, CerradoDia) VALUES('Abierto', 'Baja', 'Description Test', '05/08/2021 07:57:24', 'DAVID DE LA HOZ', 'dasdas')
.schema tickets
UPDATE tickets
SET Estado = "Cerrado"
WHERE Noticket = 16