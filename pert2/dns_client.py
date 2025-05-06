import socket
DOMAIN_NAME = 'www.facebook.com'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(DOMAIN_NAME.encode(), ('localhost', 8000))

response, _ = client_socket.recvfrom(1024)
ip_address = response.decode()
print(f"IP address : {ip_address}, Domain name: {DOMAIN_NAME}")