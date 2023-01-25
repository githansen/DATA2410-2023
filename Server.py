import socket

host = socket.gethostbyname(socket.gethostname())  # Host IP
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket and bind
sock.bind((host, port))
print(host)
sock.listen()

while True: 
    c, addr=sock.accept()
    msg = c.recv(1024)
    print(msg.decode())
    