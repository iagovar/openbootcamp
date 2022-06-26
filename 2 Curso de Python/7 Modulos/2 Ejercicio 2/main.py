"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""

import datetime

def main():
	ahora 			= datetime.datetime.now()
	horaActual		= ahora.hour
	minutoActual	= ahora.minute
	horaDeSalida 	= 19
	minutoDeSalida	= 60 # 60 mins de la hora anterior, equivalentes a 00 de la actual

	if horaActual >= horaDeSalida:

		print("Hora de largarse, muchacho")

	else:
		quedanHoras = horaDeSalida - horaActual
		quedanMinutos = abs(minutoDeSalida - minutoActual)

		print(f"Te quedan {quedanHoras} horas y {quedanMinutos} minutos pringando. Ánimo.")



if __name__ == "__main__":
	main()