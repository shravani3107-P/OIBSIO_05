# Python Chat Server

## Description

This is a simple Python socket programming project that creates a server for chatting between two users on the same computer.

The server waits for a client connection, receives messages from the client, and sends replies back.

---

## Features

* Creates a server using Python sockets
* Waits for client connection
* Receives messages from client
* Sends replies back
* Simple command-line chat system

---

## Requirements

* Python 3.x
* No external libraries required

---

## How to Run

### Step 1: Save the file

Save the code as:

server.py

---

### Step 2: Run the server

Open terminal / command prompt and run:

python server.py

You will see:

Waiting for connection...

---

### Step 3: Run the client

Run the client file in another terminal window:

python client.py

---

## How It Works

1. Server starts and waits for connection
2. Client connects to server
3. Server receives client messages
4. Server sends reply
5. Chat continues until stopped manually

---

## Example Output

### Server Side

Waiting for connection...
Connected to ('127.0.0.1', 54321)

User 2: Hello
You: Hi

User 2: How are you?
You: Fine

---

## Code Explanation

### Create Socket

```python
server = socket.socket()
```

Creates a socket object.

### Bind Server

```python
server.bind(("localhost", 5000))
```

Binds server to local machine on port 5000.

### Listen for Connections

```python
server.listen(1)
```

Waits for one client connection.

### Accept Connection

```python
conn, addr = server.accept()
```

Accepts client connection.

### Receive Message

```python
message = conn.recv(1024).decode()
```

Receives message from client.

### Send Reply

```python
conn.send(reply.encode())
```

Sends reply to client.

---

## Common Errors

### SyntaxError

If you wrote:

Cimport socket

Correct it to:

import socket

---

### ConnectionRefusedError

This happens if client runs before server.

Solution:
Run server first, then client.

---

## Author

Python Socket Chat Application
