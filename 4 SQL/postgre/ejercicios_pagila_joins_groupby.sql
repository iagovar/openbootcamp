
-- C�mo obtener una lista de valores �nicos/no duplicados
select distinct district from address;

select distinct first_name from customer;

-- Operadores l�gicos AND, OR, NOT

 -- NOT y != son equivalentes, pero se colocan en sitios distintos
select * from address where district != 'California';
select * from address where not district = 'California';

-- OR/AND

select * from address where district = 'Abu Dhabi' or district = 'California';

select * from address where
not district = '' 				-- Evitamos vac�os
-- and not district = null 		-- Evitamos valores null NO FUNCIONA
and not district is null
and not district = 'California'	-- Exclu�mos a los californanios
order by district;


/*
 * GROUP BY 
 * 
 * https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-group-by/
 * 
 * Siempre nos va a pedir alguna funci�n de agrupaci�n como count()
 */

select district, count(district) as contados from address
group by district
order by contados desc;

-- Aplicar condiciones a grupos no se puede hacer con WHERE, sino con HAVING
-- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-having/

-- explain analyze -- Explica la consulta y mide su tiempo de ejecuci�n
select district, count(district) as contados from address
group by district
having count(district) > 7 -- PARECE que no se ejecuta dos veces el count
order by contados desc;

-- Join + Group by: �Cu�ntas Pelis hizo cada actor?

select * from film_actor
select * from actor
select * from film
select * from inventory

select
concat(actor.first_name, ' ', actor.last_name) 	as "Nombre",
count(film_actor.film_id) 						as "Pelis"
from film_actor
inner join actor on film_actor.actor_id = actor.actor_id
group by "Nombre"
having count(film_actor.film_id) > 30
order by "Pelis" desc;

-- �Y cu�ntas copias de sus pel�culas ha vendido cada actor?




/*
 * JOINs
 * 
 * https://www.w3schools.com/sql/sql_join.asp
 * 
 * Inner join -> Se muestran los resultados de ambas tablas, pero s�lo los que coinciden.
 * Left outer join -> Todos los registros de la tabla izquierda y los que coincidan de la derecha.
 * Right outer join -> Todos los registros de la tabla derecha, y los que coincidan de izquierda.
 * Full outer join -> �? Aparentemente todos los registros? 
 * 
 * Como hay varias tablas, si hay columnas que se llamen igual en ambas habr� errores, pero se puede
 * especificar qu� queremos obtener mediante nombreTabla.nombreColumna, evitando as� el conflicto en
 * el namespace.
 * 
*/


-- Probando una consulta a 2 tablas: customer y address
select
first_name,
last_name,
customer.address_id,	-- Las dos tablas tienen una columna que se llama igua, especificamos.
address					-- De la col derecha, pero s�lo una tabla tiene una columna con este nombre
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
 * Funci�n CONCAT()
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
 * Sirve para indicarle al WHERE que busque en una lista, evitando as�
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


/*
 * Sub-queries (select dentro de otro select)
 */

select * from film;

-- Necesitamos cambiar el idioma a algunas columnas, porque solo hay una

update film set language_id = 2 where film_id > 100 and film_id <200;
update film set language_id = 3 where film_id > 200 and film_id <300;
update film set language_id = 4 where film_id > 400 and film_id <400;

-- Ejercicio: Buscar las pel�culas en Ingl�s e Italiano

select
film.title,
film.language_id
from film
-- Ejecutamos un where con un select que nos devolver� el ID del lenguaje que queremos
where language_id = (select language.language_id from language where language.name = 'Italian')

-- Si queremos varios lenguajes, el segundo select devolver� una lista, asi que hay que usar IN

select
film.title,
film.language_id
from film
where language_id IN (	select
						language.language_id
						from language
						where language.name = 'Italian' or language.name = 'English'
					 );

-- Ejercicio: �Qu� pel�culas son las m�s alquiladas?
	
select * from film;
select * from rental;
select * from inventory;

/*
 * La tabla rental nos registra los alquileres, la tabla inventory relaciona
 * el ID del inventario con el ID de la pel�cula, y la tabla fil tiene el nombre
 * de las pelis, por eso hacemos dos inner joins.
 * 
 * Luego simplemente contamos el n�mero de alquileres y asignamos esa funci�n
 * a "Pel�cula" con group by.
 */

select
film.title as "Pel�cula",
count(rental.rental_id) as "N� de Alquileres"
from rental
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on inventory.film_id = film.film_id
group by "Pel�cula"
order by "N� de Alquileres" desc



