#Importare libreria tkinter
from tkinter import *
from tkinter import messagebox
#Fucnin del boton
def mensaje():
    #Titulo, mensaje
    messagebox.showinfo("Titulo","Hola mundo")
#Creacion de la raiz
raiz = Tk()
#Titulo 
raiz.title("Sigueme")
#Dimensiones de la ventana 
raiz.geometry("250x250")
#Agregamos un boton
btn=Button(raiz,bg='#809A6F', fg='white', text="Da click", command=mensaje)
#Ubicamos el boton e la ventana 
btn.place(x=30, y=25)
#Bucle de la app
raiz.mainloop()

