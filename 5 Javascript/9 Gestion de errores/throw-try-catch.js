const miFuncion = valor => {
  // Definimos una condición y un error
  if (typeof valor !== "number") {throw new Error("Es necesario pasar un número en miFuncion()")}
  return 2 * valor
};

try {
  // Código que intentaremos ejecutar
  const tempVariable = miFuncion("no es un numero!")
  console.log("Ejecutándose de manera correcta")
  console.log(tempVariable)
} catch(error) {
  // catch() puede recoger el error que definimos antes como argumento
  // para usarlo como variable
  console.error(`Algo chungo ha pasado: ${error}`)
} finally {
  console.log("Esto se ejecutará de igual manera")
};