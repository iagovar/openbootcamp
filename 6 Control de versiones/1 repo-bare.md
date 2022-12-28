## Crear un repo de cero

- Crear repo en directorio actual: `git init .`.

- Cofiguramos el repo:

	- System wide (A nivel de SO)
	- Global (Todos los repos de mi usuario)
	- Local (Este repo)

	Listamos la config local con `git config --list --local`.

	Cambiamos user y mail con:
		- `git config --local user.name "miUsuario"`
		- `git config --local user.email "micorreo@mimail.com`

	**Nota**: Cambiar el user o mail del repo local tiene efectos en el push. En el historial del repo --bare el commit cambiará, y supongo que se podrá denegar commits de user/mails desconocidos con alguna config. En Gitea simplemente aparece otro usuario y mail.

- Añadimos los archivos al staging area: `git add .`

## Repositorio BARE

Un repotorio creado con `git init --bare nombredelrepo` es similar a un repo *remote* pero que naturalmente es local. Se usará para almacenar información pero no será el repositorio de trabajo.

Contiene un histórico de confirmaciones (commits) pero no es posible trabajar con él directamente. Toda la información del repo se contiene en el directorio raíz, en lugar del directorio *.git* que se puede encontrar en los repos de trabajo.

### ¿Para qué usar un repo bare?

Puede ser útil en una carpeta compartida como repo al que hacer el *push*. De esta forma se tiene un server git. También para centralizar cambios en una LAN y luego enviarlos a otro remoto.


### ¿Cómo se crea y se usa un repo bare?

- Crear el repo: `git init --bare`.

- Clonar el repo: `git clone /my/bare/repo/path .`

o

- Usar el bare repo como remote de un repo preexistente: `git remote add origin /my/bare/repo/path`.

- Comprobar si está añadido como repo remoto: `git remote -v`.

A partir de aquí, en el repo de trabajo haremos como habitualmente, con el staging area, commits y push.
