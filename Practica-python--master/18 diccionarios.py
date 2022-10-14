''''''''''
#Parte 1, valores tipo texto
#Estos son otro tipo de coleccion, donde los elementos se guardan desordenados y la principal caracteristica, es que tienen 2 elemtentos por posicion, la clase y el valor(no pueden haber claves duplicadas)
diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}
#Osea azul es clave y el valor seria blue
print(diccionario)
#Y si por ejemplo solo quiero que me aparezca un elemento del diccionario, colocaria print(diccionario["azul"]), como resultado me daria blue, osea el resultado de azul
print(diccionario["azul"])

#Tambien si queremos agregra un elemento al diccionario, colocariamos: diccionario["amarillo"] = "yellow" y abajo un print para imprimir el resultado, osea print(diccionario)
diccionario["amarillo"] = "yellow"

print(diccionario)

#Y si queremos modificar un elemento del diccionario se colocaria: diccionario["azul"] = "BlUE", con esto queremos que azul seria igual BLUE, pero con la respuesta en mayuscula, y abajo colocamos un print(diccionario), para imprimir el resultado

diccionario["azul"] = "BlUE"

print(diccionario)

#Tambien podemos eliminar un valor o elemento del diccionario, usando: del(diccionario["verde"]), esto nos eliminaria el verde del diccionario con su respuesta tambien, y abajo un print(diccionario), para imprimir el resultado

del(diccionario["verde"])

print(diccionario)


#Parte 2, pero con valores tipo string o numeros
diccionario = {"Juan":{"edad":18,"estatura":1.72},"Jose":[21,1.75], "Maria":[25,1.75]}
#Si acomodamos asi podemos mirar que dentro de juan hay otro diccionario, con edad y nombre, y si imprimimos y buscamos solo el alejandro, nos va a aparecer los valores que estan dentro de juan, osea estatura y edad, osea un valor que enceuntre en dicha clave
print(diccionario["Juan"])
'''''''''

#Parte 3, diccionario 

equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo",17:"Mario Mandzukic"}
#Clave 10 = tipo cadena Paulo Dybala 
#Si buscamos por ejemplo a cristiano ronaldo, colocariamos: print(equipo[7]) y asi sucesivamente con los otros jugadores que estan e el diccionario
#Pero si coloco un numero, y no hay ningun jugador dentro de mi diccionario con ese dorsal uasriamos: print(equipo.get(6,"no existe un jugador con ese dorlas")), con el .get para imprimir el mensaje
#Y si queremos hacer una busqueda directa dentro del diccionario, colocaria: print(10 in equipo), y nos saldra que true, si esta dentro del diccionario, si colocamos por ejemplo, en vez del 10, colocamos 3, saldra false, ya que no esta dentro del diccionario
#Y si quiero todos los dorsales del equipo, osea solo el numero, colocaria: print(equipo.keys()). solo apareceran los dorsales, osea solo el 10,11,7,17
#Y ahora para que solo aparezca el nombre o los valores, colocariamos: print(equipo.values()), con esto solo apareceran los nombres de los judaores, no su numero
#Y para mostrar la clave y el valor, osea el numero y el nombre se puede colocar de la manera facil: print(equipo) o print(equipo.items())
#Y si quiero que me diga cuantos jdaores hay en mi equipo, usaria: print(len(equipo)), osea cuantos jugaodres hay en mi equipo o cuantos elementos hay
#si quiero eliminar todo el equipo usaria equipo.clear() y abajo imprimo el resultado con: print(equipo)
equipo.clear()

print(equipo)