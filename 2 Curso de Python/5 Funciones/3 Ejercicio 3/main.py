# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(ano):
	# Espera un ineger y devuelve un boolean

	cumpleCondiciones = False

	if ano % 4 == 0: cumpleCondiciones = True
	if ano % 100 == 0:
		cumpleCondiciones = False
		if ano % 400 == 0: cumpleCondiciones = True

	return cumpleCondiciones


while True:
	entrada = int(input("Escribe un año y comprobaremos si es bisiesto: "))
	salida = esBisiesto(entrada)

	if salida:
		print("El año es bisiesto")
	else:
		print("El año NO es bisiesto")
