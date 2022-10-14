'''''''''''
#Ejercicio 1(Escribir la sgt expresion en forma de expresion algoritmica)
a = float(input("a ->"))
b = float(input("b ->"))
c = float(input("c ->"))
resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultadp es: {resultado}")

#Ejercicio 2
a = float(input("a ->"))
b = float(input("b ->"))

r = ((3+5*8))<3 and ((-6/3*4)+2<2) or (a>b)
print(f"El resultado es: {r}")

#Ejecicio 3(Hacer un programa para intercambiar el valor de 2 variables)
a = 10
b = 5
a,b = b,a
print(a, b)

#Otra forma de hacer el ejercico 3
a = input("a ->")
b = input("b ->")
a,b = b,a
print(f"El resultado de a: {a}")
print(f"El resultado de b: {b}")

#Ejercicio 4(Hacer un programa para ingresar el radio de un circulo y se reparte su area y la longitud de la circunferencia)
#Importar el modulo math, donde esta pi
import math
Radio = float(input("radio ->"))
area = math.pi * Radio**2
longitud = 2 * math.pi * Radio

print(f"El area es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")
'''''
#Ejercicio 5(Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente su compra)
precio = float(input("Digite el precio: "))

descuento = precio * 0.15
precio_final = precio - descuento

print(f"El precion final a pagar es de ${precio_final:.2f}")
