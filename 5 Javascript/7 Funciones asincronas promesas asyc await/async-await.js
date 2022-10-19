// Creamos la función asíncrona/ejecutora
async function generaTexto() {
  let unTextoCualquiera = "Devuelvo este texto"
  return unTextoCualquiera;
}


// Podemos consumir la promesa con .then()
// Devuelve en consola: Devuelvo este texto
generaTexto().then(
  (x) => (console.log(x)),
  (y) => (console.log(y))
)

// Podemos consunsumirla dentro de una función asíncrona con await
async function getTexto() {
  let unTexto = await generaTexto();
  console.log(unTexto);
}

// Llamamos a nuesta función de consumo para ejecutarla
// Devuelve en consola: Devuelvo este texto
getTexto()


// ¿Y qué pasa si tratamos de consumir generaTexto() directamente?
// Devuelve en consola: Promise { [[PromiseStatus]]:resolved, [[PromiseValue]]:Devuelvo este texto }
console.log(generaTexto())