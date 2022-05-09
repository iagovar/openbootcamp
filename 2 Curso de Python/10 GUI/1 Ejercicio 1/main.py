"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.

Documentación TK con los conceptos básicos: https://tkdocs.com/tutorial/concepts.html
"""
from tkinter import *
from tkinter import ttk

# Globales
# (Vacío por el momento)

# Funciones de cambio de estado
def cambiarValor():
	labelSeleccion.config(text="Selecionaste la " + str(elegido.get()))

def borrarSeleccion():
	labelSeleccion.config(text="Selección borrada, por favor selecciona de nuevo")
	elegido.set("")


# Dibujamos la ventana principal
ventanaPrincipal = Tk()
ventanaPrincipal.title("Ventana Principal")
ventanaPrincipal.geometry("400x200+100+100")


# Dibujamos un content frame o widget con contenido
# (usan estos nombres indistintamente en la documentación)

contenidoPrincipal = ttk.Frame(ventanaPrincipal, padding=10)
contenidoPrincipal.grid()


# Radio Buttons con contenido
opcionesDeRadio = ["Opción 1", "Opción 2", "Opción 3"]
botonesDeRadio = []

ttk.Label(contenidoPrincipal, text="Lista de Radio Buttons").grid(column=0, row=0, sticky="w")

elegido = StringVar()

for i in range(len(opcionesDeRadio)):
	ttk.Radiobutton(
		contenidoPrincipal,
		text=opcionesDeRadio[i],
		value=opcionesDeRadio[i],
		variable=elegido, #Asigna un valor cada vez que se hace click, comparido por todos los botones
		command=cambiarValor
		).grid(column=0, row=i+1, pady=2, sticky="w")

	# Muestra el RadioButton Seleccionado
labelSeleccion = ttk.Label(contenidoPrincipal, text="Selecciona una opción")
labelSeleccion.grid(column=0, row=5, sticky="w")

	# Borra el valor de elegido
botonDeBorrado = ttk.Button(contenidoPrincipal, text="Borrar la Selección", command=borrarSeleccion)
botonDeBorrado.grid(column=0, row=6, sticky="w")

# Generamos el loop infinito para que se mantenga abierta
ventanaPrincipal.mainloop()