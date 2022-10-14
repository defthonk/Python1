#En lo anterior hemos definido atributos de instancia, ya que estos son atributos que pertenecen a cada perro en concreto
#Y respecto al atributo de clase, que sera para todos los perro, ejemplo: especie de los perros es algo comun para todos los objetos perro

class Perro:
    #Atributo de clase 
    especie = 'mamifero'
    
    #El metodo __init__ es llamado al crear eñ pbjeto 
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
        
        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza

#Ya que es un atributo de clase, no es necesario crear un objeto para acceder al atributo, Asi que se puede hacer lo siguiente
print(Perro.especie)

#Se puede acceder tambien al atributo de clase desde el objeto 
mi_perro = Perro("Ozzy", "Chow chow")
mi_perro.especie

#Todos los objetos que se creeen de la clase perro compartiran ese atributo de clase, ya que pertenecen a la misma 

