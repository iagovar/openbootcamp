## Tipado en JS

El tipado en JS es tipado "inferido" (dinámico), es decir, el intérprete asignará un tipo en *runtime*. 

- Ventajas: Menor esfuerzo requerido a la hora de escribir el código. Prototipado mucho más rápido.
- Desventajas: El intérprete/compilador no nos mostrará un error si le asignamos un valor que no debería tener a una variable. Esto significa que el error nos saltará en *runtime* cuando exista algún conflicto.


## Tipos de datos

### Primitivos

Ver [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Primitive).

- Number -> Ver [Bigint VS Number en JS](https://stackoverflow.com/questions/61583163/javascript-data-type-bigint-vs-number).
- String -> Admite ambos tipos de comillas y `también.
- Boolean
- Null -> `typeof null` devuelve `Object`. Esto se considera un bug no solucionable por cuestiones de retrocompatibilidad. 
- Undefined -> No tiene asignación en memoria.

---
-  null, undefined, false, 0 ==> Falsy, esto es, se interpretan como False en flujos.

---
### Listas

Dos formas de definirlas:

````
const lista = [1, "hola", true, undefined, null];
````
O también nos sirve:
````
const lista2 = new array(1, "hola", true, undefined, null);
````

Necesario apuntar que aunque se definen como constantes, es posible cambiar los valores que están dentro de la lista.

````
// Cambiando el primer elemento de lista
lista[0] = "soy un nuevo valor";
````

En JS las listas también pueden contener listas a su vez, y cualquier tipo de valor u objeto en realidad.

### Objetos

Muy similar a Python, aunque la notación es diferente.

````
const miObjeto = {
	atributo_1: "Valor",
	atributo_2: [1,2,3],
	atributo_objeto: {
		atributo_anidado_1: "Valor_1",
		atributo_anidado_2: 100
	},
	// Nombre de atributo con caracteres no admitidos se define con ""
	"atributo-con-guones-medios": 101
};

console.log(miObjeto.atributo_objeto);
// Output: {atributo_anidado_1: "Valor_1", atributo_anidado_2: 100}


// Cambiamos un atributo
miObjeto.atributo_1 = "Nuevo valor";

console.log(miObjeto.atributo_1);
// Output: "Nuevo valor"
````

### Fechas
Las fechas son un poco liosas. Por ejemplo, los meses se ejecutan como un índice, siendo 0 -> Enero, y 11 -> Diciembre.

También es necesario notar que el siguiente código sólo funciona con Node.js, no en la consola del navegador, desconozco el motivo.

````
const ahora = new Date();
// Sat Sep 24 2022 13:01:45 GMT+0200 (hora de verano de Europa central)

const fecha_milisegundos = new Date(10);
// 10 Milisegunods desde el 1 de Enero de 1970
// Thu Jan 01 1970 01:00:00 GMT+0100 (hora estándar de Europa central)

const fecha_cadena = new Date("march 25 2020");
// Wed Mar 25 2020 00:00:00 GMT+0100 (hora estándar de Europa central)

const fecha_valores = new Date(20, 0, 2022);
// Mon Jan 24 2022 00:00:00 GMT+0100 (hora estándar de Europa central)
// Notamos que el MES 0 --> Enero, como ya advertimos se tratan como un índice

const dia = ahora.getDate() 		// 24
const mes = ahora.getMonth() + 1	// 9
const anho = ahora.getFullYear()	// 2022

console.log(dia, mes, anho)
// 24 9 2022
````


## Declaración de variables

- var
- let -> Método preferido por consenso a partir de su introducción en ES6.
- const

Ver [let vs var en w3schools](https://www.w3schools.com/JS/js_let.asp).

La principal diferencia es que LET tiene block scope y VAR no. Con lo cual, es fácil declarar una variable con VAR dentro de, por ejemplo, un bucle FOR, sin recordar que está definida en otro lugar de un nivel superior, y cambiar su valor. Esto con LET no pasa, no sólo porque no se puede redeclarar dentro del mismo scope, sino que declaraciones con el mismo nombre en scopes diferentes apuntan a bloques de memoria diferentes.

## Notación

Similar a Python, con las siguientes diferencias:

- `;` Es el método clásico de finalizar una línea. Hoy en día se puede ignorar, aunque se sigue recomendando su uso.
- `{}` Para objetos, funciones y estructuras de control, tal que:

    Definimos un objeto:
    ````
    const movil = {
        anchura: 5,
        altura: 10
    };
    ````
	Definimos una función:
	````
	function nombre(arg1, arg2) {
	// Aquí se define la función
	};
	````
	Ejemplo de estructura de control:
	````
	if (true) {
	// Cuerpo de la estructura de control
	};
	````