'''''''''
edad = int(input("Digite su edad:"))

if edad>=18:
    print("Es usted mayor de edad")
else:
    print("Usted es menor de edad")

#Condicionales anidados y condiciones combinados
edad = int(input("Digite su edad:"))

if edad>0 and edad<100: #Tambien se puede colocar(if 0<edad<100:)
    print("Edad correcta")
    if edad>=18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

#Ejercicio numero 1 de condicionales(Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son)
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el primer numero: "))

if num1%2==0 and num2%2==0: 
    print("Ambos son pares")
elif num1%2==0 and num2%2!=0: 
    print(f"{num1}es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par") 
else: 
    print("Ambos numeros son impares") 

#Ejercicio 2(Hacer un programa que pida 3 numeros y determine cua es el mayor)
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if num1>=num2 and num1>=num3:
    print(f"El primer numero es mayor {num1}")
elif num2>=num1 and num2>= num3:
    print(f"El segundo numero es mayor {num2}")
elif num3>=num1 and num3>= num2:
    print(f"El tercer numero es mayor {num3}")

#Ejercicio 3(Hacer un programa que pida un caracter e indique si es una vocal o no) (El lower se usa para que lo lea asi sea minuscula o mayuscula)
l = input("Ingrese una Letra : ").lower()
if l.lower()=="a" or l.upper()=="e" or l.upper()=="i" or l.upper()=="o" or l.upper()=="u":
    print("Es una vocal")
else:
    print("Es una consonante")

#Otra forma de hacer el ejercicio 3
letra = input("Digite el caracter: ").lower() #Y upper para transformarlo a mayuscula

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("Es una vocal")
else:
    print("No es una vocal")

#Ejercicio 5
#suma = S, Resta = R, Miltplicacion = M, Division = D
num1 = float(input("Digite el primer numero: "))
num2 = float(input("Digite el segundo numero: "))

operacion = input("Digite la operacion: ").upper()

if operacion == 'S':
    suma = num1+num2
    print(f"\nLa suma es: {suma}")
elif operacion == 'R':
    resta = num1-num2
    print(f"\nLa resta es: {resta}")
elif operacion == 'M' or operacion == 'P':
    mult = num1*num2
    print(f"\nLa multiplicacion es: {mult}")
elif operacion == 'D':
    div = num1/num2
    print(f"\nLa division es: {div:.2f}")
else:
    print("\nSe equivoco de operacion")
'''''''''
#Ejercicio 5
saldo = 1000
print("\t.:MENU:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Digite opcion de menu: "))

print()

if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar a la cuenta -> "))
    saldo += extra 
    print(f"Dinero en la ceunta es de: {saldo}")
    
elif opcion == 2: 
    retirar = float(input("Cuanto dinero desea retirar a la cuenta -> "))
    if retirar>saldo: 
        print("No tiene suficiente fondos")
    else: 
        saldo -= retirar 
        print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Dinero en la cuenta:  {saldo}")
elif opcion == 4:
    print("Gracias por utilizar su cajero automatico")
else: print("Error, se equivoco de opcion de menu")        
    
        