## Importar y exportar módulos en JS


1. CommonJS - require / module.exports
2. Import ES6 - import / export


## Método Common JS

Para exportar:

- Usando module.exports: `module.exports = {unNombre, dosNombre, nNombre}`

Para importar:

- Usando modulo.nombre:

````
const moduloMatematicas = require("./modulos/fmatematicas.js")

const miSuma = moduloMatematicas.suma(1,2);
````

- Importando al *namespace* local:

````
const {suma, multiplica} = require("./modulos/fmatematicas.js")

const miSuma = suma(1,2);
````

## Método ES6+

Después podemos exportar los elementos escribiendo `export` delante de cada nombre, como `export miFuncion() {}`, lo mismo para variables de cualquier tipo.

Luego se puede importar de las siguientes maneras:

- Importando todo con un alias: `import * as ModuloMatematicas from "./modulos/fmatematicas.js";`
- Importando por nombre: `import { suma } from "./modulos/fmatematicas.js"`

### Export default

Para usar el siguiente método de importación `import miNombre from './modules/literatura.js'`es necesario usar el formato de *export default* con `export default miNombre`.

Sólo puede haber un *default* export por módulo.
## Referencias:

https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Modules

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/expord