## Conceptos a explorar

- Relaciones many-to-many: [Pequeña introducción teórica en YT](https://www.youtube.com/watch?v=1eUn6lsZ7c4)


- Tablas particionadas: Al menos en postgre se pueden particionar tablas para mejorar su rendimiento, cuando tienen muchos registros.

- Los wildcards para Postgre son tipo ``SELECT columna1, columna2 FROM tabla WHERE columna2 LIKE '%keyword%'`` donde % es el wildcard. 

- primary y foreign keys, explorar más

- Full outer join aparentemente devuelve todos los registros?

	Sí, devuelve todos los registros de las tablas implicadas, tengan valores correspondientes o no.

	[Breve explicación en YT](https://youtu.be/UfgRTbRN9FM?t=429)

- ¿Por qué la clausula WHERE debe ir después del JOIN y no al revés?