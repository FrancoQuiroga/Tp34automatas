import re
import unittest

class Pila:
     def __init__(self):
         self.items = ['$','E']

     def insertar(self, item): #inserta elemento en la pila (cima)
         self.items.append(item)

     def extraer(self): #extrae elemento de la pila (cima)
         return self.items.pop()

     def inspeccionar(self): #devuelve el elemento de la cima de la pila
         return self.items[len(self.items)-1]
     
     def contenido(self): #devuelve el tamaño de la pila
         return (self.items)

tablasintáctica=[ ["E->TE'","","","","E->TE'","",""]
                 ,["","E'->+TE'","","","E'->e","","E'->e"]
                 ,["T->FT'","","","","T->FT'","",""]
                 ,["","T'->e","T'->-FT'","","","F'->e","F'->e"]
                 ,["F->GF'","","","","F->GF'","",""]
                 ,["","F'->e","F'->e","F'->% GF'","","F'->e","F'->e"]
                 ,["G->id","","","","G->( E )","",""]]


def obtener_columna(simbolo_entrada):
    if re.match(r'[\d]+', simbolo_entrada):
        return 0
    elif simbolo_entrada == '+':
        return 1
    elif simbolo_entrada == '-':
        return 2
    elif simbolo_entrada == '%':
        return 3
    elif simbolo_entrada == '(':
        return 4
    elif simbolo_entrada == ')':
        return 5
    elif simbolo_entrada == '$':
        return 6

def obtener_fila(string_entrada):
    if    string_entrada == 'E':
        return 0
    elif string_entrada == "E'":
        return 1
    elif string_entrada == "T":
        return 2
    elif string_entrada == "T'":
        return 3
    elif string_entrada == "F":
        return 4
    elif string_entrada == "F'":
        return 5
    elif string_entrada == "G":
        return 6
 
def calcularcuenta(cadena): # No es necesario un try/except porque la verificación se hace con el arbol sintactico
    resultado = eval(cadena)
    return (f'El resultado de tu operación es: {resultado}')

def listarelementos(entrada): #lista de strings para usar en el árbol
    result = re.findall(r'\d+|[()+\-%]', entrada)
    return result

def arbolsintactico(cadena):
    
    pila = Pila()
    resultado = ''
    print('{:<30}{:<25}{:>25}'.format('PILA', 'ENTRADA', 'SALIDA')) 
    
#   while cadena:
    print('{:<30}{:<25}{:>25}'.format(str(pila.contenido()), cadena, resultado))
    if pila.inspeccionar() == '$':
        return 'Árbol sintáctico completo'
    entradaactual = cadena[0]
    cimadepila = pila.inspeccionar()
    salidactual = tablasintáctica[obtener_fila(cimadepila)][obtener_columna(entradaactual)]

class Testcolumnayfila(unittest.TestCase):
    def test_columna_id(self):
        self.assertEqual(obtener_columna('195 + 200'), 0)
class Testcuenta(unittest.TestCase):
    def test_returnt(self):
        self.assertEqual(calcularcuenta('10+10'), 'El resultado de tu operación es: 20')
    def test_listarelementos(self):
        cadena = '10+10'
        self.assertEqual(listarelementos(cadena), ['10','+','10'])

arbolsintactico('HOLA')


unittest.main()
