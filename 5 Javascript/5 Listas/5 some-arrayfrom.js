// .some() es un método similar a .every(), con la diferencia de que devolverá True si algún elemento cumple la condición
// https://www.w3schools.com/jsref/jsref_some.asp


const listaObjetos = [
    { nombre: "Leire", edad: 35 },
    { nombre: "Gorka", edad: 34 },
    { nombre: "Miguel", edad: 28 },
    { nombre: "Lucía", edad: 3 },
    { nombre: "Amaia", edad: 29}
]

const algunoMasDe30 = listaObjetos.some(elemento => elemento.edad > 30); // true

// Array.from() es un método estático (es decir, sólo se puede usar con esta sintaxis),
// Que devuelve un array: https://www.w3schools.com/jsref/jsref_from.asp

const nuevoArray = Array.from("Esto es un string")

console.log(nuevoArray)