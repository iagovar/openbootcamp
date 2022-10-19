// Los sets son conjuntos de valores únicos y no ordenados
// https://www.w3schools.com/js/js_object_sets.asp


/* Los sets no se pueden definir como en Python
   En JavaScript es necesario un construcctor.

   Es decir, esto no es válido: const miSet = {1,2,3,4,5,6}

   Es necesario pasar los valores con la siguiente sintaxis
*/

const miSet = new Set([1,2,3,4,5,6,7,8,9,9,9,9])

console.log(miSet)

/* Los métodos para sets no tienen nada de particular.

   Lo único notar que no se puede acceder mediante índices,
   ya que es un objeto no ordenado
*/

miSet.add("un elemento")

console.log(miSet)

miSet.delete("un elemento")

console.log(miSet)

// Como no podemos usar índices, iteramos con valores


miSet.forEach(valor => console.log(valor))

console.clear()

// O también

for (valor of miSet) {console.log(valor)}