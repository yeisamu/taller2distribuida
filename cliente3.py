#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones3
import json
ruta_s= socket.socket()
#coneccion con el servidor
ruta_s.connect(("localhost",35000))
inicio=''
datos_oper=[]
cadena_oper=''
compra=[]
while True:
 inventario={1:'Arroz,100,1500','frijoles':'2,100,3000','Azucar':'3,50,2000','Panela':'4,20,3000','Jabón':'5,30,5000','Carne Cerdo':'6,20,12000','Carne res':'7,20,15000'}
 lista=((1,'Arroz',100,1500),('frijoles','2,100,3000'))
 #datos_oper = []
 #cadena_oper = ''
 #datos = ruta_s.recv(1000)
 #listamenu=funciones3.menu_lista(datos)
 #opt=raw_input('Selecciones una opción: ')
 #datos_oper.append(opt)
 for key in inventario:
     print key, ":", inventario[key]
 idpro=int(raw_input('Ingrese id del producto a comprar'))
 canti=int(raw_input('Cantidad'))
 compra.append(idpro)
 compra.append(canti)
 valor = inventario.get(idpro)
 print lista[0]
 if(canti>inventario[idpro][1]):
     print "No hay cantidades suficientes"
 #print inventario['verduras'][0]