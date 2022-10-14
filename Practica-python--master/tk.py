from distutils.command.config import config
from email.mime import application
from select import select
import tkinter 
from tkinter import ttk
from tkinter import *

from setuptools import Command

class root:
    def __init__(self, window):
        self.vent=window
        self.vent.geometry("500x310")
        self.vent.title("Lyrics")
        self.vent.resizable(width=False, height=False)
        
        lbl1=Label(self.vent, text="Seleccionar cancion")
        lbl1.config(fg="black", font=("Dosis", 12))
        lbl1.place(x=5, y=5)
        
        select=ttk.Combobox(self.vent, state="redonly", values=["Name1", "Name2", "Name3"])
        select.place(x=210, y=10)
        
        def fun1():
            lbl1=Label(fc, text="Texto1")
            lbl1.config(bg="white", fg="black", font=("Dosis", 18))
            lbl1.place(x=110, y=50)
              
              
        def fun2():
            cf=Canvas(fc)
            cf.config(bg="Green", highlightthickness=0)
            cf.place(x=5, y=150, width=390, height=160)
            
            lbl1=Label(fc,text="Texto2")
            lbl1.config(bg="white",fg="black", font=("Dosis", 18))
            lbl1.place(x=110, y=50)
    
            seguir=Button(self.vent, text="Seguir ->", command=fun1)
            seguir.place(x=70, y=74)
            
        
        btn1=Button(self.vent, text="Mostrar", command=fun2)
        btn1.place(x=370, y=9)
                
        #Creamos un contenedor para los textos 
        fc=ttk.Notebook(self.vent)
        fc.place(x=60, y=100, width=390, height=160)
    
if __name__ == '__main__':
    window=Tk()
    application=root(window)
    window.mainloop()