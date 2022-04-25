"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""

class Vehiculo:
	color = None
	ruedas = None
	puertas = None
	"""
	def __init__(self, color, ruedas, puertas):
		# __init__ es una función reservada que actúa de constructor en python
		self.color = color
		self.ruedas = ruedas
		self.puertas = puertas
	"""

# La herencia en python se ejecuta con clase(padre) y todos los métodos y propiedades
# son públicos, aunque se puede usar la convención _método o __propiedad para indicarlo
# al lector, pero python por sí mismo no lo va a respetar.
class Coche(Vehiculo):
	velocidad = None
	cilindrada = None
	def __init__(self, **kwargs):
		# type(kwargs) es diccionario
		for key, value in kwargs.items():
			print(f"{key} = {value}")

miCoche = Coche(key="valor", key2="valor2")

print(miCoche)
print(dir(miCoche))