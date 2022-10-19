
// Importamos controller.js
import * as controlador from './controller.js';


// Usamos controller.js
const miSuma = controlador.suma(2,3);

const miMultiplica = controlador.multiplica(2,3);

// importamos la lib chalk
// https://www.npmjs.com/package/chalk
import chalk from "chalk";


// Imprimimos con chalk
console.log(chalk.red(`Suma ${miSuma}, multiplicacion ${miMultiplica}`))