'''''''''
#Primera parte de la explicacion de conjuntos
#Grupos de elementos desordenados, pero no se pueden repetir o no pueden haber duplicados
#Para especificar que es conjunto usamos la funcion set()
conjunto = set()
#Dentro de los conjuntos no pueden haber otro tipo de colecciones, osea, aca no puede haber conjunto = {1,2,3,"hola",4.56,[1,2,3]}, de una nos va a saltar error
#si por ejemplo duplicamos el 1,2,3 osea asi conjunto = {1,2,3,"hola",4.56,1,2,3} el va a borrar el ultimo y solo va a dejar los principales
conjunto = {1,2,3,"hola",4.56}
#Si quiero agregar un elemento uso el comando .add
conjunto.add(5)
conjunto.add("Adios")
conjunto.add('a')
#Estos elementos se agregar donde el conjunto quiera

#Por ejemplo si quiero eliminar algun dato del conjunto usaremos el comando .discard
conjunto.discard(3)

#Y si quiero que el conjunto quede vacio usaria el comando .clear, este lo voy a colocar aca, por que si lo coloco abajo se me va a borrar todos los elemtos, pero se usaria: conjunto.clear() y el automaticamente me borra todo 

#Tambien puedo buscar un determinado elemento con la funcion in, por ejemplo quiero buscar el 4.56, colocaria: print(4.56 in conjunto) y en la terminal me aparecera true, por que si esta, pero si por ejemplo coloco print(7 in conjunto), me va a aparecer error, debido que el 7 no esta en el conjunto
print(7 in conjunto)

print(conjunto)


#Segunda parte de la explicacion
#No haria falta colocar un .set, python se da cuenta que los elementos se estan separando por comas, por que en los diccionarios usamos 2 puntos, pero tambien usa {}

a = {1,2,3}
b = {3,2,1}
#1 Para saber de una igualdad, osea si el conjunto a es igual al conjunto b, usamos: print(a == b), y nos daria falso, por que dentro de a esta 1,2,3 y dentro de b 3,4,5 
#1.2Pero si por ejemplo en a hay 1,2,3 y en b 3,1,2 y usamos la funcion de igualdad, nos saldria que es verdadero o true, debido que no importa si estan en desorden, igual son elementos iguales
#print(a == b), dejare ese print ahi, eliminar el numeral, al usarlo, con la explicacion de arriba, de la igualdad

#Con la funcion: print(len(a)), nos estaria contando que en el conjunto a hay 3 elementos y en el conjunto b tambien hay 3 elementos, dentro del: (len(a)), cambiamos la letra a por b, o ya miramos por que lo cambiamos, depende del nombre del conjunto

#Tercera parte de conjuntos, guiado a matematicas 

a = {1,2,3}
b = {3,4,5}
#Para unir conjuntos usariamos este simbolo |, osea si tenemos 2 conjuntos, que en este caso seria a y b, a tiene 1,2,3 y b tiene 3,4,5, los colocaria en una sola linea y daria como resultado: {1, 2, 3, 4, 5, 6}, con la union, y se escribiria asi: c = a | b y abajo colocamos print(c), para imprimir el resultado que esta dentro de c, que c contiene a y b
#Pero tambien podemos hacer la interseccion, osea elementos que hay en ambos conjuntos, osea si en a hay 1,2,3 y en b 3,4,5 y usamos el simbolo &, nos daria como resultado {3}, que se repite en el conjunto y nos quedaria c = a & b y despues imprimimos el resultado: print(c)
#Y tambien tenemos la diferencias, osea elementos a que no estan en b, con el menos, osea: c = a - b, y nosa daria como resulado 1,2 por que en b ya esta repetido el 2 y viceversa, osea c = b - a, y nos daria como resultado 4,5 por que en a ya esta 3
#Tambien la diferencia simetrica, osea elementos que estan en a y en b, pero no estan en ambos, osea usando: c = a ^ b, nos daria como resultado que 1,2,4,5 se encuentran dentro de los conjuntos, pero no muestra 3 por que se esta repitiendo
c = a ^ b
print(c)


#subconjuntos(parte 3.1)
a = {1,2,3}
b = {3,4,5}
#Vamos a ver si un conjunto es subconjunto de otro, osea si un conjunto esta dentro de otro, colocamos. print(a.issubset(c)), esto nos quiere decir que si esta dentro del conjunto c y nos daria que es true, y si preguntamos que b esta dentro de c, tambien nos daria true, por que si esta dentro, usando: print(b.issubset(c))
#pero si dentro del conjunto c, borramos el 4 y preguntamos que si b estan dentro de c, o si es subconjunto de c, usando: print(b.issubset(c)), nos va a saltar false debido que ya se borro el 4 y dentro de b hay 3,4,5 y dentro de c 1,2,3,5
c= {1,2,3,4,5}

#Tambien se puede ver un super conjunto, osea en este caso si c es el super conjunto de a, usamos: print(c.issuperset(a)), esto nos daria true, debido que c contiene, 1,2,3,5 y a contiene 1,2,3 enotnces si es verdad que esta dentro del superconjunto c 
#Pero si por ejemplo tenemos que b tiene 3,4,5 y colocamos: print(c.issuperset(b)), nos daria false, por que a c le faltaria el 4, para que c sea el superconjuto de b

#Pero tambien podemos preguntar si ambos conjuntos son disconexos, osea que si no comparten ningun elemento en comun, osea se usaria: print(a.isdisjoint(b)) y me daria false por que si comparten un elemento en comun que es el 3, pero si colocamos en vez del 3, colocamos 7, pues daria true, por que no compartirian ningun elemento en comun, usando el comando .isdisjoint, ejemplo print(a.isdisjoint(b))
'''''''''

#Parte 4 explicacion 
#Tambien podemos hacer conjuntos inmutables, usando la funcion frozenset({})
a = frozenset({1,2,7})
b = {3,4,5}
#Osea si queremos agregar algo al conjunto a, no nos dejaria, por que el conjunto a ya es inmutable, osea si colocamos: a.add(3) no nos deja por que ya no se puede agregar, ni eleminar, ni modificar al ser inmutable
a.add(3)

print(a)