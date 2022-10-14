"""""""""
#Es un trozo de codigo que se va a repetir un numero indeterminado de veces, osea es algo que se repite y se repite

import math 

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))
    
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")
"""""
#Ejercicio 2, para mostrar un hola mundo 10 veces

i = 0

while i<10:
    print("Hola mundo")
    i += 1

    
    