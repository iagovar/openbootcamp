import math

pasos = 2
entrada = "A"
matriz = [
["A","B","C"],
["D","E","F"],
["G","H","I"]
]

longitud = len(matriz) * len(matriz[0])
alto = len(matriz)
ancho = len(matriz[0])
entradaI = 0
for i in range(alto):
	try:
		entrada = matriz[i].index("A")
	except:
		pass
soluciones = []

"""
V de n/m = m! / (m-n)!

m -> longitud
n -> pasos
"""


variaciones = math.factorial(longitud) / math.factorial((longitud-pasos))


print(variaciones)			

