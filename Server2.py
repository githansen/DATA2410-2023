import socket # Imports socket library

host = socket.gethostbyname(socket.gethostname()) #Gets IP of your computer
print(host)
port = 8080 # Port can be whatever you want, find one that is not used by other services
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates socket, AF_INET -> Address family (IPV4) - SOCK_STREAM -> Socket type (TCP Socket)
sock.bind((host,port)) # Assigns IP and port to the created socket
sock.listen() # Starts listening for connections
client, addr = sock.accept() # Waits for connections, accepts any incoming
msg = client.recv(1024).decode() #Receives and decodes message
print(msg)