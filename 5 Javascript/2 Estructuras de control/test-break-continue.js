// Ejecutar con $ node ./test-break-continue.js

// Un pequeño ejemplo sobre break y continue


for (let numero = 0; numero < 100; numero++) {

	console.log("\n Inicio del bucle");

	if (numero == 0) {console.log("\n Numero es 0, continue"); continue};

	if (numero == 10) {console.log("\n Numero es 10, break"); break};

	console.log("\n\t" + numero);

	console.log("\n Fin del bucle");
};