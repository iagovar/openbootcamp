export function suma(a, b) {
    return a + b
}

export function multiplica(a, b) {
    return a * b
}

export function eleva(a, b) {
    return a ** b
}

export function factorial(a) {
    // factorial de 5: 5 * 4 * 3 * 2 * 1
    let resultado = 1;
    for (let index = a; index > 0; index--) {
      resultado *= index;
    }
    return resultado;
}

