# -*- coding: utf-8 -*-
import json
import os
def menu():
    lista=['Menú de Opciones','a. Comprar Productos','b. Ventas del Día','c. Inventarios','e. Salir']
    cadena=json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i
