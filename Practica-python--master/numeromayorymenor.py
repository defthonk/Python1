x = int(input("¿Cuál es el primer número?")) 
y = int(input("¿Cuál es el segundo número?"))
z = int(input("¿Cuál es el segundo número?"))
if x>y and x > z:
  print(f"El número mayor es {x}")
elif y > x and y > z:
  print(f"El numero mayor es {y}")
elif z > x and z > y:
    print(f"El numero mayor es {z}")
else:
  print('Es el mismo número.')