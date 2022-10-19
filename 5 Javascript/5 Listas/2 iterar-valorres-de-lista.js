


const array = ["hola", 1,2,3, true, null, "adios"]
array.propiedadPersonalizada = "Esto es una propiedad personalziada";


for (valor of array) {
    console.log(valor) // Muestra un listado de todos los valores
}

for (valor in array) {
    console.log(valor) // Muestra un listado de los índices, asi que se puede acceder a los valores con valor[indice]
}


// .forEach permite correr una función por cada elemento
array.forEach(elemento => {console.log(elemento)})

// Esto puede ser útil para para ejecutar operaciones sobre cada elemento, o todo el array
// Problemos, por ejemplo, sumar todos los valores de un array

let suma = 0;
const arrayNums = [1,2,3,4,5,6,7,8,9,10];

arrayNums.forEach(valor => {
    suma += valor;
    console.log(valor);
})

console.log(`Esto es una suma del array: ${suma}`);



// Buscar un valor dentro de una lista con .find()
console.clear()

    // Recordemos el array inicial: const array = ["hola", 1,2,3, true, null, "adios"]

    /*
    Según: https://www.w3schools.com/jsref/jsref_find.asp

    The find() method returns the value of the first element that passes a test.

    The find() method executes a function for each array element.

    The find() method returns undefined if no elements are found.

    The find() method does not execute the function for empty elements.

    The find() method does not change the original array.

    */

    const encontrado = array.find(valor => {
        if (valor === "adios") {return true} // mientras no se retorne false, undefined o NaN devolverá "adios"
    })

    console.log(encontrado)

    // Otro ejemplo de uso
    console.clear()

    const listaObjetos = [
        { nombre: "Leire", edad: 35 },
        { nombre: "Gorka", edad: 34 },
        { nombre: "Miguel", edad: 28 },
        { nombre: "Lucía", edad: 3 },
        { nombre: "Amaia", edad: 29}
    ]

    // Si hay un objeto.nombre == "Miguel", obtenemos su edad

    const miObjeto = listaObjetos.find(valor => valor.nombre === "Miguel") // Las funciones flechas con esta sintaxis implican return valor.nombre == "Miguel"

    console.log(miObjeto.edad)
