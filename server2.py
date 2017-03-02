#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones2
import json

#se crea una variable de conoxion tipo socket
server= socket.socket()
#direccion ip del servidor y puerto de la conexion
server.bind(("",35000))
#cuantas conexiones se van a escuchar
server.listen(1)
ruta_c, direccion=server.accept()
login=''
while True:
    if login == '':
        datos = funciones2.menu()
        ruta_c.send(datos)
        login='true'
    else:
        resp=[]
        recibido = ruta_c.recv(1024)
        dato_calcu = json.loads(recibido)
        print dato_calcu[0]
        if dato_calcu[0] == 'a':
            resp = funciones2.listarfiles()
        if dato_calcu[0] == 'b':
            resp = funciones2.crearfile(dato_calcu[1], dato_calcu[2])
        if dato_calcu[0] == 'c':
            resp = funciones2.editafile(dato_calcu[1])
        if dato_calcu[0] == 'n':
            resp = funciones2.actufile(dato_calcu[1], dato_calcu[2])
        if dato_calcu[0] == 'd':
            resp = funciones2.eliminar(dato_calcu[1])
        if dato_calcu[0] == 'e':
            print "Hasta la Vista"
            break
        ruta_c.send(resp)
    #devolver peticion al cliente

ruta_c.close()
server.close()