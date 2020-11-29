import socket


HOST='127.0.0.1' #localhost
PORT=65432 #ports >1032 are non priveleged

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT)) #tuple needs to be passed in
    s.sendall(b'Hello World!')
    data=s.recv(1024)
    s.close()

print("received data", repr(data))