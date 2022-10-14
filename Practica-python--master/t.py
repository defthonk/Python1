class Perro:
    #Atributo de clase 
    especie = 'mamifero'
    
    #El metodo __init__ es llamado al crear eñ pbjeto 
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
        
        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza
        
print(Perro.especie)

#Se puede acceder tambien al atributo de clase desde el objeto 
mi_perro = Perro("Ozzy", "Chow chow")
mi_perro.especie

print("me gusta la cuca humeda")
