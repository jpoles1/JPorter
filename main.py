import socket
import time
s = socket.socket()         # Create a socket object
host = "192.168.1.123" # Get local machine name
port = 8080
rsize = 1024                # Reserve a port for your service.
s.bind((host, port))
s.listen(5)
log = []                 # Now wait for client connection.
while True:
    c, addr = s.accept()
    data = c.recv(rsize)
    print(addr[0]+": "+data)
    log.append([addr[0], data])
    for i in log:
        c.send(i[0]+": "+i[1])
    c.send("CLOSECONNECTION")
time.sleep(.1)
c.close()                # Close the connection
