import socket # Imports socket library
host = socket.gethostbyname(socket.gethostname()) #Gets IP of your computer
port = 8080 #Port that is used on server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # See server2.py
sock.connect((host,port)) #Connects socket to given IP and port
msg = "HEI"
sock.send(msg.encode()) # Sends encoded message