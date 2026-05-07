import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print("Connected to", addr)

while True:
    message = conn.recv(1024).decode()
    print("User 2:", message)

    reply = input("You: ")
    conn.send(reply.encode())
