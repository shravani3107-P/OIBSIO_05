# Client Chat Application

## Description

This Python program is a simple **client-side chat application** using the **socket module**. It connects to a server running on the same computer and allows two-way communication between the client and server.

---

## Features

* Connects to the server using localhost
* Sends messages to the server
* Receives replies from the server
* Simple command-line chat interface

---

## Requirements

* Python 3.x
* Server program must be running before starting the client

---

## How to Run

### Step 1: Start the Server

Run the server file first:

```bash
python server.py
```

You should see:

```bash
Waiting for connection...
```

---

### Step 2: Run the Client

Open another terminal or Python IDLE and run:

```bash
python client.py
```

---

## Code Explanation

### Import Socket Module

```python
import socket
```

Imports Python’s built-in networking module.

### Create Client Socket

```python
client = socket.socket()
```

Creates a client socket.

### Connect to Server

```python
client.connect(("localhost", 5000))
```

Connects to the server running on port **5000**.

### Send Message

```python
client.send(message.encode())
```

Sends the user’s message to the server.

### Receive Reply

```python
reply = client.recv(1024).decode()
```

Receives and decodes the server’s reply.

---

## Example Output

```bash
You: Hello
User 1: Hi

You: How are you?
User 1: Fine
```

---

## Common Errors

### ConnectionRefusedError

**Reason:** Server is not running.

**Solution:**
Run `server.py` before running `client.py`.

---

## Author

Shravani
