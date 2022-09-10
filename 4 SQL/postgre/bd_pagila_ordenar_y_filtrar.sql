
-- Cómo obtener una lista de valores únicos/no duplicados
select distinct district from address;

select distinct first_name from customer;

-- Operadores lógicos AND, OR, NOT

 -- NOT y != son equivalentes, pero se colocan en sitios distintos
select * from address where district != 'California';
select * from address where not district = 'California';

-- OR/AND

select * from address where district = 'Abu Dhabi' or district = 'California';

select * from address where
not district = '' 				-- Evitamos vacíos
-- and not district = null 		-- Evitamos valores null NO FUNCIONA
and not district is null
and not district = 'California'	-- Excluímos a los californanios
order by district;


/*
 * GROUP BY 
 * 
 * https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-group-by/
 * 
 * Siempre nos va a pedir alguna función de agrupación como count()
 */

select district, count(district) as contados from address
group by district
order by contados desc;

-- Aplicar condiciones a grupos no se puede hacer con WHERE, sino con HAVING
-- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-having/

-- explain analyze -- Explica la consulta y mide su tiempo de ejecución
select district, count(district) as contados from address
group by district
having count(district) > 7 -- PARECE que no se ejecuta dos veces el count
order by contados desc;

-- Obtener cuantas pelis ha hecho cada actor

select * from film_actor
select * from actor
select * from film

select
concat(actor.first_name, ' ', actor.last_name) as Nombre
from film_actor
inner join actor on film_actor.actor_id = actor.actor_id
group by film_actor.actor_id


/*
 * JOINs
 * 
 * https://www.w3schools.com/sql/sql_join.asp
 * 
 * Inner join -> Se muestran los resultados de ambas tablas, pero sólo los que coinciden.
 * Left outer join -> Todos los registros de la tabla izquierda y los que coincidan de la derecha.
 * Right outer join -> Todos los registros de la tabla derecha, y los que coincidan de izquierda.
 * Full outer join -> ¿? Aparentemente todos los registros? 
 * 
 * Como hay varias tablas, si hay columnas que se llamen igual en ambas habrá errores, pero se puede
 * especificar qué queremos obtener mediante nombreTabla.nombreColumna, evitando así el conflicto en
 * el namespace.
 * 
*/


-- Probando una consulta a 2 tablas: customer y address
select
first_name,
last_name,
customer.address_id,	-- Las dos tablas tienen una columna que se llama igua, especificamos.
address					-- De la col derecha, pero sólo una tabla tiene una columna con este nombre
from customer			-- tabla 1 (izquierda)
inner join address		-- tabla 2 (derecha)
on customer.address_id = address.address_id;

-- Probando una consulta a cuatro tablas: customer, address, city y country

select
customer.email,
address.address,
city.city,
country.country 
from customer
inner join address on customer.customer_id  = address.address_id
inner join city on address.city_id = city.city_id
inner join country on city.city_id = country.country_id;

/*
 * Función CONCAT()
 */

select concat(first_name, ' ', last_name) as full_name from actor;

/*
 * Operador LIKE
 * 
 *  ILIKE => LIKE pero case insensitive
 */

select title, description from film where description ilike '%Monastery'
order by title asc;


/*
 * Operador IN
 * 
 * Sirve para indicarle al WHERE que busque en una lista, evitando así
 * tener que concatenar equivalencias con el operador OR
 * 
 * Se suele usar para pasar checboxes de un frontend en listas a SQL
 *
 */


select * from country where country in(
'Spain',
'Germany',
'France'
);

