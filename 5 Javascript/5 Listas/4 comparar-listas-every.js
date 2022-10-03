/* EVERY: Devuelve un boolean si todos los elementos del array cumplen una condicion  

Ver: https://www.w3schools.com/jsref/jsref_every.asp
*/

const listaObjetos = [
    { nombre: "Leire", edad: 35 },
    { nombre: "Gorka", edad: 34 },
    { nombre: "Miguel", edad: 28 },
    { nombre: "Lucía", edad: 3 },
    { nombre: "Amaia", edad: 29}
]

// Every con una función normal

const masDe30 = listaObjetos.every(comprobarMasDe30)

function comprobarMasDe30(currentValue) {return currentValue.edad > 30}
// false

// Every con una función anónima normal

const masDe30anonima = listaObjetos.every(function(currentValue) {return currentValue.edad > 1})
// false

// Every con una función flecha

const masDe30Flecha = listaObjetos.every(currentValue => currentValue.edad > 30)
// false



/*
        Comparación de listas

    En JS las listas no se pueden comparar con operadores de comparación,
    sino elemento por elemento.
*/


lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [1,2,3,4,5,6,7,8,9]

// console.log(lista1 === lista2) --> false

sonListasIguales = lista1.every((currentvalue, arrayPos) => currentvalue == lista2[arrayPos])

console.log(sonListasIguales) // true