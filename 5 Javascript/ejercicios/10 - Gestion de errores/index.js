const miLogger = require("./logger");


function unaFuncion(numero) {
	if (typeof numero !== "number") {throw new Error("Este es un error personalizado")};
	return numero * 2
}


try {
	miVariable = unaFuncion("No es un número!");
	miLogger.log("La operación tuvo éxito")
} catch(unErrorPersonalizado) {
	miLogger.error(`${unErrorPersonalizado}`)
}
