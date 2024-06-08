import re
#import unittest
class Pila:
    def __init__(self):
        self.items = ['$','E']

    def insertar(self, item): #inserta elemento en la pila (cima)
        self.items.append(item)

    def extraer(self): #extrae elemento de la pila (cima)
        return self.items.pop()

    def inspeccionar(self): #devuelve el elemento de la cima de la pila
        return self.items[-1]
     
    def contenido(self): #devuelve el tamaño de la pila
        return self.items

tablasintactica = [
    ["E->T E'", "", "", "", "E->T E'", "", ""],
    ["", "E'->+ T E'", "", "", "E'->e", "", "E'->e"],
    ["T->F T'", "", "", "", "T->F T'", "", ""],
    ["", "T'->e", "T'->- F T'", "", "", "F'->e", "F'->e"],
    ["F->G F'", "", "", "", "F->G F'", "", ""],
    ["", "F'->e", "F'->e", "F'->% G F'", "", "F'->e", "F'->e"],
    ["G->id", "", "", "", "G->( E )", "", ""]
]

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
    if string_entrada == 'E':
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
    return f'El resultado de tu operación es: {resultado}'

def listarelementos(entrada): #lista de strings para usar en el árbol
    result = re.findall(r'\d+|[()+\-%]', entrada)
    result.append('$')  
    return result

def arbolsintactico(cadena):
    cadena = listarelementos(cadena)
    pila = Pila()
    resultado = ''
    print('{:<30}{:<25}{:>25}'.format('PILA', 'ENTRADA', 'SALIDA')) 

    while cadena:
        if pila.inspeccionar() == '$' and cadena[0] == '$':
            print('{:<30}{:<25}{:>25}'.format(str(pila.contenido()), str(cadena), resultado))
            return 'Árbol sintáctico completo'
        
        entradaactual = cadena[0]
        cimadepila = pila.inspeccionar()
        
        if re.match(r'[\d]+', entradaactual) and cimadepila == 'id':
            pila.extraer()
            cadena.pop(0)
            print('{:<30}{:<25}{:>25}'.format(str(pila.contenido()), str(cadena), resultado))
            continue
        
        if cimadepila == entradaactual:
            pila.extraer()
            cadena.pop(0)
            print('{:<30}{:<25}{:>25}'.format(str(pila.contenido()), str(cadena), resultado))
            continue
        
        try:
            resultado = tablasintactica[obtener_fila(cimadepila)][obtener_columna(entradaactual)]
        except:
            print(f'La cadena tiene un error sintáctico en la entrada actual: \n {entradaactual} (No forma parte del analizador sintáctico)')
            return 'Error'

        if resultado == '':
            print('La cadena ingresada está mal escrita')
            return 'Error'

        posicion = resultado.find('>')
        produccionsig = resultado[posicion+1:]
        pila.extraer()
        for simbolo in reversed(produccionsig.split()):
            if simbolo != 'e':
                pila.insertar(simbolo)
        
        print('{:<30}{:<25}{:>25}'.format(str(pila.contenido()), str(cadena), resultado))
#    if pila.contenido == ['$','E']:
#        print('No ingresó ning')

# class Testcolumnayfila(unittest.TestCase):
#     def test_columna_id(self):
#         self.assertEqual(obtener_columna('195 + 200'), 0)
# class Testcuenta(unittest.TestCase):
#     def test_returnt(self):
#         self.assertEqual(calcularcuenta('10+10'), 'El resultado de tu operación es: 20')
#     def test_listarelementos(self):
#         cadena = '10+10'
#         self.assertEqual(listarelementos(cadena), ['10','+','10'])


def main():
    entrada = input("Ingrese una expresión matemática(Ej:10+5-2): ")
    arbolsintactico(entrada)
    print(calcularcuenta(entrada))

if __name__ == "__main__":
    main()

# unittest.main()