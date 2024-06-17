import re
class InputError(Exception):
    pass

def tomaruserinput(cantidadopciones: int)-> int: 
#función que comprueba que el usuario haya elegido la opcion correcta 
    #Que tiene que hacer esta funcion? Tomar inputs? Procesar los inputs? Verificar que los inputs esten bie?
    while True:
        opcion = ''
        try:
            opcion = int(input(f'Ingrese una opción(1-{cantidadopciones}): '))
            if opcion < 1 or opcion > cantidadopciones:
                raise InputError
            return  opcion
        except InputError:
            print('Ingrese una opción válida')
        except ValueError:
            print('La opcion tiene que ser un número')

# tomaruserinput(5)
class AnalizadorSintáctico: #Tipos de datos a analizar: Access Points, Usuarios, Tiempo determinado
    def __init__(self,basededatos=[],inicioperiodo=0,finperiodo=0):
        self.basededatos = basededatos
        self.inicioperiodo = inicioperiodo
        self.finperiodo = finperiodo

    def analizarfechas(self):
        pass