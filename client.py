import socket               # Import socket module
import time
while 1:
    mes = raw_input("Message:")
    s = socket.socket()         # Create a socket object
    host = "192.168.1.123" # Get local machine name
    port = 8080                # Reserve a port for your service.
    x=0
    s.connect((host, port))
    mes = raw_input("Message:")
    s.send(mes)
    while x==1:
        data = s.recv(1024)
        if data == "CLOSECONNECTION":
            x=1
        else:
            print data
    time.sleep(.1)
    s.close                     # Close the socket when done
