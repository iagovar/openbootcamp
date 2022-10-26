/*
 * Ver el tama�o de una tabla
 * 
 * https://www.postgresqltutorial.com/postgresql-administration/postgresql-database-indexes-table-size/
 * 
 */

select pg_relation_size('categories');

-- Si queremos hacerlo m�s legible podemos usar pg_size_pretty() que transforma las unidades en kb, mb, etc

select pg_size_pretty(
	pg_relation_size('categories')
	); -- Resulta en ~8k que no coincide con lo mostrado por DBeaver
	
-- pg_relation_size() s�lo devuelve el tama�o de la tabla, no de otros objetos como �ndices, para evitar esto
-- podemos usar pg_total_relation_size()

select pg_size_pretty(
	pg_total_relation_size('categories')
	); -- Resulta en ~32k que s� coincide con lo mostrado por DBeaver
	

/*
 * Ver el tama�o de una BD
 * 
 * El proceso es similar para las tablas
 */
	
select pg_size_pretty(pg_database_size('northwind'))

-- Y de todas las BD
-- Ver system catalogs: https://www.postgresql.org/docs/14/catalogs.html

SELECT
    pg_database.datname,
    pg_size_pretty(pg_database_size(pg_database.datname)) AS size
    FROM pg_database
;

   
/*
 *  M�s joins y groupby's
 * 
 * No reproducimos el v�deo porque es m�s de lo que hicimos con pagila.
*/

   
   
   
   
   
   
/*
 *  VISTAS
 * 
 * Las vistas son consultas que se pueden guardar en la DB con un alias,
 * de forma que no hay que volver a escribirlas constantemente.
 * 
 * Los datos generados en las vistas no est�n guardados, sino que la consulta
 * se ejecuta cada vez que es llamada.
 * 
 * LAS VISTAS VATERIALZIADAS s� guardan esos datos generados en la consulta,
 * pero no son soportadas por muchas dbms (como MySQL, SQLite o DuckDB)
 * 
 */


-- �Qu� empleado ha vendido m�s (N� Ventas, ��� y � por venta) en Enero del 97? Vista normal

create view ventas_empleados as
select
concat(employees.first_name, ' ', employees.last_name) as "Empleado",
count(orders.order_id) as "N� Ventas",
-- Esta columna calcula el precio final de todas las ventas, y luego suma todos sus valores
sum(round(cast(order_details.unit_price * order_details.quantity * (1 - order_details.discount) as numeric), 2)) as "Monto �",
-- Esta tabla divide el monto total entre el n�mero de ventas
round(cast(sum(order_details.unit_price * order_details.quantity * (1 - order_details.discount)) / count(orders.order_id) as numeric), 2) as "�/Venta"
from order_details
inner join orders on order_details.order_id = orders.order_id
inner join employees on orders.employee_id = employees.employee_id
where orders.order_date between '1997-01-01' and '1997-01-31'
group by "Empleado"
order by "�/Venta" desc

-- En qu� estados se han vendido m�s productos Enero del 97?
-- N�mero de ventas, monto de ventas y �/Venta

/*
 * Las vistas materializadas tienen sentido para consultas muy intensivas 
 */

create materialized view ventas_pais as
	select
		-- Tabla de agrupaci�n
		orders.ship_country,
		-- �Cu�ntas ventas se ejecutaron?
		count(orders.order_id) as "N� Ventas",
		-- �Cu�l es el monto total de ventas por pa�s?
		round(cast(sum(order_details.unit_price * order_details.quantity * (1 - order_details.discount)) as numeric), 2) as "Monto Total",
		-- �Cu�l es el promedio de precio de todas las ventas?
		round(cast(avg(order_details.unit_price * order_details.quantity * (1 - order_details.discount)) as numeric), 2) as "Promedio de todas las ventas"
	from orders
	inner join order_details on orders.order_id = order_details.order_id
	group by orders.ship_country
	order by "Promedio de todas las ventas" desc
-- Indicamos que no meta datos por ahora (se har� con un refresh etc)
with no data;


-- Ahora actualizamos la vista materialziada

/*
 * CONCURRENTLY previene el lock de la vista.
 * 
 * Como no ten�a datos al crearla, al hacer el refresh se poblar� por primera vez.
 * 
 * https://www.postgresqltutorial.com/postgresql-views/postgresql-materialized-views/
 */


REFRESH MATERIALIZED VIEW 
-- CONCURRENTLY  no se puede usar si la vista no tiene datos, como es el caso cuando
-- la hemos creado.
ventas_pais;


-- Ver las vistas materializadas que existen en la DB
select * from pg_matviews;


-- Otro ejemplo de vista materializada generando series

create table prueba1(
	id int,
	name varchar
)


-- generate_series para generar datos de prueba

INSERT into prueba1(id)
SELECT * FROM generate_series(1, 500000)

create materialized view vista_prueba1 as
select * from prueba1
with data

