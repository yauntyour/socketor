import socket
import time

HOST = "127.0.0.1"
PORT = 8080

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = bytes(time.asctime(time.localtime()).encode()) + b"\0"
        print(f"Sending: {message}")
        s.sendall(message)

        data = s.recv(1024)
        print(f"Received: {data}")
    # time.sleep(0.5)
