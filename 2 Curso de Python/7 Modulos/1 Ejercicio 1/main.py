"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
"""

import operaciones as op


a = 2
b = 3
suma 			= op.suma(a, b)
resta 			= op.resta(a, b)
multiplicacion 	= op.multiplicacion(a, b)
division		= op.division(a, b)
directorio		= dir(op)

print(f"""
Con los parámetros a: {a} y b: {b} importamos el módulo 'operaciones' teniendo los siguientes resultados:
\n
Suma: {suma}
Resta: {resta}
Multiplicacion: {multiplicacion}
Division: {division}
\n
Como output de dir() mostramos:
\n
{directorio}

""")