# Ruler en 42 para postear sin line-break

class Coche:
    
    """
    Los atributos y métodos privados en
    Python convierten:

    __atributo  en  _Clase__atributo
    __método    en  _Clase__método

    Así que no son realmente privados,
    simplemente se les cambia el nombre
    para no poder acceder con su nombre
    original, pero lo podrías hacer
    escibiendo _Clase antes.

    Tampoco hace falta declararlos antes
    del constructor como en JS.
    """




    def __init__(self, marca, modelo, cc):
        # Declaramos el constructor
        self.marca = marca
        self.modelo = modelo
        self.cc = cc
        
        # Atributos privados
        self.__robado = False
        self.__encendido = False
        
        
    def girarContacto(self):
        # Un método público cualquiera
        if self.__getEncendido() == False:
            self.__setEncendido(True)
        else:
            self.__setEncendido(True)
            
        print("Cambiando motor a " + str(self.__getEncendido()))
        return "Cambio del estado del motor con éxito"





    # Métodos privados
    def __getEncendido(self):
        return self.__encendido
    
    def __setEncendido(self, boolean):
        self.__encendido = boolean




# Instanciación de clase
miCoche = Coche("Fiat", "Panda", 1500)



# Probando método público
    ## Usando el return
print(miCoche.girarContacto())

    ## Sin usar el return
miCoche.girarContacto() 



# Probando atributos y métodos privados

    ## Probamos primero los métodos
    
try:
    miCoche.__getEncendido()
    # AttributeError: 'Coche' object has
    # no attribute '__getEncendido'

    print("Se ejecuto el try en métodos")
except:
    # Aunque llamar con __método no
    # funciona, llamar con
    # _Clase__método sí.
    miCoche._Coche__getEncendido()
    print(
        "Se ejecutó el except en métodos"
        )







    ## Probamos los atributos

try:
    print(miCoche.__encendido)
    #AttributeError: 'Coche' object has
    # no attribute '__encendido'
    print("Se ejecutó el try")
except:
    print(miCoche._Coche__encendido)
    print("Se ejecutó el except")
    






# Probamos la herencia
# Sobre el uso de la keyword "super":
# https://www.w3schools.com/python/ref_func_super.asp

class Todoterreno(Coche):
    def __init__(self, marca, modelo, cc, traccion):
        super().__init__(marca, modelo, cc)
        self.traccion = traccion



    ## Probando polimorfismo

    def girarContacto(self):
        super().girarContacto()
        print("Esta es una clase extendida y modificada")







    def __getEncendido(self):
        # En python si es posible 
        #extender un método privado
        print("Obteniendo el estado del motor")
        super().__getEncendido()




# Instanciamos una nueva clase
nissanPatrol = Todoterreno("Nissan", "Patrol", 3000, "4x4")

# Imprimimos el objeto para observar
# los cambios
print(nissanPatrol.__dict__)

# Probamos método extendido
nissanPatrol.girarContacto()
nissanPatrol.girarContacto()