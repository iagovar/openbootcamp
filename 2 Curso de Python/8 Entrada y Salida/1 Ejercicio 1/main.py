"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""

def main():
	f = open("miArchivo.txt", "a")

	for i in range(10):
		f.write(f"{i}\n")

	f.close()

if __name__ == '__main__':
	main()