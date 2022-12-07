/*
Crea un nuevo fichero JS que contenga las siguientes líneas

- Una función que admita un parámetro "num", y devuelva una lista con esa cantidad de números de la secuencia de Fibonacci (Por ejemplo: num = 6 => Resultado [1, 1, 2, 3, 5, 8])

- Ejecuta la depuración de VSCode para visualizar la ejecución de la función
*/

function miFuncion(num) {
    // Devuelve NUM enteros en secuencia fibonacci

    const miLista = [1];
    let indice = 0

    while (miLista.length < num) {
        let miSuma = 0;

        if (indice == 0) {
            miSuma = 1;
        } else {
            miSuma = miLista[indice-1] + miLista[indice];
        }

        miLista.push(miSuma);
        indice++;
    }

    return miLista;
}

const resumen = miFuncion(6)

console.log(resumen)

