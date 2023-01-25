import socket 
import sys
host = socket.gethostbyname(socket.gethostname())  # Host IP
print(host)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, 80))
msg = sys.argv[1]
socket.send(msg.encode())