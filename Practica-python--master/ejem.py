import turtle 
from time import sleep

# Part 1 : Initialize the module
t = turtle.Turtle()#La t va hacer nuestra variables que usaremos como si fuera una super clase
t.speed(4) #.speed Velocidad del lapiz
turtle.bgcolor("black") #.bgcolor va hacer el color de la ventana
t.color("white") #Color del lapiz
turtle.title('Netflix Logo') #.title nombre de la ventana 

# Part 3 : Drawing the N shape
#Lapiz que lleva a escribir abajo
t.up() 
t.color("black") #Color de el lapiz
t.setheading(270) #Movinmiento a la derecha 
t.forward(240) #Movimiento hacia abajo
t.setheading(0) 
t.down() 
#Primer palo de N 
t.color("red") #Color de el lapiz
t.fillcolor("#E50914") #Tipo de color 
t.begin_fill() #Relleno 
t.forward(30) 
t.setheading(90) 
t.forward(180)#Girar 180 grados
t.setheading(180) 
t.forward(30) 
t.setheading(270) 
t.forward(180) 
t.end_fill() 
t.setheading(0) 
#Segundo palo de N 
t.up() 
t.forward(75) 
t.down() 
t.color("red") 
t.fillcolor("#E50914") 
t.begin_fill() 
t.forward(30) 
t.setheading(90) 
t.forward(180) 
t.setheading(180) 
t.forward(30) 
t.setheading(270) 
t.forward(180) 
t.end_fill() 
#Interseccion de N 
t.color("red") 
t.fillcolor("red") 
t.begin_fill() 
t.setheading(113) 
t.forward(195) 
t.setheading(0) 
t.forward(31) 
t.setheading(293) 
t.forward(196) 
t.end_fill() 
t.hideturtle() 

sleep(10)