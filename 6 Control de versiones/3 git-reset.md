# Git Reset

Sirve para "volver hacia atrás" en los commits.

## Conceptos previos necesarios

En GIT el HEAD o cabecera siempre es el último commit. Cada vez que se comitea de nuevo, GIT asigna HEAD al último commit.

## Cómo operar git reset

- `git reset --soft cd1fd34`: Moverá el HEAD a un commit anterior, en este caso al cd1fd34, pero no modifica los ficheros del directorio de trabajo.

	Si haces un `git log` posterior al reset, verás que el último commit que aparece es el que has referenciado en el reset.

- `git reset --hard cd1fd34:` Moverá el HEAD al commit cd1fd34 pero **SÍ MODIFICA** los ficheros del directorio de trabajo.


## Git diff para comparar

 - Es posible usar `git diff [HASH]` para comparar las diferencias entre los ficheros del directorio de trabajo y lo guardado en el .git del repo local.