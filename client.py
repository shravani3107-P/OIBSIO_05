import socket

client = socket.socket()
client.connect(("localhost", 5000))

while True:
    message = input("You: ")
    client.send(message.encode())

    reply = client.recv(1024).decode()
    print("User 1:", reply)