select * from generate_series(
	'2022-01-01 00:00'::timestamp,
	'2022-12-25 00:00',
	'6 hours'
)


/*
 EXPLAIN ANALYZE 
 
 �til:
	- Buscar escaneos sequenciales y crear �ndices que puedan reducir el tiempo.

	  Un �ndice sobre columnas escaneadas sequencialmente puede acelerar mucho los
	  tiempos de consultas con WHERE o que no devuelva grandes grupos de datos.
	
	- En trabajos OLAP tendr� sentido optimizarvistas, ya que no hay a penas trabajo
	  transaccionar. En OLTP habr� que averiguar cu�les son las consultas m�s comunes
	  a la BD o cu�les tienen mayor impacto.
	  
	  https://dataschool.com/sql-optimization/optimization-using-explain/
	  
	  https://explain.depesz.com/
 */

-- Una vista No materialziada
explain analyze
select * from ventas_empleados;

-- Vista materializada
explain analyze
select * from ventas_pais;

/*

Sobre ventas_empleados obtenemos:

Planning Time: 0.491 ms  
Execution Time: 1.012 ms 

Lo cierto es que las tablas son muy peque�as y no vamos a notar la diferencia con ninguna t�nica, intentemos con la tabla
prueba1, que tiene muchos elementos.

 */

explain analyze
select * from prueba1 where prueba1.id > 9999 and prueba1.id < 11000;

/*
Planning Time: 0.091 ms       
Execution Time: 73.418 ms <- Podemos reducir esto? 
 */

-- Creamos un �ndice sobre prueba1.id

create index index_prueba1_id
on prueba1(id);

-- Probamos de nuevo, a ver qu� nos da
explain analyze
select * from prueba1 where prueba1.id > 9999 and prueba1.id < 11000;


/*
Planning Time: 1.683 ms     
Execution Time: 0.326 ms <-- Hemos bajado de 73 a 0 ms
 */




/*
 *		Particionamiento de tablas
 * 
 *		Las particiones de tablas permiten la fragmentaci�n autom�tica de los datos en varias tablas,
 *		trat�ndolas al mismo tiempo como una �nica colecci�n a trav�s de una tabla principal.
 *   
 *		
 *		- Explicaci�n muy completa: https://www.youtube.com/watch?v=oJj-pltxBUM
 *		- Docs oficiales: https://www.postgresql.org/docs/current/ddl-partitioning.html
 *
 *		Tipos de pariciones:
 *		- Por Rango
 *		- Por Lista
 *		- Por Hash
 */


-- creamos la tabla base

create table users (
	id bigserial, -- Si vamos a almacenar muchos datos tiene sentido usar bigserial
	birth_date date not null,
	first_name varchar(20) not null,
	primary key(id, birth_date)
)

partition by range (birth_date);

-- creamos las particiones

create table users_2020 partition of users
-- Primera fecha inclu�da, segunda exclu�da
for values from ('2020-01-01') to ('2021-01-01');

create table users_2021 partition of users
-- Primera fecha inclu�da, segunda exclu�da
for values from ('2021-01-01') to ('2022-01-01');

create table users_2022 partition of users
-- Primera fecha inclu�da, segunda exclu�da
for values from ('2022-01-01') to ('2023-01-01');


-- Insetamos datos
-- Podemos insertarlos sobre la tabla maestra y la BD ya colocar� la fila donde corresponde.

insert into users(birth_date, first_name) values
('2020-02-11','Usuario 1'),
('2020-05-01','Usuario 2'),
('2021-01-02','Usuario 3'),
('2021-12-01','Usuario 4'),
('2022-10-28','Usuario 5'),
('2022-11-22','Usuario 6')


-- Miramos a ver si el insert hizo lo que queremos
select * from users;
select * from users_2021;

-- Probamos con una consulta a ver qu� escanea

explain analyze select * from users where users.birth_date > '2021-01-01'


/*
QUERY PLAN                                                                                                          |
--------------------------------------------------------------------------------------------------------------------+
Append  (cost=0.00..43.52 rows=554 width=70) (actual time=0.020..0.028 rows=4 loops=1)                              |
  ->  Seq Scan on users_2021 users_1  (cost=0.00..20.38 rows=277 width=70) (actual time=0.015..0.016 rows=2 loops=1)|
        Filter: (birth_date > '2021-01-01'::date)                                                                   |
  ->  Seq Scan on users_2022 users_2  (cost=0.00..20.38 rows=277 width=70) (actual time=0.006..0.006 rows=2 loops=1)|
        Filter: (birth_date > '2021-01-01'::date)                                                                   |
Planning Time: 0.251 ms                                                                                             |
Execution Time: 0.050 ms

	>>> Podemos ver en el query plan que ya obvia la tabla de 2020
                                                                                                                                                                                                                                                                                    |
 */


--- CARGAR EXTENSIONES

create extension pgcrypto;
	-- Ver: https://www.postgresql.org/docs/current/pgcrypto.html

