

select mybb_users.username from mybb_users;

select mybb_userfields.fid3 from mybb_userfields;


-- Listar usuarios con su sexo
select
mybb_users.username,
mybb_userfields.fid3 as 'Sexo'
from mybb_users
inner join mybb_userfields
on mybb_users.uid = mybb_userfields.ufid;

-- Cuántos usuarios de cada sexo hay

	select DISTINCT fid3 from mybb_userfields;
	
	/*
	fid3  |
	------+
	Mujer |
	      |
	Hombre|
	 */
	
	select count(*) from mybb_userfields;
	
	/*
	count(*)|
	--------+
	     456|
	 */
	
	select
	mybb_userfields.fid3 as 'Sexo',
	count(mybb_userfields.fid3) as '#'
	from mybb_userfields
	group by mybb_userfields.fid3;

-- Listar usuarios con su sexo ordenados por fecha de registro

select
mybb_users.username as Nombre,
FROM_UNIXTIME(mybb_users.regdate, '%y-%m-%d') as Registro,
mybb_userfields.fid3 as Sexo
from mybb_users
inner join mybb_userfields
on mybb_users.uid = mybb_userfields.ufid
order by Registro;

-- Historico de registros agrupados por día,
-- contando hombres por un lado, mujeres por otro


	-- Consulta que NO incorpora todos los días
	select
	FROM_UNIXTIME(mybb_users.regdate, '%y-%m-%d') as Registro,
	count(if(mybb_userfields.fid3 = 'Hombre', 1, null)) as Hombre,
	count(if(mybb_userfields.fid3 = 'Mujer', 1, null)) as Mujer,
	count(if(mybb_userfields.fid3 = '', 1, null)) as Desconocido
	from mybb_users
	inner join mybb_userfields
	on mybb_users.uid = mybb_userfields.ufid
	group by Registro
	order by mybb_users.regdate;

	-- Consulta que SI incorpora todos los días

	/*
	 * MySQL no tiene generate_series() como postgre, asi que hay que crear
	 * una tabla que contenga un listado de fechas para luego hacer un JOIN
	 */

	
	-- ! pendiente


-- Distribución de mensajes privados enviados y recibidos por sexo

	-- https://docs.mybb.com/1.6/Database-Tables-mybb-privatemessages/
	-- Folder 1 Recibidos 2 Enviados

create or replace view ranking_mensajes_privados as
select
mybb_users.username as Usuario,
mybb_users.uid,
mybb_userfields.fid3 as Sexo,
count(if(folder = 1, 1, null)) as Recibidos,
count(if(folder = 2, 1, null)) as Enviados
from mybb_privatemessages
inner join mybb_users 		on mybb_privatemessages.uid = mybb_users.uid
inner join mybb_userfields 	on mybb_privatemessages.uid = mybb_userfields.ufid
-- Quitamos al administrador de la ecuación
where 
mybb_privatemessages.fromid <> 1
and mybb_privatemessages.toid <> 1
group by Usuario
order by Recibidos desc;

	-- Creamos índices para acelerar la consulta (fundamentalmente por WHERE)
	-- ya hay un índice para toid

	create or replace index fromid
	on mybb_privatemessages(fromid);

-- Pivot table de quién ha enviado a quién
-- MariaDB no soporta pivoting nativo: https://mariadb.com/kb/en/pivoting-in-mariadb/


