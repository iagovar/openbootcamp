// Método ES6:
// 1. Creamos carpeta modulos-es6 [Lo obviamos porque hemos reestructurado los archivos de la clase]
// 2. Ejecutamos "npm init -y" dentro de modulos-es6
// 3. Agregamos "type":"module" dentro del package.json
// 4. Copiamos modulos/fmatematicas.js a modulos-es6/modulos/fmatematicas.js
// 5. Escribimos "export" antes del nombre de todas las funciones a exportar y eliminamos "module.exports = {}" que ya no necesitamos


// Primera forma de hacerlo
// import { suma } from "./modulos/fmatematicas.js"

// Segunda forma de hacerlo
import * as ModuloMatematicas from "./modulos/fmatematicas.js";


// Primer método
// const sum = suma(1,2);

// Segundo método
const sum = ModuloMatematicas.suma(1,2);

console.log(sum);

// Probando el export default de literatura.js
import getAutor, {miConstante} from "./modulos/literatura.js";

console.log(getAutor(), miConstante);