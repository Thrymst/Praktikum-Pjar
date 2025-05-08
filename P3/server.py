import socket

# Inisialisasi socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat dan port
host = '127.0.0.1'
port = 5000
server_socket.bind((host, port))

# Listen untuk koneksi masuk
server_socket.listen(5)
print(f"Server mendengarkan di {host}:{port}...")

# Terima koneksi
client_socket, addr = server_socket.accept()
print(f"Terhubung dengan {addr}")

# Loop komunikasi
while True:
    # Terima data dari client
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")
    
    # Kirim balasan
    response = input("Anda: ")
    client_socket.send(response.encode())

# Tutup koneksi
client_socket.close()
server_socket.close()