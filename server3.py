#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones3
import json

#se crea una variable de conoxion tipo socket
server= socket.socket()
#direccion ip del servidor y puerto de la conexion
server.bind(("",35000))
#cuantas conexiones se van a escuchar
server.listen(1)
ruta_c, direccion=server.accept()
while True:
  datos = funciones3.menu()
  ruta_c.send(datos)
ruta_c.close()
server.close()