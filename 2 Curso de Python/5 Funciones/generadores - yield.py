def genera_pares(limite):
	"""
	 - Codigo Facilito
	 https://www.youtube.com/watch?v=TLVnoqXGWpY
	 https://www.youtube.com/watch?v=ucaHqGII350

	Una función generador devuelve con YIELD un objeto generador
	donde se van almacenando, uno a uno, poco a poco, diversos elementos.

	Estos elementos devueltos pueden ser de naturalezas diferentes.
	"""

	num = 1

	while num < limite:

		yield num*2

		num = num + 1
 
devuelvepares = genera_pares(10)

print(next(devuelvepares))

print("Aquí iría un bloque de código\nSe pausa la función genera_pares hasta que se le llama de nuevo.")

print(next(devuelvepares))

