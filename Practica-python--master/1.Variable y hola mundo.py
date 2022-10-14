'''''''''''''''''
#Definir variables, una variable es cualquier cosa le asignamos algo ejemplo "Texto = Repaso" y con el print imprimimos en pantalla lo que esta dentro del texto
#1
Texto = "repaso"
Nombre = "Juanes"
Year = 2022

print(Texto)
print(Nombre)
print(Year)


#Hola mundo, como imprimir palabras en la terminal, esto es otro (\n es un salto de linea)
#2
print("hola mundo?\nme llamo s")


#Con la funcion type podemos mirar si es de valor entero(int) o con decimales(float)
#3
numero = 10.56

print(numero)
print(type(numero))

#Creando 2 variables (num1 y num2), y otra variable externa que encierra el resultado de num1 y num2, y python respeta las leyes de la matetica, primero el parentesis y despues lo otro
#en el print estoy concatenando lo que quiero que aparezca en pantalla con el resultado, usando (, resultado)
#4
num1 = 10
num2 = 6.7
resultado = (num1+num2) * 10 / 6

print("El resultado es: ", resultado) 
'''''''''
#Tipado dinamico(podemos agregar 2 tipos de variables y python va a respetar cada variable)
valor = 10

print(valor)

valor = "Juan"

print(valor)

