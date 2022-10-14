#Se le conoce por que tiene un numero determinado de identaciones 
#Este bucle se usa con colecciones
#Desbloquee los ejemplos que estan en la linea 5 y 6 para verlo
"""""""""
for i in [2,10,4,"Juan"]:
    print(f"Elemento: {i}")
"""""
#Se puede usar con listas, tuplas, conjuntos, tambien diccionarios, pero este tiene clave y valor
#Este ejemplo va hacer con 
#Desbloquee los ejemplos que estan en las lineas 12,14,15
"""""""""
coleccion = {"Juan":18, "Rodolf":23, "pol":24}

for i in coleccion:
    print(f"{coleccion[i]}")    
"""
#Este ejemplo es casi el mismo de arriba para mostrar la clave y valor que estan en el diccionario, no solo la clave, que es lo que muestra en ele ejemplo de arriba 
#Desbloquear las lineas 20,22,23, es ele mismo ejemplo de arriba, solo que este muestra clave y valor 
"""""""""
coleccion = {"Juan":18, "Rodolf":23, "pol":24}

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")   
"""
#Otra forma de hacer el ejemplo mas profesional, el mismo ejemplo que se encuentra ne las lineas 20,22,23
#Desbloque lineas 28,30,31
"""""""""
coleccion = {"Juan":18, "Rodolf":23, "pol":24}

for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")   
"""
#Tambien se pueden recorrer cadenas 

coleccion = ("Juanes")
for i in coleccion:
    print(f"{i}", end=" ") 