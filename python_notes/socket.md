#socket 
 ``` python
  import socket
```
##tcp socket
```tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)```
##udp socket
```udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)```
##bind to an ip and port
```tcp.bind(("127.0.0.1",12345))```
##listen for connection
```tcp.listen(5)```
##accept connections
```
client_socket, client_address = tcp.accept()
print("connected to", client_address)
```
##send and recive data
###server side
```
client_socket.send(b"hello from server ")
data = client_socket.recv(1024)
print("client says:", data.decode())
```
###client side
```
tcp.connect(("127.0.0.1",12345))
tcp.send(b"hello from client ")
data = tcp.recv(1024)
print("server says:", data.decode())
```
##close the socket
```
s.close()
```
