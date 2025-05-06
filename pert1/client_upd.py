import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = 'hello, UDP Server!'

client_socket.sendto(bytes(message, 'utf-8'), ('localhost', 8001)
)
data, address = client_socket.recvfrom(1024)
print(data.decode('utf-8'))