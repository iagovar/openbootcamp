"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""

import pickle # Una librería para serializar/deserializar datos y poder escribirlos/leerlos en disco

class Vehiculo:
	"""docstring for Vehiculo"""
	velocidad = None
	color = None

	def __init__(self, velocidad, color):
		self.velocidad = velocidad
		self.color = color

def main():
	miObjeto = Vehiculo(120, "Rojo")

	print(f"El objeto inicializado tiene las propiedades de Velocidad {miObjeto.velocidad} y Colo {miObjeto.color}")

	bf = open("objeto.binario", "wb")
	pickle.dump(miObjeto, bf)
	bf.close()



	nf = open("objeto.binario", "rb")

	objetoCargado = pickle.load(nf)

	print(f"El nuevo objeto cargado tiene las propiedades Velocidad {objetoCargado.velocidad} y Color {objetoCargado.color}")

	nf.close()




if __name__ == '__main__':
	main()
