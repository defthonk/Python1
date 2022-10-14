#Las tuplas son otro tipo de coleccion, que parecidos a las listas, pero las tuplas son listas inmutables, osea no se pueden modificar ni nada 
#Listas con corchete y tupla con ()
#los valores que ya se meten en la tupla ya se quedaria asi hasta el final, no se puede agregar, ni eliminar, ni modoficar nada
#Que puedo hacer con una tupla? puedo buscar, por ejemplo, tenemos en la lista el 4 de primero, osea estaria en el indice o posicion 0, entonces para buscaria seria: print(tupla[0]), tambien para buscar puedo uasr los indices negativos, para buscar 6.78, colcoaria print(tupla[-3])
#Tamnbien puedo usar el slaising, osea para imprimir desde un numero en adelante, osea print(tuola[1:]), me mostraia todos los elemntos de la tupla excepto el 4 principal
#Tambien puedo buscar. todo tipo de busqueda, osea por ejemplo quiero buscar si hay algun 4, puedo colocar: print(4 in tupla) y me va a arrojar un true, debido que esto ess cierto por que si hay un 4
#Ademas se puede hacer la busquerda con el metodo .index, osea print(tupla.index("Hola")) y me a aparecer con la posicion del "Hola"
#Y si hay varios datos repetidos, puedo usar el .count, y como hay dos 4 repetidos, entonces el los contara osea: print(tupla.count(4)) y en la terminal aparecera que hay 2 en total, osea 2 cuatros
#Tambien puedo usar el metodo len, para que nos indique cuantos elementos hay en esta tupla osea: print(len(tupla))
#Y si queremos tranformar una tupla en una lista se hace asi
tupla = (4, "Hola", 6.78, [1,2,3],4)
lista = list(tupla)#uso la funcion list para pasar

print(lista)

#Este es otro para pasar de lista a tupla
#Tambien se puede hacer de viceversa
#uso la funcion tuple
lista = [4, "Hola", 6.78, [1,2,3],4]
lista = tuple(lista)

print(print)

#Las tuplas principlamente se usan cuando principal mente se han creado, los elementos no seran modificados