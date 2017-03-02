# -*- coding: utf-8 -*-
import json
import os
def menu():
    lista=['Menú de Opciones','a. Listar archivos','b. Crear archivo','c. Modificar archivo','d. Eliminar archivo','e. Salir']
    cadena=json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def listarfiles():
    path = 'D:/programaciondistribuida/taller2/'
    # Lista vacia para incluir los ficheros
    lstFiles = []
    # Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros
    # Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if (extension == ".txt"):
                lstFiles.append(nombreFichero + extension)
    cadena = json.dumps(lstFiles)
    return cadena
def crearfile(nfile,contenido):
    fo = open(nfile + ".txt", "a")
    fo.write(contenido)
    fo.close()
    lista=["Archivo creado Exitosamente!!!",'Menú de Opciones','a. Listar archivos','b. Crear archivo','c. Modificar archivo','d. Eliminar archivo','e. Salir']
    cadena = json.dumps(lista)
    return cadena

def editafile(file):
    if os.path.isfile(file + ".txt"):
        fo = open(file+ ".txt", "r")
        contenido=fo.read()
    else:
        contenido="Archivo No existe"
    return contenido

def actufile(file,conten):
    if os.path.isfile(file + ".txt"):
        fo = open(file+".txt", "a")
        fo.write(conten+"\n")
        fo.close()
        lista = ["Archivo modificado Exitosamente!!!", 'Menú de Opciones', 'a. Listar archivos', 'b. Crear archivo',
             'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir','Digite una opcion']
    else:
        lista = ["Archivo No existe", 'Menú de Opciones', 'a. Listar archivos', 'b. Crear archivo',
                 'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir', 'Digite una opcion']
    cadena = json.dumps(lista)
    return cadena

def eliminar(file):
    if os.path.isfile(file+".txt"):
        os.remove(file+".txt")  # remove the file
        lista = ["Archivo eliminado Exitosamente!!!", 'Menú de Opciones', 'a. Listar archivos', 'b. Crear archivo',
             'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir']
    else:
        lista = ["Archivo No existe", 'Menú de Opciones', 'a. Listar archivos', 'b. Crear archivo',
                 'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir']
    cadena = json.dumps(lista)
    return cadena


