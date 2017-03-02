#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones1
import json
ruta_s= socket.socket()
#coneccion con el servidor
ruta_s.connect(("localhost",35000))
men=0
datos_usuario=[]
datos_oper=[]
login=''
while True:
    cadena_oper = ''
    datos_oper=[]
    if login=='':
        datos=''
        cadena_envio=''
        cadena_oper=''
        usuario = raw_input("ingrese usuario ")
        datos_usuario.append(usuario)
        password = raw_input("ingrese Contraseña ")
        datos_usuario.append(password)
        cadena_envio = json.dumps(datos_usuario)
        ruta_s.send(cadena_envio)
        datos_usuario=[]
        datos = ruta_s.recv(1000)
        if datos == 'true':
            print "Bienvenido al Sistema\n"
            login='true'
            datosok=funciones1.menu()
            listamenu=funciones1.menu_lista(datosok)
            opt = raw_input("Seleccione una opción ")
            datos_oper.append(opt)
            if opt == 'e':
                datos_oper.append('')
                datos_oper.append('')
                cadena_oper = json.dumps(datos_oper)
                ruta_s.send(cadena_oper)
                break
            n1 = raw_input("ingrese primer Número ")
            datos_oper.append(n1)
            n2 = raw_input("ingrese segundo Número ")
            datos_oper.append(n2)
            if opt == 'd':
                if n2 == '0':
                    print "No se puede dividir por cero"
                    n2 = raw_input("ingrese segundo Número ")
                    datos_oper[2]=(n2)


            cadena_oper=json.dumps(datos_oper)
            ruta_s.send(cadena_oper)

        else:
            login=''
            print 'Password incorrecto'
    else:
        datos = ruta_s.recv(1000)
        print 'Resultado de la operación '+datos
        datosok = funciones1.menu()
        listamenu = funciones1.menu_lista(datosok)
        opt = raw_input("Seleccione una opción ")
        datos_oper.append(opt)
        if opt == 'e':
            datos_oper.append('')
            datos_oper.append('')
            cadena_oper = json.dumps(datos_oper)
            ruta_s.send(cadena_oper)
            break
        n1 = raw_input("ingrese primer Número ")
        datos_oper.append(n1)
        n2 = raw_input("ingrese segundo Número ")
        datos_oper.append(n2)
        if opt == 'd':
            if n2 == '0':
                print "No se puede dividir por cero"
                n2 = raw_input("ingrese segundo Número ")
                datos_oper[2] = (n2)

        cadena_oper = json.dumps(datos_oper)
        ruta_s.send(cadena_oper)


    #verificar mensaje para salir
    #if usuario == 'salir':
     #   break
#print "Vuelva cuando quiera"
#cerrar conexion con el servidor
ruta_s.close()