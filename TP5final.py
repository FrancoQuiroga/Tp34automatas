import pandas as pd


# cargar datos del csv
# el archivo no lo subi en el github pq es muy grande, y no me deja
# hay que crear una carpeta que se llama csv , y adentro ponerl el archivo 
def cargar_datos(archivo):
    return pd.read_csv(archivo, low_memory=False)


def exportar_a_exel():
    pass



archivo_csv = 'csv/export-2019-to-now-v4.csv'
data = cargar_datos(archivo_csv)



# input
fecha_inicio = input("Ingrese la fecha de inicio (AAAA-MM-DD): ")
fecha_fin = input("Ingrese la fecha de fin (AAAA-MM-DD): ")



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
