import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to server.")

while True:
    message = input("Enter message: ")
    client_socket.sendall(message.encode())

    if message.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

client_socket.close()
print("Client disconnected.")
