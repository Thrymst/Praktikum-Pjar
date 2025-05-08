import socket
import os

def send_file(filename):
    host = '127.0.0.1'
    port = 8000         

    s = socket.socket()
    s.connect((host, port))
    s.sendall(filename.encode())
    with open(filename, 'rb') as file:
        data = file.read()
        s.sendall(data)

    print(f"File '{filename}' berhasil dikirim.")
    s.close()

if __name__ == "__main__":
    filename = input("Masukkan nama file yang ingin dikirim: ")
    if os.path.exists(filename):
        send_file(filename)
    else:
        print("File tidak ditemukan.")