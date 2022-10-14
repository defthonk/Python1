'''''''''
#1 ejercicio
#Escriba un progama donde tenga una lista y que, a continuacion, elimine los elementos repetidos, por ultimo mostrar la lista
#Mi forma
list = ["ola", "olita", "siempre", "olita"]
print(list)
conjunto=set()
conjunto=set(list)
print(conjunto)

#La forma de ats

lista = [1,2,3,"Juan",2,2,1,"Juan",3]
conjunto = set(lista)
lista = list(conjunto)
print(lista)

#Tambien se puede hacer en una sola linea de codigo 
lista = [1,2,3,"Juan",2,2,1,"Juan",3]
lista = list(set(lista))
print(lista)
'''''''''

#2 ejercicio 
#Escriba un programa que tenga 2 listas y que, a continuacion, cree las siguientes listas(en las que no debe haber repeticiones):
#Lista de palabras que aparecen en las 2 listas
#Lista de palabras que aparecen en la primera lista, pero no en la segunda
#Lista de palabras que aparecen en la segunda lista, pero no en la primera
#Lista de palabras que aparecene en ambas listas

p = [1,2,3,4,5,4,3,2,2,1,5]
l = [4,5,6,7,8,4,5,6,7,7,8]

#Elimine los elementos repetidos de ambas listas
a = set(p)
b = set(l)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f"lista de elementos que aparecen en las 2 listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {soloA}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {soloB}")
print(f"Lista de palabras que aparecene en ambas listas: {interseccion}")
