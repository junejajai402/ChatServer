#simple 1 server 1 client test. only accepts 1 connection and prints the connecting tuple

import socket

HOST='127.0.0.1' #localhost
PORT=65432 #ports >1032 are non priveleged

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: #creates socket, AF_INET id the IPv4 family internet address family
    s.bind((HOST,PORT)) #binds host+port to this socket
    s.listen() #starts listening for incoming data/connections. we can specify how many we want too
    conn, addr = s.accept() #blocks all calls waiting to accept connection. creates new socket object for this purpose
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break #if no data is recieved
            conn.sendall(data) #sends data back
