// Calcula el factorial de un número
// Para ello itera sobre el entero a factorizar, y va multiplicando los factores
// y guardando el resultado en factorialResultado


let numeroFactorizar = 10;
let factorialResultado = 1;

let bucle = numeroFactorizar;

while (bucle > 0) {
	factorialResultado *= bucle;
	bucle--;
}

console.log(`\n\t El factorial de ${numeroFactorizar} es ${factorialResultado} \n`);