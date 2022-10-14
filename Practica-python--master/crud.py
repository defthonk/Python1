class Electrodomesticos:
    def __init__(self, id, nombre,marca):
        self.id = id
        self.nombre = nombre 
        self.marca = marca
    def __str__(self):
        return f"identificacion= {self.id} Nombre: {self.nombre} Marca: {self.marca}"
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getMarca(self):
        return self.marca
    def modId(self, Rid):
        self.id = Rid
    def modNombre(self, Rnombre):
        self.nombre = Rnombre
    def modMarca(self, Rmarca):
        self.marca = Rmarca

def agregar():
    id = input("ingrese id: ")
    nombre = input("ingrese nombre: ")
    marca = input("ingrese marca: ")
    electrodomesticoNuevo = Electrodomesticos(id, nombre, marca)
    listaElectrodomesticos.append(electrodomesticoNuevo)

def listar():
    print("    ")
    print("----listar----")
    for elect in range(0, len(listaElectrodomesticos)):
        print(f"{elect + 1} - {listaElectrodomesticos[elect]}")


def borrar():
    listar()
    elect = int(input("Ingrese el numero de Electrodomesticos que desea borrar"))
    print(f"Seguro profe que quiere eliminar ese electrodomesrico? {listaElectrodomesticos[elect -1].getId} {listaElectrodomesticos[elect -1].getNombre}")
    respuesta = input("S- borrar - N - No borrar")
    if (respuesta == "S"):
        listaElectrodomesticos.remove(listaElectrodomesticos[elect -1])

def modificar():
    listar()
    elect = int(input("Ingrese el numero de Electrodomesticos que desea modificar"))
    id = input("ingrese nuevo id: ")
    listaElectrodomesticos[elect -1].modId(id)
    nombre = input("ingrese nuevo nombre: ")
    listaElectrodomesticos[elect -1].modNombre(nombre)
    marca = input("ingrese nuevo marca: ")
    listaElectrodomesticos[elect -1].modMarca(marca)

listaElectrodomesticos = []
Electrodomestico1 = Electrodomesticos('12','Celular', 'Xiaomi')
Electrodomestico2 = Electrodomesticos('43','Pc', 'Acer')
listaElectrodomesticos.append(Electrodomestico1)
listaElectrodomesticos.append(Electrodomestico2)
opcion = ''
while(opcion != 'x'):
    print("----Inicio----")
    print("1. agregar Electrodomestico")
    print("2. Modificar Electrodomestico")
    print("3. Listar Electrodomestico")
    print("4. Eliminar electrodometico")
    print("5. Salir de la aplicación")
    opcion = input("Ingrese la opcion deseada: ")
    if(opcion == '5'):
        print("saliendo...")
    elif(opcion == '1'):
        agregar()
    elif(opcion == '3'):
        listar()
    elif(opcion == '4'):
        borrar()
    elif(opcion == '2'):
        modificar()
    else :
        print("opcion incorrecta")