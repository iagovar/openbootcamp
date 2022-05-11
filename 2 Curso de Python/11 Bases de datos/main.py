"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import os
import sqlite3

def main():
	"""
	Ejecuta el menú princpal
	"""
	print("""
	Por favor, selecciona una de las siguientes operaciones:\n
	0 -> Inserción de alumno\n
	1 -> Búsqueda de alumno\n
	2 -> Finalizar el programa\n
	""")
	userChoice = input("Escribe el código de la operación que deseas realizar: ")

	if userChoice == "2":
		clear()
		quit()
	elif userChoice == "0":
		insercion()
	elif userChoice == "1":
		busqueda()
	else:
		clear()
		print("Algo hiciste mal, vuelve a intentarlo...")
		main()

def insercion():
	"""
	Ejecuta las operaciones de inserción.

	SQLite ya asigna automáticamente una primary key en desuso, y desaconseja el uso de autoincrement
	https://sqlite.org/autoinc.html

	No usamos autoincrement, ya que por el momento si se borra un usuario y se reusa la clave, no
	parece que pueda suponer un problema.
	"""

	clear()
	print("Por favor, introduce los siguientes datos del alumno. Los campos no pueden quedar vacíos.\n")

	nombreAlumno, apellidosAlumno = "", ""

	while nombreAlumno == "" or apellidosAlumno == "":

		nombreAlumno 	= input("Nombre del alumno: ")
		apellidosAlumno = input("Apellidos del alumno: ")

		if nombreAlumno == "" or apellidosAlumno == "":
			clear()
			print("Dejaste algún campo en blanco, introdúcelos de nuevo!\n")

	# Abrimos la conexión con SQLite y generamos el insert

	alumnoParaInsertar = f"INSERT INTO alumnos (nombre, apellidos) VALUES('{nombreAlumno}', '{apellidosAlumno}')"

	conn = sqlite3.connect("alumnosbd.sqlite")
	cursor = conn.execute(alumnoParaInsertar)
	conn.commit()
	conn.close()

	print("\nInsertado alumno en la BD.")
	print("0 -> Insertar otro alumno | 1 -> Volver al menú principal")

	userChoice = input("\nEscoge una opcion: ")

	if userChoice == "0":
		clear()
		insercion()
	elif userChoice == "1":
		clear()
		main()
	else:
		clear()
		print('Algo hiciste mal!')
		main()

def busqueda():
	"""
	Genera una consulta diferente en función de qué campos se rellenan y devuelve
	el resultado.
	"""

	clear()
	print("Busca alumnos por nombre y apellidos. Uno de los dos campos puede quedar vacío.\n")

	nombreAlumno	= input("Nombre del alumno: ")
	apellidosAlumno = input("Apellidos del alumno: ")

	if nombreAlumno != "" and apellidosAlumno != "":
		print("\nSe ejecutará la consulta atendiendo a los dos criterios.")

		consultaDeAlumno = f"SELECT idAlumno, nombre, apellidos FROM alumnos WHERE nombre LIKE '{nombreAlumno}' AND apellidos LIKE '{apellidosAlumno}'"

	elif nombreAlumno != "" and apellidosAlumno == "":
		print("\nSe ejecutará la consulta atendiendo al nombre.")

		consultaDeAlumno = f"SELECT idAlumno, nombre, apellidos FROM alumnos WHERE nombre LIKE '{nombreAlumno}'"

	elif nombreAlumno == "" and apellidosAlumno != "":
		print("\nSe ejecutará la consulta atendiendo al apellido.")

		consultaDeAlumno = f"SELECT idAlumno, nombre, apellidos FROM alumnos WHERE apellidos LIKE '{apellidosAlumno}'"

	# Abrimos la conexión sqlite y ejecutamos la consulta

	conn = sqlite3.connect("alumnosbd.sqlite")
	cursor = conn.execute(consultaDeAlumno)

	print("\nEstas son las coincidencias encontradas:\n")

	for row in cursor:
	   print ("Identificador = ", row[0])
	   print ("Nombre = ", row[1])
	   print ("Apellidos = ", row[2], "\n")

	conn.close()

	print ("No hay más datos devueltos\n")
	print("0 -> Buscar otro alumno | 1 -> Volver al menú principal")

	userChoice = input("\nEscoge una opcion: ")

	if userChoice == "0":
		clear()
		busqueda()
	elif userChoice == "1":
		clear()
		main()
	else:
		clear()
		print('Algo hiciste mal!')
		main()


def clear():
	"""
	Limpiar pantalla de la consola
	https://gist.github.com/Didweb/c2ea77b7ff6a3d73c79a4ff1a5741775
	"""
	if os.name == "posix":
		os.system ("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system ("cls")


if __name__ == '__main__':
	main()





