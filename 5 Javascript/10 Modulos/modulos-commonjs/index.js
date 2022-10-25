// Importación de módulos con commonjs, es decir, el método antiguo


// Importamos el modulo matematicas con commonjs
const moduloMatematicas = require("./modulos/fmatematicas.js")

// Otra forma de hacerlo
const {suma, multiplica} = require("./modulos/fmatematicas.js")


console.log(moduloMatematicas) // Muestra los elementos que importamos
console.log(moduloMatematicas.factorial) // Muestra info sobre este elemento en particular

// Probamos uno de las funciones importadas con commonjs a ver
const miFactorial = moduloMatematicas.factorial(5)
console.log(miFactorial)


// Probamos el segundo método de llamado de commonjs
console.log(suma(2,3), multiplica(2,3))