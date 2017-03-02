#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones1
import json
import time
#se crea una variable de conoxion tipo socket
server= socket.socket()
#direccion ip del servidor y puerto de la conexion
server.bind(("",35000))
#cuantas conexiones se van a escuchar
server.listen(1)
ruta_c, direccion=server.accept()
login=''
usuario=''
while True:
   if login=='':
    recibido=''
    dato_cliente=''
    recibido = ruta_c.recv(1024)
    dato_cliente = ''
    data=funciones1.usuarios()
    dato_cliente=json.loads(recibido)
    dato_coneccion=json.loads(data)
    #print dato_cliente[0]
    fecha_actual= time.strftime("%c")
    if dato_cliente[0] in dato_coneccion:
        if dato_cliente[1] == '123':
           # ruta_c.send()
            f = open("datosacceso.txt", "a");
            f.write("Datos de usuario \n usuario: "+dato_cliente[0]+", password: "+dato_cliente[1]+"\n Direccion IP:"+direccion[0]+"\n Inicio de sesion:" + fecha_actual + "\n");
            f.close()
            data = 'true'
            login=data

            ruta_c.send(data)
        else:
            login=''
            ruta_c.send('false')
    else:
        login = ''
        ruta_c.send('usuario incorrecto ')
   else:
       recibido = ruta_c.recv(1024)
       dato_calcu = json.loads(recibido)
       if dato_calcu[0]=='a':
           resp=funciones1.suma(dato_calcu[1],dato_calcu[2])
       if dato_calcu[0]=='b':
           resp=funciones1.resta(dato_calcu[1],dato_calcu[2])
       if dato_calcu[0]=='c':
           resp=funciones1.multi(dato_calcu[1],dato_calcu[2])
       if dato_calcu[0] == 'd':
           resp = funciones1.div(dato_calcu[1], dato_calcu[2])

       if dato_calcu[0] == 'e':
            break
       ruta_c.send(resp)
    #devolver peticion al cliente
print "Hasta la Vista"
ruta_c.close()
server.close()