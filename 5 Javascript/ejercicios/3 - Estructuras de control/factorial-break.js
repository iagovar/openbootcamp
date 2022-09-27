// Calcula el factorial de un número
// Para ello itera sobre el entero a factorizar, y va multiplicando los factores
// y guardando el resultado en factorialResultado


let numeroFactorizar = 10;
let factorialResultado = 1;

let bucle = numeroFactorizar;

while (true) {
	factorialResultado *= bucle;
	bucle--;

	if (bucle == 0) {break}
}

console.log(`\n\t El factorial de ${numeroFactorizar} es ${factorialResultado} \n`);