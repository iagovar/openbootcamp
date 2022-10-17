
// Funcion simple
function verdadero() {
  return true
}

// Función asíncrona
async function miFuncionAsincrona() {
  setTimeout(() => console.log("Hola soy una promesa"), 5000)
}

// función generadora
function* generadora() {
  let miNumero = 0;
  while (true) {
    miNumero += 2;
    yield miNumero;
  }
}

// Probamos primera funcion
console.log(verdadero())

// Probamos la función asíncrona
miFuncionAsincrona()

// Probando la función generadora

let miVariable = generadora();

console.log(miVariable.next())
console.log(miVariable.next())
console.log(miVariable.next())
console.log(miVariable.next())
console.log(miVariable.next())
console.log(miVariable.next())

