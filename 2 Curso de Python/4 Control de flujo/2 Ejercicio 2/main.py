print("El script muestra los números inpares desde un número inicial a uno final, ambos inclusive\n")

numInicial = int(input("Introduce el número incial: "))
numFinal = int(input("Introduce el número final: "))

for i in range(numInicial, numFinal+1):
	if i % 2 != 0:
		print(i)