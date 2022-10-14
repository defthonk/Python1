#Las colas son una estructura de datos tipo fifo, osea primero en entrar, primero en salir

cola = ["Maria", "Juan", "Jose", "Mario"]
#Agregamos elementos al final de la cola
cola.append("Karla")
cola.append("Flor")

print(cola)

#Sacando elementos por el principio de la cola
#Tenemos que indicar con el indice para que no me saque el ultimo de la cola, con el .pop(0), indicando que me saque primero a la que llego
n = cola.pop(0)
print(f"Atendiendo a {n}")
print(cola)

n = cola.pop(0)
print(f"Atendiendo a {n}")
print(cola)