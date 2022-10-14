#No se pueden trabajar directamente, para trabajar con ella, pero se puede simular para trabajar con ella, usando listas
#Se conocen como estrctura de datos tipo lifo, osea ultimo en entrar y ultima en salir

pila = [1,2,3]
#Agregando elementos por el final de la pila, para agregar elementos a la lista, usariamos el .append()
pila.append(4)
pila.append(5)

print(pila)
#Tambien se pueden sacar elementos de la pila y para sacarlos usariamos el .pop()
n = pila.pop()
print(f"sacando el elemento {n}")
n = pila.pop()
print(f"sacando el elemento {n}")

print(pila)


