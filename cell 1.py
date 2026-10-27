
import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started...")
print("Waiting for client...")

connection, address = server_socket.accept()
print("Client connected:", address)

while True:
    data = connection.recv(1024)

    if not data:
        break

    message = data.decode()
    print("Client:", message)

    if message.lower() == "exit":
        break

    connection.sendall(("Message received: " + message).encode())

connection.close()
server_socket.close()
print("Server closed.")

