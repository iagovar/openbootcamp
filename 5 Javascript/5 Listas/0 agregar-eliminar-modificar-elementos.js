
let var1 = { id: false};
let array = [1, "hola", false, {id: 5 }, null, undefined, var1];

// Se accede de forma similar a python

console.log(array[1]) // hola

// Introducir nuevos valores

array.push("Este valor va al final"); // Push meter los valores al final

array.unshift("Este valor va al inicio"); // Unshift coloca los valores al principio del array

// Eliminar valores

array.pop(); // Elimina valor del final del array

array.shift(); // Elimina el valor del inicio


// Eliminar valores con .splice(indice, num_valores_eliminar)
array2 = [1,2,3,4,5,6,7,8,9,10];

array2.splice(0, 2); // .splice(a_partir_de_que_indice, cuantos_valores_elimino), en este caso del indice 0 elimina dos valores.




// agregar valores con .splice(indice, num_valores_eliminar, agrego_1, agrego_2, ... , agrego_n)

array2.splice(0, 0, "primer_valor", "segundo_valor"); // .splice permite agregar y eliminar parámetros con un mismo método. En este caso no elimina porque el segundo parámetro es 0




// Modificar valores con .splice(indice, elementos_a_eliminar, elementos_a_agregar)
// Ahora mismo tenemos: array2 = ['primer_valor', 'segundo_valor', 3, 4, 5, 6, 7, 8, 9, 10]

array2.splice(2, 1, "tercer_valor"); // El 3 está en el índice 2, lo eliminamos (eliminamos un valor con "1"), y metemos "tercer_valor" en ese mismo índice

array2.splice(2, 2, "tercer_valor", "cuarto_valor"); // Similar al anterior, eliminamos "tercer_valor" y 4, y añadirmos "tercer_valor" y "cuarto valor"


console.log(array2);