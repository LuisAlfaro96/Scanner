#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

#limpiar la pantalla
subprocess.call('clear',shell=True)
#ENtrada de datos
remoteServer = raw_input("Enter a remote host to scan:")
remoteServerIp = socket.gethostbyname(remoteServer)#funcion propia de la liberia socket para obtener ip del dominio
print "-"*60
print "Empezando Scaneo"
print "-"*60
t1 = datetime.now()
try:
    for port in range (0,1025):
        sock = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
        resultado = sock.connect_ex((remoteServerIp,port)) # aqui es donde esta la magia pues lo que hace es fijarse si existe una conexion existosa entre el socket del puerto correspondiente con la dir ip que le enviamos
        if resultado == 0:
            print "Puerto:  Open".format(port)
        sock.close()
except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
