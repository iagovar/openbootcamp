
# ESlint con VSCode

1. Creamos carpeta npm-eslint

2. Inicializamos un proyecto de Node con `npm init -y`

3. Instalamos ESLint con `npm install eslint --save-dev` o `npm i -D eslint`

	De esta manera instalamos dependencias que nos ayudarán durante el desarrollo, es decir, están pensadas para ser usadas por nuestro IDE.

	Aparecerán como `devDependencies` en nuestro *package.json*, no como dependencias de la propia aplicación que estamos desarrollando, a la hora de ejecutar un `build` o algún comando similar.

4. Ejecutamos `npm init @eslint/config`, que nos mostrará un *prompt* con un arbol de preguntas en consola para averiguar qué tipo de archivo queremos generar.

	Una de las cosas que pregunta es sobre line endings, por si desarrollas en Linux o Windows (LF vs CRLF), lo que puede causar problemas, no sólo con ESLint sino también con Git. [+info](https://daksh.github.io/line-endings/) - [Documentación ESLint](https://eslint.org/docs/latest/rules/linebreak-style)

5. Para poder usar ESLint en VSCode habría que usar la extensión de ESLint de Microsoft. En Sublime Text es posible, pero hay que dar más vueltas.


---

- Dentro de un archivo JS puedes desactivar ESLint para un número determinado de líneas envolviendo el código en `/* eslint-disable */` y `/* eslint-enable */`. 

	También se puede desactivar una línea en concreto con `// eslint-disable-line`.

	Para desactivar alguna regla concreta, por ejemplo sobre *quotes* sería `// eslint-disable-line quotes` en caso de ser para una línea.

## Usando reglas de terceros

Como se indica en la [documentación oficial](https://eslint.org/docs/latest/user-guide/getting-started), los archivos de config de ESLint importan por defecto una serie de reglas creadas por la gente de ESLint, pero se pueden importar muchas otras que se pueden encontrar en [npmjs.com](https://www.npmjs.com/search?ranking=popularity&q=eslint-config).

Cada una de las reglas incluyen documentación en npm de cómo usarlas.

## Correr ESlint fuera del IDE

ESLint asume que has creado un archivo *package.json*, de manera que la forma de hacerlo es incluírlo como un escript.

Útil puede ser:

- "lint": "eslint ."
- "lint-fix": "eslint --fix ."

Una vez incluídos en el *package.json* en la consola corremos los scripts con `npm run nombre-del-script|lint|lint-fix` y nos pintará la consola con el resultado.

El sufijo `--fix` corrige automáticamente los fallos de estilo detectados.

