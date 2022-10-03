Ver archivos JS del directorio

## Diferencias notables

En JS existe algo llamado *factor de propagación*. Ilustramos;

````
console.log(...lista3) // Esto nos muestra los valores de la lista por separad: hola 2 false null adios 9 true undefined 

const lista4 = [lista1, lista2] // Obtienes una lista, con dos elementos que son dos listas

const lista5 = [...lista1, ...lista2] // Obtienes una lista con todos los elementos de lista 1 y lista 2
````

Esta sintaxis con `...` antes del nombre de una lista es lo que se llama *factor de propagación* y su comportamiento es el descrito arriba.