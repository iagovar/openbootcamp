# Ramas - branches

Se usan para tener múltiples versiones de desarollo y/o modificaciones sin modificar el master.

## Ver, crear y cambiar a ramas

- `git branch` 										-> ver ramas.

- `git branch [nombreDeLaRama]` 					-> Crea la rama.

	- `git branch [nombreDeLaRama] [hashDelCommit]` -> Crear una rama desde un commit anterior.

- `git checkout [nombreDeLaRama]` 					-> Cambiar a una rama. Cambian también los ficheros del directorio de trabajo.

	- `git checkout -b [nombreDeLaRama]` 			-> Cambia a una rama, y la crea si no existe.

- `git status`										-> Muestra (también) en qué rama estamos.

- `git pull origin [nombreDeLaRama]`				-> Obtener una rama del repo remoto

---
También es posible crear una rama de otra rama. Simplemente haciendo chechout a la rama padre y haciendo el branch desde ahí.
---

# Unificación de cambios - merge y rebase

- `git merge NOMBRE-DE-LA-RAMA` -> Fusiona la rama indicada con la rama en la que nos hemos colocado con *checkout*.


## Tipos de merge

- Explicado en el blog: [Enlace](https://iagovar.com/git/git-merge-rebase)

## rebase

- Explicado en el blog: [Enlace](https://iagovar.com/git/git-merge-rebase)

## Cuańdo usar merge y cuándo rebase

- Merge para origin y rebase en local?

## Más información

- Sobre Rebase: [Link](https://www.atlassian.com/es/git/tutorials/rewriting-history/git-rebase)
- Merge VS Rebase:
	- [Matt Mickard](https://matt-rickard.com/squash-merge-or-rebase)
	- [Attlasian](https://www.atlassian.com/es/git/tutorials/merging-vs-rebasing)
	- [The modern coder](https://www.youtube.com/watch?v=f1wnYdLEpgI)
