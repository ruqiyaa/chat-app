import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Listening on port 5000...")

conn, addr = server.accept()
print("Connected:", addr)

#receive and echo
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data)
    conn.sendall(data)

conn.close()
print("Disconnected:", addr)