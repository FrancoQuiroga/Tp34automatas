#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# www.pythondiario.com
 
import re
 
#Definimos la funcion caracter 
def caracter(character):
    global simbolo
    simbolo=""
    global Fin
    Fin=" "
    #digito="[m|n]"
    letra_m = "m"
    letra_n = "n"
    #operador="(\+|\-|\*|\/)"
     
    #comparamos si es digito o operador
    if(re.match(letra_m,character)):
        simbolo=" letra m"
        return 0
       
    elif(re.match(letra_n,character)):
        simbolo=" letra n"
        return 1
    
    else:
        # if(re.match(operador,character)):
        #     simbolo="Operador"
        #     return 1
        simbolo = " valida "

        if(character==Fin):
            return 2
         
        #si no es ni un digito ni un operador entonces es un caracter no validp
        print("Error el ",character,"no es valido")
        exit()
 
#definimos al la funcion  encabezado
def encabezado():
    print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
    body()
 
#definimos la funcion contenido donde guarda cada valor despues de encontrarlo en un ciclo
def contenido(estadosig,character,simbolo,estado):
    
    print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
    body()
 
#solo muestra la linea que se repetira cada vez que la mandemos a llamar
def body():
    print("+--------------+---------+-----------+---------------+")
 
#MAIN
#Este es la tabla de transiciones del automata AFD creado
#tabla=[[1,"E","E"],[1,2,"E"],[3,"E","E"],[3,2,"A"]]
    '''
    0 = I
    1 = A
    2 = B
    3 = C
    '''
tabla=[[1,'E',"E"],[2,3,4],[2,3,4],[2,3,4],[4,4,4]] # [estado a cambiar con m,estado a cambiar con n, Acepta Cadena Actual] 
estado = 0

print ("""+-------------------------------------+
|    La ExReg que acepta es: m(m|n)*  |
+-------------------------------------+""")
 
print ("""+-------------------------------------+
|    Ingrese una cadena a evaluar:    |
+-------------------------------------+""")
cadena = input()
body()
encabezado()
cadena += ' '
#ciclo para recorrer la cadena
for  character in cadena:
    estadosig=estado
     
    #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
    charcaracter= caracter(character)
     
    #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
    estado=tabla[estado][charcaracter]
     
    #Si el valor obtenido es una E imprimimos cadena no valida
    if (estado=="E"):
        print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
        body()
        print("""|              Cadena No Valida :(                   |
+----------------------------------------------------+""")
        exit()
    contenido(estadosig,character,simbolo,estado)
 
#al concluir si el estado no es 3 que es el de aceptacion imprimimos cadena no valida    
if(estado!=4):
        print("""|              Cadena No Valida :(                   |
#+----------------------------------------------------+""")
 
#si el estado es 3 es una cadena de aceptacion
if(estado==4):
    print("|     ",estado,"      |         |    FND    |               |")
    body()
    print("""|                Cadena Valida :)                    |
+----------------------------------------------------+""")
