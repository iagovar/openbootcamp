"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""

from tkinter import *
from tkinter import ttk

# Funciones de cambio de estado
def cambiarValor(evento):
	seleccion = evento.widget.curselection()
	indice = seleccion[0]
	valor = evento.widget.get(indice)
	#print(valor)
	labelSeleccion.config(text="Selecionaste " + str(valor))

# Dibujamos la ventana principal
ventanaPrincipal = Tk()
ventanaPrincipal.title("Ventana Principal")
ventanaPrincipal.geometry("400x250+100+100")

# Dibujamos un content frame

contenidoPrincipal = ttk.Frame(ventanaPrincipal, padding=10)
contenidoPrincipal.grid()

# Dibujamos Listbox
misOpciones = ["primera", "segunda", "tercera", "cuarta"]
misOpcionesVar = StringVar(value=misOpciones)

elegido = StringVar()

miLista = Listbox(contenidoPrincipal, listvariable=misOpcionesVar)
miLista.bind("<<ListboxSelect>>", cambiarValor)
miLista.grid()

# Label mostrando la selección
labelSeleccion = ttk.Label(contenidoPrincipal, text="Selecciona una opción")
labelSeleccion.grid(sticky="w")

# Generamos el loop infinito para que se mantenga abierta
ventanaPrincipal.mainloop()