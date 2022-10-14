#Programacion orientada a objetos
#Ejemplo del perro, las clases, nos ayuda a organizar codigo de una manera que se asemeja mucho a la vida real, usando las clases, la cual nos permire agrupar un  conjunto de variables  y funciones
#El perro tiene doferentes caracteristicas, las  cuales son edad, nombre o la raza, las caractiristicas se les llama atributos 
#La clases tienen funcionalidades, en el caso del perro pueden ser andar o ladrar y estas funcionalidades se llaman metodos
#Y hay diferentes tipos de perros, osea yo tengo uno que se llama ozzy o el del vecino que se llama kira, y los diferentes tipos de perros se llaman objetos.
#La programación orientada a objetos está basada en 6 principios o pilares básicos: Herencia,Cohesión,Abstracción,Polimorfismo,Acoplamiento,Encapsulamiento

#Parte programacion 

#Creando una clase vacia 
''''
class Perro:
    pass
'''
#Nótese el uso del pass que no hace realmente nada, pero daría un error si después de los : no tenemos contenido.

#Ahora creada la clase, se puede crear un objeto, se puede hacer como si definieramos una variable

#Creamos un objeto de la clase perro
''''
mi_perro = Perro()
'''''
#Definiendo atributos, hay 2 tipos de atributos:
#Atributo de instancia: Pertenecen a la instancia de la clase o al objeto, son atributos particulaes de cada instancia, en nuestro caso de cada perro
#Atributo de clase: Se trata de atributos que pertenecen a la clase, por  lo tanto seran comunes para toso los objetos

#En este caso usaremos atributos de instancia para nuestro perro, el nombre y la raza, y para hacer esto creamos un metodo __init__  que sera llamado automaticamente cuando creemos un objeto, se trata del constructor

class Perro:
    #El metodo __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}.{raza}")
    
        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza
    
#Una vez definida el mettodo init con 2 parametros de entrada, podemos crear el objeto pasando el valor de los atributos, usando type() se puede ver como efectivamente el objeto es de la clase perro 
mi_perro = Perro("Ozzy", "Chow chow")
print(type(mi_perro))
#Creando perro ozzy, chow chow
#<class '__main__Perro'>

#El self pasa como parametro de entrada del metodo, es una variable que representa la instancia de la clase y siempre esta ahi 
#Las cosas que tiene __ se conoce como un construcor 
#Se puede acceder a los atributos usando el objeto .

print(mi_perro.nombre)
print(mi_perro.raza)
