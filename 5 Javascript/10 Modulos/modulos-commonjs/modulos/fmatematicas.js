function suma(a, b) {
    return a + b
}

function multiplica(a, b) {
    return a * b
}

function eleva(a, b) {
    return a ** b
}

function factorial(a) {
    // factorial de 5: 5 * 4 * 3 * 2 * 1
    let resultado = 1;
    for (let index = a; index > 0; index--) {
      resultado *= index;
    }
    return resultado;
}

// Método de exportación de common.js
module.exports = {
    suma,
    multiplica,
    eleva,
    factorial
}