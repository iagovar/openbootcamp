//Crea un archivo llamado objetos.js que contenga las siguientes líneas

//- Un objeto con tus datos personales (nombre, apellido, edad, altura, eresDesarrollador)

const miObjeto = {
    nombre: 'Iago',
    apellido: 'Var',
    edad: 35,
    altura: '180',
    eresDesarrollador: true
}

//- Una variable que obtenga tu edad a partir del objeto anterior

const miEdad = miObjeto['edad']

//- Una lista que contenga el objeto con tus datos personales y un nuevo objeto con los datos personales de tus dos mejores amig@s


const miHermano = {
    nombre: 'Juan',
    apellido: 'Var',
    edad: 48,
    altura: 170,
    eresDesarrollador: false
}


const miHermana = {
    nombre: 'Elsa',
    apellido: 'Var',
    edad: 42,
    altura: 160,
    eresDesarrollador: false
}

let miLista = [miObjeto, miHermano, miHermana]


//- Una nueva lista con los objetos de la lista anterior ordenados por edad, de mayor a menor

// Ver .sort() en: https://www.w3schools.com/js/js_array_sort.asp
// Numeric sort tiene sus particularidades

    // como tiene que ser una nueva lista, hagamos simplemente:
    let nuevaLista = []
    for (let valor of miLista) {nuevaLista.push(valor)};

    // Ordenemos la lista por edad

    nuevaLista.sort(ordenarPorEdad)

    function ordenarPorEdad(primerValor, segundoValor) {
        // Ordena por edad de menor a mayor
        return primerValor.edad-segundoValor.edad
    }

    console.log(nuevaLista) // !!! Javascript no tiene id() como en python