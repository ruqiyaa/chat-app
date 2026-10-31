import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Listening on port 5000...")

def handle_client(conn, addr):
    print("Connected:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received:", data)
        conn.sendall(data)
    conn.close()
    print("Disconnected:", addr)

while True:
    conn, addr = server.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    t.start()