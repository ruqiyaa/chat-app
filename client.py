import socket
import threading
import time

s = socket.create_connection(("127.0.0.1", 5000))

def receive():
    while True:
        data = s.recv(1024)
        if not data:
            print("Disconnected from server")
            break
        print(data.decode(), end="", flush=True)

threading.Thread(target=receive, daemon=True).start()

while True:
    text = input()
    s.sendall(text.encode() + b"\n")
    if text == "/quit":
        break

time.sleep(0.3)
s.close()