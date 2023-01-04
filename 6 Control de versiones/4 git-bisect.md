# Git bisect

Un código que funcionaba de repente deja de hacerlo. Se ha introducido un error, pero ¿dónde y cuándo exactamente? Especialmente en equipos grandes o después de que se haya integrado una serie de nuevos commits, encontrar ese error puede ser todo un reto.

Está bien explicado [aquí](https://www.git-tower.com/learn/git/faq/git-bisect/).

## Cómo operar

Git Bisect requiere sólo dos piezas de información antes de que pueda comenzar la búsqueda de errores:

1. Un commit (hash) en la que las cosas funcionaban bien.
2. Un commit (hash) en la que esté presente el fallo.

  - `git bisect start` 			-> Comenzamos el proceso.
  - `git bisect bad [hash]` 	-> Indicamos el commit donde dejó de funcionar.
  - `git bisect good [hash]` 	-> Indicamos último commit que funcionaba. Esto puede ser complicado, quizá tengas alguna certeza, a través de una fecha u otro dato, quizá sea sólo intuición.


Una vez hecho esto, Git nos presentará en el directorio de trabajo el estado de un commit (hash), y será nuestro trabajo correr la aplicación con esos ficheros y ver si el bug está presente o no.

  - Le indicaremos a Git con `git bisect good`, `git bisect bad` si el commit que nos ha presentado funciona correctamente o no.

	Git nos presentará otro commit distinto, y repetirá el proceso (seleccionando los commits como si un *binary search* se tratara), hasta aislar el commit culpable.

  - `git bisect reset` finalizará el proceso, y moverá el HEAD al último commit bueno, así como nuestro sistema de archivos.
