### Operadores de comparación
Ver [este artículo de javascript.info](https://javascript.info/comparison#comparison-of-different-types).

A grandes rasgos, la diferencia notable con Python es la siguiente. El artículo contiene más particularidades extrañas de JS, aunque no se mencionan en el curso (de momento).

- `==` Compara valores
- `===` Compara valores y tipos

### Estructuras IF

Muy similar a python, con keywords  `if`, `else if`,`else`.

### Estructuras SWITCH

El equivalente a MATCH en Python.

Nótese la keyword `default` que permite establecer un flujo por defecto si no se cumplen el resto de condiciones o casos.

````

switch(expression) {
  case x:
    // expression se evalua como x, y se ejecuta el código
    break;
  case y:
    // expression se evalua como y, y se ejecuta el código
    break;
  default:
    // La evaluación no coincide con ningún case, asi ejecuta el default
}

````

### Bucles FOR

Los bucles FOR en JS son algo diferentes que en python, tienen mayor variedad en su léxico. Veamos:

- Bucles FOR estándar, con `for (inicializacion; condición; iteración) {}`
- Bucles FOR OF, pensado para iterables, con `for (variable in iterable) {}`
- Bucles FOR IN, pensado para objetos, con `for (key in object) {}`
- Método forEach() sobre iterables, con `miArray.forEach(miFuncion)`

#### Ejemplos de código

Bucle for estándar:

````
for (let miVar = 0; miVar < 10; miVar++){
    console.log(miVar);
}

// 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
````

Bucle for of para iterables:

````
let miLista = [1, 2, 3, 4, 5]

for (let variable in miLista) {
    console.log(variable)
}

// 1, 2, 3, 4, 5
````

Bucle for in, para objetos:

````
let miObjeto = {
    key1: "valor1",
    key2: "valor2"
}

for (let miVar in miObjeto) {
  console.log("Asi imprimes la key: " + miVar + " y así el valor: " + miObjeto[miVar])
}

// Asi imprimes la key: key1 y así el valor: valor1
// Asi imprimes la key: key2 y así el valor: valor2
````

### Bucles WHILE y DO WHILE

Python no tiene bucles DO WHILE, pero es sencillo entender. Simplemente, la condición se comprueba al final del bucle, no antes, con la siguiente sintaxis.

````
do {
  // code block to be executed
}
while (condition);
````

Es necesario apuntar que si vamos a usar una variable en la condición, debemos inicializarla antes del bucle y cambiar su valor, o el bucle puede romper el runtime del navegador.

### Control de bucles con BREAK y CONTINUE

Exáctamente igual que python. `BREAK` rompe la ejecución del bucle y sale fuera de él, mientras que `CONTINUE` simplemente salta a la siguiente iteración del bucle, ignorando el código que se delcara después del propio `CONTINUE`.

#### LABELS en bucles

JS tiene una característica que no tiene Python, y es que se pueden asignar nombres o etiquetas a los bucles, y a las sentencias BREAK y CONTINUE. Hay más información [en MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label).