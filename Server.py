import socket
import select
import time
host = socket.gethostbyname(socket.gethostname())  # Host IP
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket and bind
sock.bind((host, port))
print(host)
sock.listen()
c,addr = sock.accept()
msg = c.recv(1024).decode()
print(msg)





"""
inputs = [sock]
outputs = []
while True: 
    read, write, exception = select.select(inputs, outputs, inputs)
    for s in read:
        if s is sock: 
            c,addr = s.accept()
            inputs.append(c)
            outputs.append(c)
            read, write, exception = select.select(inputs, outputs, inputs)

        elif s in outputs:
            msg = s.recv(1024)
            print(msg.decode())
            read, write, exception = select.select(inputs, outputs, inputs)
            time.sleep(10)"""

