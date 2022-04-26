"""
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def esAprobado(self):
        notaAprobado = 5
        aprobado = "Está aprobado" if self.nota >= notaAprobado else "Está suspenso"

        return aprobado

    def mostrarDatos(self):
        print(f"Se ha introducido el alumno {self.nombre} con la nota {self.nota}")


# Inicializamos el alumno
miAlumno = Alumno("Fulanito", 6.75)
miAlumno.mostrarDatos()
print(miAlumno.esAprobado())



