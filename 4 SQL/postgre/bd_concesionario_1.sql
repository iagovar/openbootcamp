-- tabla manufacturer MANUFACTURER
create table manufacturer(
	id SERIAL,
	name VARCHAR(50) not null,
	num_employees int,
	-- otra forma de definir si una columna es primare key es con un constraint
	constraint pk_manufacturer primary key(id)
);

insert into manufacturer(name, num_employees)
values ('Ford', '29000');

insert into manufacturer(name, num_employees)
values ('Toyota', '45000');

select * from manufacturer;

-- tabla MODEL

create table model(
	id serial,
	name varchar(50) not null,
	id_manufacturer INT,
	/*
	Claves primaria y foranea
	
	El formato es:
	
	constraint nombre_de_limitacion tipo_de_clave(columna_designada_como_clave)
	
	En la foreign key hay que indicarle a quÃ© tabla y columna referencia (ver abajo)
	
	*/
	constraint pk_model primary key(id),
	constraint fk_model_manufacturer foreign key(id_manufacturer) references manufacturer(id)
);

-- Insertando datos en model

select * from model;

insert into model (name, id_manufacturer)
values ('Mondeo', 1);

insert into model (name, id_manufacturer)
values ('Fiesta', 1);

insert into model (name, id_manufacturer)
values ('Prius', 2);

-- tabla version

create table version(
	id serial,
	name varchar(50) not null,
	engine varchar(50),
	price numeric,
	-- numeric(cuantos_numeros_enteros+decimales, cuantos_decimales)
	cc numeric(2,1),
	id_model int,
	constraint pk_version primary key(id),
	/*
	Las sentencias ON UPDATE & ON DELETE establecen rutinas para esas acciones.
	
	TÃ­picamente se hace:
	CASCADE: Si se borra la referencia de la FK, en este caso un modelo, se borrarÃ­an todos los registros de esta tabla
			que contenga esa foreign key.
	
	SET NULL: En caso de borrar un modelo en la tabla de modelos, en esta tabla simplemente la FK parsarÃ¡ a NULL.	
	*/
	constraint fk_version foreign key(id_model) references model(id) on update set null on delete set null
);

select * from version;
select * from model;

INSERT INTO version (name, engine, price, cc, id_model) VALUES ('Basic', 'Diesel 4C', 30000, 1.9, 1);
INSERT INTO version (name, engine, price, cc, id_model) VALUES ('Medium', 'Diesel 5C', 50000, 2.2, 1);
INSERT INTO version (name, engine, price, cc, id_model) VALUES ('Advance', 'Diesel 5C V', 80000, 3.2, 1);

INSERT INTO version (name, engine, price, cc, id_model) VALUES ('Sport', 'Gasoline 4C', 50000, 2.1, 2);
INSERT INTO version (name, engine, price, cc, id_model) VALUES ('Sport Advance', 'Gasoline 8C', 90000, 3.2, 2);

-- Extra
/*
Los extras son una relación many-to-many, ya que una versión puede tener varios extras, y los extras pueden estar
en varias versiones simultáneamente.

Esto significa que no podremos usar claves foráneas o foreign keys.

En su lugar crearemos una tabla nueva para relacionar la tabla extra con la tabla version.
 */

create table extra(
	id serial,
	name varchar(50) not null,
	description varchar(300),
	constraint pk_extra primary key(id)
);

/* Creamos una tabla para la relación many-to-many
 * 1. La primary key son dos columnas, pues la misma fila no se puede repetir dos veces.
 * 2. Las FKs son necesarias igualmente, simplemente les cambiamos el nombre porque no pueden tener el mismo.
 */
create table extra_version(
	id_version int,
	id_extra int,
	price numeric not null check (price >= 0),
	constraint pk_extra_version primary key(id_version, id_extra),
	constraint fk_version_extra foreign key(id_version) references version(id) on update cascade on delete cascade,
	constraint fk_extra_version foreign key(id_extra) references extra(id) on update cascade on delete cascade
);


