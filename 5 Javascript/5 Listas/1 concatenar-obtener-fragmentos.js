// Unir dos listas con lista1.concat(lista2)
// Esto NO modifica lista1 ni lista2

const lista1 = ["hola", 2, false, null];
const lista2 = ["adios", 9, true, undefined];

const lista3 = lista1.concat(lista2)  // ['hola', 2, false, null, 'adios', 9, true, undefined]

// Unir listas con el factor de propagación (...)

console.log(...lista3) // Esto nos muestra los valores de la lista por separad: hola 2 false null adios 9 true undefined 

const lista4 = [lista1, lista2] // Obtienes una lista, con dos elementos que son dos listas

const lista5 = [...lista1, ...lista2] // Obtienes una lista con todos los elementos de lista 1 y lista 2

console.log(lista5)






// Obtener un fragmento de una lista a partir de otra con .slice(indice_inicio_incluido, indice_fin_excluido)

const array = ["hola", 1,2,3, true, null, "adios"]

const array2 = array.slice(1, 4) // [1,2,3]

const array3 = array.slice(-6, -3) // [1,2,3]  También acepta valores negativos, como podemos ver

console.log(array3)
