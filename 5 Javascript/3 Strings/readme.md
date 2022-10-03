# Strings

La principal diferencia es que los *f-strings* se sustituyen por [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), con los caracteres ` `` ` o *backticks* como se les llama en inglés.

Los *template literals* permiten no sólo incrustar variables en el texto con `${variable}` sino que respetan también los saltos de línea, con lo cual es fácil incustar código HTML dentro de una variable, por ejemplo:

````
let otraVariable = "Esta es otra variable";

let miVariable = `<div class="miDiv">Este código muestra el valor de otra variable: ${otraVariable}</div>`;

console.log(miVariable);
// <div class="miDiv">Este código muestra el valor de otra variable: Esta es otra variable</div>
````

## Métodos y atributos de strings

### Atributos

 - `miCadena.lenght` es el atributo que devolverá la longitud.

### Métodos

Hay un buen resumen de de los métodos disponibles en [w3schools](https://www.w3schools.com/jsref/jsref_obj_string.asp).

- `miCadena.slice(inicio excluido, final incluido)` corta una cadena por los parámetros indicados.

	El mismo funcionamiento tiene el método `.substring()`. 

- `miCadena.replace('aCambiar', 'reemplazo')` permite reemplazar un texto por otro. Sólo lo hace **para la primera instancia** que encuentra. 

	Para hacerlo con todas habrá que usar REGEX.

	`/g` (global) en REGEX permite apuntar a todas las instancias, de tal forma que para reemplazar todas nos quedaría `miCadena.replace(/aCambiar/g, 'reemplazo')`.

- En JS se puede concatenar con `str + str`, el problema es que en este lenguaje si una cadena de texto es un número (p. ej. "1"), puedes acabar haciendo una operación aritmética en lugar de una concatenación, por eso es preferible usar `.concat` o template literals.

- Los métodos `trim()`, `trimEnd()` y `trimStart()` eliminan los espacios y son autoexplicativos, de manera similar a python.


- Con expresiones regulares y `.match()` podemos obtener una lista que contiene todas las veces que se ha encontrado la expresión.

Por lo demás, el resto de métodos no tienen mucho de particular.