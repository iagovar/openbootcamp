"""
Este documento incluye primero una explicación básica, y más abajo dos ejemplos
de utilidades prácticas de los decoradores.
"""

def funcion_decoradora(funcion_parametro):
	"""
	Una función decoradora agrega funcionalidad adicional
	a otras funciones, recibiendo como parámetro aquellas funciones
	donde se aplique @funcion_decoradora (el decorador).

	Esto es posible porque en python las funciones pueden recibir otra
	función como parámetro.

	https://www.youtube.com/watch?v=DQXm6bIZgvk
	"""

	def funcion_interior(*args, **kwargs):
		"""
		En la función interior designaremos la funcionalidad adicional.

		En inglés se puede encontrar por wrapper function.

		*args permite recibir un número indeterminado de parámetros
		**kwargs permite recibir un número indeterminado de key-values tipo argumento=valor.

		Tiene sentido hacerlo así porque quizá decoremos funciones que no coincidan en el
		número o tipo de argumentos.
		"""
		print("vamos a realizar un cálculo")

		funcion_parametro(*args) # Llamamos a la función que se recibió como parámetro

		print("Se ha terminado el cálculo")

	return funcion_interior





@funcion_decoradora
def suma(num1, num2):
	print(num1 + num2)

def resta(num1, num2):
	print(num1 - num2)


suma(7,5)
resta(10,20)


"""
------------------------------------------------
			 Ejemplos prácticos
------------------------------------------------

Los decoradores se pueden usar para cronometrar
el tiempo de ejecución de una función y para
hacer un logging de una función de forma sencilla.
"""

# Primer ejemplo, un timer
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

@timer
def run():
	time.sleep(2)

run()

# Segundo ejemplo, un logger

import datetime

def log(func):
	def wrapper(*args, **kwargs):
		with open("log.txt","a") as f:
			f.write("Función llamada con " + " ".join([str(arg) for arg in args]) + " a las " + str(datetime.datetime.now()) + "\n")
		value = func(*args, **kwargs)
		return value
	return wrapper

@log
def run2(a,b,c=9):
	print(a+b+c)

run2(1,3,c=9)