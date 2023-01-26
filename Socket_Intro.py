import socket 
host = socket.gethostbyname(socket.gethostname())
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))

