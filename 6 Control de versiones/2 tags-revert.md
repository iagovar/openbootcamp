# Git Tags

Los TAGS son una forma de asignar info extra a los commits, normalmente para asignar versiones más "humanas" que un hash.ç


## Introducir etiquetas

- `git tag -a` -> Contienen más información, como autor, mail, fecha de creación de la etiqueta. Útil para proyectos open source o versiones mayores de nuestro proyecto.

	`git tag -a v1.0` -> Se le asignaría al commit actual.

	`git tag -a v1.0 0237fcc6396d75c8070a486f3e05b0a80e24353c` -> Se le asignaría al commit con el hash introducido.

- `git tag` -> Contienen poca información. Útil para versiones menores o uso interno.

Luego, ha ejecutar `git log` debería salir el nombre del TAG al lado de la info del commit.

## Enviar las etiquetas al remote

- `git push origin v1.0` Git hace el match de la etiqueta con el hash del commit local y lo envía.

## Ver el código que había en una etiqueta

- `git checkout v1.0` -> checkout nos sirve tanto para cambiar de rama como para ver una etiqueta

- Para volver, como cambiar de rama, ejecutamos un `git checkout master`. Recordar que *master* puede ser *main* también, depende del proveedor.

# Git revert

Sirve sirve para devolver el sistema de ficheros a un punto anterior, añadiendo un *commit* adicional al log.

- `git revert [hash-del-commit]` -> No es necesario introducir el hash entero, pueden ser, por ejemplo, los 5 primeros números, siempre y cuando esos 5 primeros sean únicos en el log, de lo contrario mostrará un conflicto.

	Al ejecutar un revert, se introduce un nuevo commit en el log, con su propio mensaje. El sistema de ficheros vuelve a un punto anterior pero no se manipula ningún commit anterior, ni borrandolo ni modificandolo.