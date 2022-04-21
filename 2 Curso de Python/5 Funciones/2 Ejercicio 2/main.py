# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esNumeroPrimo(numero):
	# Calcula si un numero es primo y retorna un Boolean

	for n in range(2, numero):
		if numero % n == 0:
			return False

	return True


entrada = int(input("Introduce un número ENTERO y comprobaremos si es primo: "))
salida = esNumeroPrimo(entrada)

if salida:
	print("El número es primo")
else:
	print("El número NO es primo")