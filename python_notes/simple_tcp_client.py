import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 80))
msg = s.recv(1024)
print("server:", msg.decode())
s.send(b"thnx server")
s.close()
