#Cuando usamos __init__ ya que estamos definiendo un metodo, pero voy a ahcer un metodo que de alguna funcionalidad interesante a nuestra clase
#Vamos a codificar 2 metodos (ladrar y caminar), el primero no recibira ningun parametro y el segundo recibira el numero de pasos que queremos andar.
#como hemos hecho con self hace referencia a la instancia de la clase, se puede definir un metodo con def y el nombre, ye entre() los parametros de entrada que recibe, donde siempre tendra que estar self el primero

class Perro:
    #Atributo de clase
    especie = 'mamifero'
    
    #El metodo __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro{nombre}, {raza}")
        
        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza
        
    def ladra(self):
        print("Guau")
        
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")
    
#Por lo tanto si se crea un objeto mi_perro, podremos hacer uso de sus metodos llamandolos con "." y el nombre del metodo. Como si de una funcion se trata, estos pueden recibir y devolver argumentos
mi_perro = Perro("Ozzy", "Chow chow")
mi_perro.ladra()
mi_perro.camina(10)

#Creando perro Ozzy, Chow chow 
#Guau
#Camina 10 pasos