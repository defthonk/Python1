#and(conjuncion),or(disyuncion),not(negacion)

#Operador and(de aca para abajo escribire como usarlo y cual es su resultado)
#Operando 1   Operador   Operando2   Resuelto
#True         and          true      true
#True         and          false     false
#False        and          true      False
#False        and          False     false

#Operador or(si hay un operando true, el resultado es verdadero)
#Operando 1   Operador   Operando2   Resuelto
#True         or         true      true
#True         or         false     true
#False        or         true      true
#False        or         False     false

#Operador negacion
#Operador    Resultado
#not(True)   false
#nor(False)  True
a=10
b=15
c=20

r =  not((a<b) or (b<c))
print(r)

r = ((a==b))and((a!=c))
print(r)
