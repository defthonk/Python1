'''''''''''''''
#1 ejemplo
#Dias laborales, tipo texto
lista = ["Lunes", "Martes","Miercoles", "Jueves", "Viernes",40, 5.67,[1,2,3],True]
#Quitar el [2]
print(lista[2])#Si solo quiero elegir solo un dia, cada uno empieza desde 0, entonces lunes es indice 0, lunes es 1, y asi sucesivamente, y si coloco por ejemplo -1, entonces avanzaria desde el viernes, osea de derecha a izquierda, tambien se puede trabjar con sub listas por ejemplo con 0:3, imprime los elementos de la posicion 0,1,2 siempre acaba 1 antes, por ejemplo 1:4 solo indicaria desde el martes, miercoles y jueves, si por ejemplo quiero ir desde el 2 hasta el utimo, seria 2 y daria miercoles, jueves y viernes


#2 ejemplo
lista = [1,2,4,5]
#La funcion len, cuenta todos los elementos de la lista, ejemplo print(len(lista))
#El .append agregaria elemntos al final de la lista, sea texto o cadena por ejemplo, lista.append(6), lista.append("Juanes")}
#Si queremos agregar un valor extra en cualquier posicion y como .append solo agrega al final y queremos agregarlo donde sea, usaremos la funcion .insert(), si nos faltara el 3 usaremos lista.insert(2,3), tambien se puede con tipo texto en cualquier posicion, se usaria lista.insert(2,"hola mundo")
#y si se quiere agregar varios elementos de golpe, se usaria .extend([]), por ejemplo lista.extend([6,7,8])
lista.extend([6,7,8])
print(lista)

#3 ejemplo
#Si queremos sumar 2 listas
lista = [1,2,4,5]
lista2 = [6,7,8]
#Concatenando listas
lista3 = lista+lista2

print(lista3)

#4 ejemplo
lista = [1,2,3,4,5,"Juan"]*2
#Usando el in es para saber si un determinado elemento esta dentro de una lista, es para saber si algun elemento esta en lista, por ejemplo tenemos la lista: lista = [1,2,3,4,5,"Juan"] y buscamos: print(3 in lista) daria true, por que el 3 si esta en lista, si en vez del 3 colcamos 10, daria false, por que 10 no esta en lista
#Y si se quiere saber en que indice esta dicho elemento o posicion, usariamos el .index, si colocamos por ejemplo: print(lista.index("Juan")), nos daria como resultado 5, debido a que "Juan", esta en la posicion o indice 5
#Y si por ejemplo algunos elementos hay repetidos en lista, usaremos .count, por ejemplo si tenemos esta lista: lista = [1,2,3,4,5,"Juan",1,2,3,4,5,"Juan",1], y queremos saber cuantos 1 tenemos repetimos colocamos: print(lista.count(1))
#Y si queremos eliminar algo de una lista, usariamos la funcion: lista.pop() y abajo de eso, el print lista y este nos borrara el ultimo elemento, osea "Juan", y si se quiere eliminar por ejemplo algun numero de otra posicion o texto, indicariamos con el lista.pop(3), con el 3 estariamos diciendo cual indice o posicion de numero o texto eliminariamos
#Y si no se sabe donde esta el indice del numero, usamos .remove, con este elemento no se necesita indicar el indice como el ,pop(), este solo se coloca el numero o el texto y este lo borra de la lista, por ejemplo solo queremos sacar al 2, se usaria asi: lista.remove(2) y abajo print(lista)
#Y si se quiere remover todos los elementos de la lista usamos el .clear
#O hacer que la lista quede voltiada, osea el "Juan" de primero y asi sucesiiavmente se usaria lista.reverse y abajo print(lista)
#Y si quiero que la lista sse copie 2 veces, colocamos al lado de lista *2, por ejemplo lista = [1,2,3,4,5,"Juan"]*2, o *3 y asi sucesivamente
print(lista)
'''''''''''
#5 ejemplo
#Tambien se puede usar otro metodo, osea ordenar elementos de la lista

lista = [5,4,-7,9,0,1,3]   
#Con la funcion .sort y tenemos esta lista, el los acomodara ascendentemente, primero el -7,0,1,3,4,5,9 y abajo print(lista)
#O si se quiere acomodar al contrario, se colocaria lista.sort(reverse=True) y abajo print(lista)
lista.sort(reverse=True)

print(lista)    