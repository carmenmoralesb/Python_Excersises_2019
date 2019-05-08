drop database agenda;
CREATE DATABASE agenda;
use agenda;

CREATE TABLE contactos (
	nombre varchar(30) PRIMARY KEY,
	numero varchar(30)
	) ENGINE = InnoDB;

CREATE TABLE contactofamiliar (
	nombre varchar(30),
	FOREIGN KEY (nombre) REFERENCES contactos(nombre) ON UPDATE CASCADE ON DELETE CASCADE,
	nombrefamiliar varchar(30) ,
	FOREIGN KEY (nombrefamiliar) REFERENCES contactos(nombre) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY (nombre,nombrefamiliar)
	) ENGINE = InnoDB;

INSERT INTO contactos values ('contacto1','689784852');
INSERT INTO contactos values ('contacto2','958471512');
INSERT INTO contactos values ('contacto3','956325800');
INSERT INTO contactos values ('contacto4','647125420');

INSERT INTO contactofamiliar values ('contacto1','contacto2');
INSERT INTO contactofamiliar values ('contacto1','contacto3');