
// MAP: Crea un nuevo array llamando una función para cada elemento del array previo
// https://www.w3schools.com/jsref/jsref_map.asp

const array = ["San Sebastián", "Madrid", "Barcelona", "Alicante", "Bilbao"]

const nuevoArray = array.map((valor, indice) => `${indice +1} - ${valor}`)
// ['1 - San Sebastián', '2 - Madrid', '3 - Barcelona', '4 - Alicante', '5 - Bilbao']



// FILTER: Crea un nuevo array con los elementos que pasan el filtro del array anterior
// https://www.w3schools.com/jsref/jsref_filter.asp

const listaObjetos = [
    { nombre: "Leire", edad: 35 },
    { nombre: "Gorka", edad: 34 },
    { nombre: "Miguel", edad: 28 },
    { nombre: "Lucía", edad: 3 },
    { nombre: "Amaia", edad: 29}
]


const nuevoArrayFiltrado = listaObjetos.filter(valor => valor.edad > 30)
//  { nombre: 'Leire', edad: 35 }, { nombre: 'Gorka', edad: 34 } ]



// REDUCE: El método reduce() ejecuta una función reductora sobre cada elemento de un array, devolviendo como resultado un único valor.
// Vídeo explicativo: https://www.youtube.com/watch?v=VVySn87s8Eo
// MDN: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
console.clear()


    // Vamos a sumar todas las edades de ListaObjetos para probar
nuevoArrayReducido = listaObjetos.reduce(miArrayReducer, 0) // CallBack, ValorInicial

function miArrayReducer(acumulador, valorActual) {
    console.log(`Acumulado: ${acumulador}, Valor actual (edad): ${valorActual.edad}`);
    acumulador += valorActual.edad;
    return acumulador;
}

console.log(`El valor final de .reduce() es: ${nuevoArrayReducido}`);

/*
Output consola: 

Acumulado: 35, Valor actual (edad): 35
Acumulado: 69, Valor actual (edad): 34
Acumulado: 97, Valor actual (edad): 28
Acumulado: 100, Valor actual (edad): 3
Acumulado: 129, Valor actual (edad): 29
El valor final de .reduce() es: 129

*/