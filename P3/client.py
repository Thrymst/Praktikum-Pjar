import socket

# Inisialisasi socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server
host = '127.0.0.1'
port = 5000
client_socket.connect((host, port))
print("Terhubung ke server...")

# Loop komunikasi
while True:
    # Kirim pesan ke server
    message = input("Anda: ")
    client_socket.send(message.encode())
    
    # Terima balasan dari server
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

# Tutup koneksi
client_socket.close()