-- Creamos nuevos extras

select * from extra;

insert into extra(name, description)
values('Techo Solar', 'Techo solar de puta madre');

insert into extra(name, description)
values('Climatizador', 'Ke haga freskito premoh');

insert into extra(name, description)
values('Wifi', 'Pal nene');

insert into extra(name, description)
values('Frigorífico', 'Pa las birras');

-- creamos nuevos extra-version
/*
 * Al meter values sobre todas las columnas, no hace falta especificar sobre qué columnas vamos
 * a ejecutar los cambios después del insert into nombre_tabla
 */
	-- Ford Mondeo Basic Techo Solar
insert into extra_version
values(1, 1, 3000);
	-- Ford Mondeo Basic Climatizador
insert into extra_version
values(1, 2, 1000);
	-- Ford Mondeo Basic Wifi
insert into extra_version
values(1, 3, 500);


	-- Ford Mondeo Advance Techo Solar
insert into extra_version
values(3, 1, 3300);
	-- Ford Mondeo Advance Climatizador
insert into extra_version
values(3, 2, 1200);
	-- Ford Mondeo Advance Wifi
insert into extra_version
values(3, 3, 500);



--- Creamos empleados

create table employee(
	id SERIAL,
	name varchar(30),
	nif varchar(9) not null unique,
	phone varchar(9),
	constraint pk_employee primary key(id)
);

insert into employee(name, nif, phone) values('bob', '12345678A', '600123456');
insert into employee(name, nif, phone) values('Mike', '12345678B', '601123456');


-- Creamos clientes

create table customer(
	id SERIAL,
	name varchar(30),
	email varchar(9) not null unique,
	constraint pk_customer primary key(id)
	
);

insert into customer(name, email) values('customer1', 'mail1@mail.com');
insert into customer(name, email) values('customer2', 'mail2@mail.com');

/*
 * Esta inserción da error porque hemos puesto la tabla email con varchar(9), que es demasiado
 * corto, vamos a modificarlo.
 * 
 * https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-change-column-type/
 */

alter table customer
	alter column email type varchar(50);



-- creamos vehículos

create table vehicle(
	id serial,
	license_num varchar(7), -- la metrícula del vehículo
	creation_date date,		-- la fecha de fabricación
	price_gross numeric,
	price_net numeric,
	type varchar(30),		-- tipo de vehículo
	
	id_manufacturer int,
	id_model int,
	id_version int,
	id_extra int,
	
	constraint pk_vehicle primary key(id),
	constraint fk_vehicle_manufacturer foreign key(id_manufacturer) references manufacturer(id),
	constraint fk_vehicle_model foreign key(id_model) references model(id),
	constraint fk_vehicle_extra_version foreign key(id_version, id_extra) references extra_version(id_version, id_extra)
	
);

	-- Ford mondeo basic con techo solar
insert into vehicle (license_num, price_gross, id_manufacturer, id_model, id_version, id_extra)
values('1234LLL', 40000, 1, 1, 1, 1);

	-- Ford mondeo advance con techo solar
insert into vehicle (license_num, price_gross, id_manufacturer, id_model, id_version, id_extra)
values('1234ZZZ', 40000, 1, 1, 3, 1);

-- creamos un registro de ventas


create table sale(
	id serial,
	sale_date date, -- Es yyyy-mm-dd
	channel varchar(300),
	
	id_vehicle int,
	id_employee int,
	id_customer int,
	
	constraint pk_sale primary key(id),
	constraint fk_sale_vehicle foreign key (id_vehicle) references vehicle(id),
	constraint fk_sale_employee foreign key (id_employee) references employee(id),
	constraint fk_sale_customer foreign key (id_customer) references customer(id)	
);

	-- insertamos ventas

insert into sale(sale_date, channel, id_vehicle, id_employee, id_customer)
values('2022-01-01', 'Phone', 1, 1, 1);

