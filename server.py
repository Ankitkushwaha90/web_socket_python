import socket

# Create the socket object
s = socket.socket()
print('Socket Created')

# Bind the socket to localhost and port 9999
s.bind(('172.16.2.37', 9991))

# Start listening for incoming connections (3 is the max number of queued connections)
s.listen(3)
print('Waiting for connections')

while True:
    # Accept an incoming connection
    c, addr = s.accept()

    name = c.recv(1024).decode()
    print("Connected with", addr, name)

    # Send a message to the client (encoded as bytes)
    c.send(bytes('Welcome to Telusko', 'utf-8'))

    # Close the connection after sending the message
    c.close()
