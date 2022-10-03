

## Precisión numérica

Quizá la mejor explicación sobre qué es y cómo resolver los problemas de precisión numérica en JS es [este enlace](https://javascript.info/number#imprecise-calculations.)

Básicamente la idea es usar la siguiente sintaxis:

````
let sum = 0.1 + 0.2;
alert( +sum.toFixed(2) ); // 0.3
````

### toFixed()

Se usa el método `.toFixed()` junto con `+` delante para forzarle a devolver un número en lugar de string. En cualquier caso esto sólo limita los decimales, no aumenta la precisión de la operación.

Para aumentar la precisión se puede tratar de convertir los números en enteros y luego en float de nuevo.


## NaN (Not a Number)

````
let n = Number('Hola');
console.log(n);
// Devuelve: NaN
````

## Infinity

````
let numerador = 19;
let denominador = 0;

console.log(numerador / divisor);

// Devuelve Inifinity
````

## Casting

````
let cadena = '5.89';
let numero = 17.2;

console.log(Number(cadena) + numero); // 23.09
console.log(parseInt(cadena) + numero); // 22.2 (Ya que hace 5.89 -> 5, a entero)
console.log(parseFloat(cadena) + numero); // 23.09
````

## Números Hexadecimales (base 16)

Para hacer casting de números hexadecimales, podemos usar `parseInt(numHex, base)`.

````
let numHex = '0x3a5b7';
console.log(parseInt(numHex, 16));
````