#funciones
'''''
var_altura = int(input("Cual estu altura?: "))

def mostrarAltura(altura):
    resultado = ""
    
    if altura >= 180:
        resultado = "Eres una persona alta"
    else:
        resultado = "Eres una persona bajita"
        
    return resultado 
        
print(mostrarAltura(var_altura))
'''''

#Listas
personas = ["Paco", "Juan", "Rodrigo" ]
print(personas[0])

#Buclefor

for personas in personas:
    print("-"+personas)
