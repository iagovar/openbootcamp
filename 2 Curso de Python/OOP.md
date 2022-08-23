# Seis principios de la POO

- Herencia: ``class claseHija(clasePadre):`` hereda todos los métodos y atributos de ``clasePadre``, pero además, puede re-escribirlos o definir unos nuevos.

	También puede heredarse de varias clases, como ``class claseHija(clasePadre1, clasePadre2)``.

- Polimorfismo: Objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos.

	### Ejemplo de polimorfismo
	````
	class Coche():
		def mostrarRuedas(self):
			print("Un coche tiene cuatro ruedas")

	class Moto():
		def mostrarRuedas(self):
			print("Una moto tiene cuatro ruedas")

	def cuantasRuedasTiene(vehiculo):
		vehiculo.mostrarRuedas()

	# Ejecutando el código

	miVehiculo = Coche()

	cuantasRuedasTiene(miVehiculo)

	# Salida de la consola

	Un coche tiene cuatro ruedas
	````




- Encapsulamiento: La práctica de esconder o restringir el acceso de los métodos o variables de una clase desde el exterior (fuera de su *scope*). En Python se hace por convención con ``_variable`` o con ``__variable`` vía *name mangling* (ver variables privadas).

# Convenciones POO en Python

- ``_variable``: Las variables escritas con un guión delante **no deberían modificarse desde fuera de la clase**. Deberíamos usar, o definir, un método dentro de la clase para consultar o modificar su estado. Esto se puede hacer con los típicos métodos *get* y *set* que ya vimos en Java.

	Existe un método para emular la privacidad de un método o atributo llamado *name mangling*. Al escribir dos guiones en lugar de uno, como en ``__atributo`` python cambiará automáticamente el nombre por ``_nombreDeClase_atributo``, de modo que al acceder por ``__atributo`` mostrará un error, aunque no sucederá al acceder por ``_nombreDeClase_atributo``.

# Clases estáticas VS Clases dinámicas

Las clases dinámicas se instancian, las clases estáticas no.

Esto implica que las clases estáticas siempre ocupan el mismo lugar en la memoria, mientras que en las clases dinámicas ha de reservarse un nuevo espacio en la memoria para cada instancia.

## Ejemplo de una clase dinámica:

````
class Perro:
	# Atributos de clase
	especie = "mamífero"

	# Constructor
	def __init__(self, nombre, raza):
		print(f"Creando perro {nombre}, {raza}")

		# Atributos de instancia
		self.nombre = nombre
		self.raza = raza

````
Las clases dinámicas siempre tienen ``self`` como parámetro (en python) ya que al instanciarse, es necesario referenciar el espacio de memoria de la instancia.

Así pues, sabemos que es una clase dinámica porque observamos que los métodos ``__init__`` y varios atributos usan ``self`` como parámetro.

Observamos también que hay un atributo que no usa ``self``. Se heredará dentro de la instancia y se accederá a él mediante ``instancia.atributo``.

También sería posible acceder desde ``clase.atributo`` pero **no deberías hacerlo**, porque si la modificas afectarás a todas las instancias que se creen a partir de ese momento, que heredarán el nuevo valor. Es bastante probable que esto no te interesa, de lo contrario habrías incluído el parámetro ``mamífero`` en el constructor de la clases ¿no es así?.

## Ejemplo de clase Estática:

````
class Estatica:
	numero = 1

	def incrementa():
		Estatica.numero += 1
````

Si llamamos a la función ``incrementa()`` las variables internas se manipularán, pero siempre en el mismo espacio de memoria.

Un ejemplo de clases estáticas son los modelos de datos en Django, que se especifican con clases estáticas. También se pueden encontrar para especificar opciones, para llamadas tipo ``opciones.encendido``, etc.

# Clases abstractas

Las clases abstractas permiten añadir mayor definición y seguridad a la herencia, el evitar que se puedan instanciar y obligar a sobreescribir los métodos en las clases hijas, algo que la herencia, por sí misma, no obliga.

De: https://www.youtube.com/watch?v=Ji8uoRvi17s

Una clase abstracta:

- No las vamos a instanciar nunca *directamente*.
- Contiene por lo menos un método abstracto con el decorador @abstractmethod.
- Las vamos a usar de base para subclases más específicas.

Los métodos abstractos:

- Debemos sobreescribirlos en cada una de las subclases.

Un ejemplo de clases abstractas:

````

from abc import ABC, abstractmethod # Obligatorio para el uso de clases abstractas

class Personaje(ABC):
	
	@abstractmethod # Este decorador indica que es un método abstracto
	def __init__(self, nombre):
		self.nombre = nombre
		self.nivel = 0
		self.inventario = []
		self.vida = 100

	@abstractmethod
	def atacar(self. objetivo):
		pass

	@abstractmethod
	def getstatus(self):
		print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")

	def subirDeNivel(self):
		# Este método no lo haremos abstracto, porque es
		# muy sencillo, y no pretendemos extenderlo.
		self.nivel += 1

	def verInventario(self):
		for objeto in self.inventario:
			print(objeto)

class Mago(Personaje):
	# Clase heredando de nuestra clase abstracta padre.
	# Extenderemos los métodos abstractos en ella.

	def __init__(self, nombre):
		super().__init__(nombre) # Equivale a Personaje.__init__(self, nombre)
		self.vida = 120
		self.inteligencia = 95
		self.inventario = ["Poción", "Libro de conjuros"]

	def getStatus(self):
		print(f"{self.nombre} es de la clase Mago.")
		super().getStatus()

	def atacar(self, objetivo):
		objetivo.vida -= self.inteligencia*0.6
		print(f"La vida actual del objetivo es {objetivo.vida}")

class Guerrero(Personaje):
	def __init__(self, nombre):
		super().__init__(self, nombre)
		self.vida = 200
		self.fuerza = 75
		self.inventario = ["Poción", "Escudo", "Espada"]

	def getStatus(self):
		print(f"{self.nombre} es de la clase Guerrero.")
		super().getStatus()

	def atacar(self, objetivo):
		objetivo.vida -= self.fuerza*0.8
		print(f"La vida actual del objetivo es {objetivo.vida}")
````

# Composición

Una clase que contiene instancias de otras clases, es una clase compuesta. Se crea una jerarquía de objetos sin utilizar herencia.

Hay quien dice que la composición se hace más legible que la herencia cuanto mayor código haya en un proyecto.

Un ejemplo de composición:

````
# Definición de clases y su jerarquía
class Motor:
	tipo = "Diesel"

class Ventanas:
	cantidad = 5

	def cambiarCantidad(self, valor):
		self.cantidad = valor

class Ruedas:
	cantidad = 4

class Carroceria:
	ventanas = Ventanas()
	ruedas = Ruedas()

class Coche:
	motor = Motor()
	carroceria = Carroceria()

# Instanciamos para comprobar cómo funciona

miCoche = Coche()

# Probamos a imprimir la jerarquía

print("El motor es de tipo ", miCoche.motor.tipo)
print("Ventanas: ", miCoche.carroceria.ventanas.cantidad)

# Output

El motor es de tipo  Diesel
Ventanas:  5
````

**Observaciones**

1. La clase ``Coche`` tiene que ir después de ``Carroceria`` ya que si llamamos a una clase que el intérprete de python aún no ha leído, se producirá un error.

2. La jerarquía, en composición, se establece en función de las llamadas a otras clases, no a parámetros pasados como argumentos de una clase, que sería el caso de la herencia.

3. Para obtener un valor, se recorre la jerarquía *de los atributos* de cada clase. Por eso vemos ``miCoche.carroceria.ventanas.cantidad``.

