# TIMER DE FUNCIONES
import time

def timer(func):
	def wrapper():
		"""
		Tomamos un tiempo de referencia, ejecutamos una función,
		y cuando finalice la ejecución tomamos otro tiempo de referencia.

		La diferencia entre las dos referencias es el tiempo de ejecución
		que queremos determinar.
		"""
		before = time.time()
		func()
		print("La función tardó:", time.time() - before, "segundos")

	return wrapper