import json
def usuarios():
    lista=['admin','usuario1','usuario2']
    cadena=json.dumps(lista)
    return cadena

def menu():
    lista=['a. Suma','b. Resta','c. Multiplicacion','d. Division','e. Salir']
    cadena=json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def suma(n1,n2):
    resp=int(n1)+int(n2)
    return str(resp)

def resta(n1,n2):
    resp=int(n1)-int(n2)
    return str(resp)

def multi(n1,n2):
    resp=int(n1)*int(n2)
    return str(resp)

def div(n1,n2):
    resp=float(n1)/float(n2)
    return str(resp)