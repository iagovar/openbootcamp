/*
Crea un archivo JS que contenga las siguientes líneas)
*/

// Una variable que contenga la lista de la compra (mínimo 5 elementos

const listaDeCompra = ["Patatas", "Tomates", "zanahoria", "Caldo de pollo", "Ajo"]

// Modifica la lista de la compra y añádele "Aceite de Girasol"

listaDeCompra.push("Aceite de Girasol")

console.log(listaDeCompra)

// Vuelve a modificar la lista de la compra eliminando "Aceite de Girasol"

let indexNecesario = listaDeCompra.indexOf("Aceite de Girasol")
listaDeCompra.splice(indexNecesario, 1)

console.log(listaDeCompra)

// Una lista de tus 3 películas favoritas (objetos con propiedades: titulo, director, fecha)

listaDePeliculas = [
    {titulo: "Las aventuras de fulanito", director: "Menganito", fecha: "1987/12/1"},
    {titulo: "Jungla de Cristal", director: "Señor X", fecha: "1986/12/3"},
    {titulo: "Alicia ya tal", director: "Un Director", fecha: "2012/10/1"}
]

// Una nueva lista que contenga las películas posteriores al 1 de enero de 2010 (utilizando filter)

let nuevaLista2010 = listaDePeliculas.filter(comprobarFecha)

function comprobarFecha(elemento) {
    let fecha = new Date(elemento.fecha).getFullYear();
    return fecha > 2010; // Se ejecuta la condición sin necesidad de un IF
}

console.log(nuevaLista2010)

// Una nueva lista que contenga los directores de la lista de películas original (utilizando map)

let nuevaListaDirectores = listaDePeliculas.map(valor => valor.director)

console.log(nuevaListaDirectores)

// Una nueva lista que contenga los títulos de la lista de películas original (utilizando map)

let nuevaListaTitulos = listaDePeliculas.map(valor => valor.titulo)

console.log(nuevaListaTitulos)

// Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando concat)

let nuevaListaConcat = nuevaListaDirectores.concat(nuevaListaTitulos)

console.log(nuevaListaConcat)

// Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando el factor de propagación)

let nuevaListaFactorPropagacion = [...nuevaListaDirectores, ...nuevaListaTitulos]

console.log(nuevaListaFactorPropagacion)