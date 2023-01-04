# Ramas - Branches

Se usan para tener múltiples versiones de desarollo y/o modificaciones sin modificar el master.

**nota**: Hay un directorio que contiene diagramas en SVG explicando los procesos.

## Ver, crear y cambiar a ramas

- `git branch` 										-> ver ramas.

- `git branch [nombreDeLaRama]` 					-> Crea la rama.

	- `git branch [nombreDeLaRama] [hashDelCommit]` -> Crear una rama desde un commit anterior.

- `git checkout [nombreDeLaRama]` 					-> Cambiar a una rama. Cambian también los ficheros del directorio de trabajo.

	- `git checkout -b [nombreDeLaRama]` 			-> Cambia a una rama, y la crea si no existe.

- `git status`										-> Muestra (también) en qué rama estamos.

- `git pull origin [nombreDeLaRama]`				-> Obtener una rama del repo remoto



También es posible crear una rama de otra rama. Simplemente haciendo chechout a la rama padre y haciendo el branch desde ahí.


# Unificación de cambios - merge y rebase

- `git merge NOMBRE-DE-LA-RAMA` -> Fusiona la rama indicada con la rama en la que nos hemos colocado con *checkout*.


## Tipos de merge

- Explicado en el blog: [Enlace](https://iagovar.com/git/git-merge-rebase)

## Rebase

- Explicado en el blog: [Enlace](https://iagovar.com/git/git-merge-rebase)

## Cuańdo usar merge y cuándo rebase

tl:dr > Rebase en local y merge en remoto

Aunque el [post del blog](https://iagovar.com/git/git-merge-rebase) contiene mucha información al respecto, resumidamente se puede decir que, salvo acuerdo previo con el resto del equipo (de haberlo), es preferible usar `git rebase` sólo para incorporar los cambios de *origin master* en la rama feature local.

Es decir, ejecutar un `git pull` desde *local master*, y luego un `git rebase master` desde la rama *local feature* sobre la que estemos trabajando.

Para incorporar los cambios en la rama *local master* y luego subirlos al remoto, es preferible usar un `git mere` por el simple hecho de que aunque el historial de confirmaciones pueda estar más sucio, y luego un `git bisect` se pueda complicar, es también más transparente y no se esconde nada.

## Más información

- Sobre Rebase: [Link](https://www.atlassian.com/es/git/tutorials/rewriting-history/git-rebase)
- Merge VS Rebase:
	- [Matt Mickard](https://matt-rickard.com/squash-merge-or-rebase)
	- [Attlasian](https://www.atlassian.com/es/git/tutorials/merging-vs-rebasing)
	- [The modern coder](https://www.youtube.com/watch?v=f1wnYdLEpgI)
