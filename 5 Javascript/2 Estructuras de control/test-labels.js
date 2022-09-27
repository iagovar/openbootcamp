// Test labels

// Construímos un número del 0.0 al 10.0 con dos bucles

let unidades = 0
let decenas  = 0

console.log("Inicio de Labels");

bucleUnidades: while (true) {
	bucleDecenas: while (true) {

		console.log("\t" + unidades + "." + decenas);
		decenas++;

		if (unidades == 10) {break bucleUnidades}
		if (decenas == 10) {decenas = 0; break bucleDecenas}
	}

	unidades ++
}

console.log("Fin de Labels");