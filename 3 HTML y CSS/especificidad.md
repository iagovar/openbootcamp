Recursos:

https://www.w3schools.com/css/css_specificity.asp
https://www.codecaptain.io/tools/css-specificity-calculator

La especificidad es la puntuación que el navegador asigna a cada selector CSS.

Cuando existen dos selectores apuntando a un mismo elemento, ¿Cómo se decide qué selector aplicar en caso de conflicto? El que tenga mayor puntuación en especificidad.

¿Y si dos selectores en conflicto tienen la misma puntuación? En este caso sería el último selector declarado en la hoja de estilos.


## Estructura de prioridad en CSS (Especificidad)

Selector 							Puntuación

!Important							Total -> No se computa, simplemente se fuerza
Inline								1000
IDs									100
Clases, pseudo-clases, atributos	10
Elementos y pseudo-elementos		1
*									0


Anidaciones como >, +, etc pueden hacer un elector más específico, pero no añaden puntuación.

## Ejemplos de cálculo

CSS 								Puntuación

#navbar p#demo						100 + 1 + 100 = 201

#heading nav ul li.disabled			100 + 1 + 1 + 1 + 10 = 113

body a[href="something"]			1 + 1 + 10 = 12

#blog article:last-child			100 + 1 + 10 = 111