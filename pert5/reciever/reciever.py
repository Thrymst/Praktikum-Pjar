import socket

def receive_file():
    host = '0.0.0.0'
    port = 8000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print(f"Menunggu koneksi di port {port}...")

    conn, addr = s.accept()
    print(f"Terhubung dengan {addr}")
    filename = conn.recv(1024).decode()
    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

    print(f"File '{filename}' berhasil diterima.")
    conn.close()
    s.close()

if __name__ == "__main__":
    receive_file()