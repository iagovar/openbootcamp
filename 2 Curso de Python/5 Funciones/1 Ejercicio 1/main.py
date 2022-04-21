# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

def AreaTriangulo(base, altura):
	return (base * altura) / 2

def areaCirculo(radio):
	pi = 3.141592653589793
	return pi * (radio**2)


pruebaTrianulo = AreaTriangulo(5,8)
pruebaCirculo = areaCirculo(10)

print(f"Nuestra prueba nos indica que el área del triángulo es {pruebaTrianulo} u² y que el área del círculo es {pruebaCirculo} u²")