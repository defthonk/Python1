#Primero se crea un input para recibir datos tipo numero, para preguntar su estrato
estudiante = int(input("Digite su estrato: "))
Carrera =""
#Despues se crea otro input preguntando que carrera quiere estudiar y dependiendo de su opcion, ya sea l, m, t se vaya a esa opcion
Carrera = input("Que carrera quiere estudiar? ")
#Defino que l es igual a un millon, m que es igual a un millon doscientos y t es igual a un millon trecientos
#Dependiendo de la carrera que se escoja, sera igual a un precio
if Carrera == "l":
    Carrera = 1000000
    print("Elegiste tecnologia en matematicas")
elif Carrera == "m":
    Carrera = 1200000
    print("Elegiste ingenieria")
elif Carrera == "t":
    Carrera = 1300000
    print("Elegiste macroeconomia")
else:  
    print("Opcion incorrecta")

#Se crea un un if y se encierra la varible estudiante que si es igual a 2 tiene un 10% de descuento en su matricula
if estudiante == 2: #Si pertenece al estrato 2 tiene 10% de descuento
    print("Se le hara un descuento del 10 porciento sobre el valor de su matricula")
    sub = Carrera #se crea una varible que va ser igual al segundo input que se tiene en el sistema
    desc = float(sub) * 0.10 #despues sub tiene que ser un float ya que no acepta valores enteros * 0.10, que seria 10%
    total = sub - desc #Despues se crea una variable llamada total que encierre el valor sub menos desc
    print(f"subtotal: {sub}")
    print(f"descuento: {desc}")
    print(f"Total a pagar: {total}")
    #Por ultimo se muestra por pantalla cada valor, desde su valor principal, cuanto se descuenta y cuanto es el valor a pagar

if estudiante ==1: #Si pertenece al estratato 1 del 20%
    print("Se le hara un descu  ento del 20 porciento en el valor de su matricula") #Si pertenece al estrtato 1 del 20%
    sub = Carrera 
    desc = float(sub) * 0.20
    total = sub - desc
    print(f"subtotal: {sub}")
    print(f"descuento: {desc}")
    print(f"Total a pagar: {total}")

else: 
    print("opcion incorrecta")

