import socket

c = socket.socket()

c.connect(('172.16.2.37', 9991))

name = input("Enter your name")
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())