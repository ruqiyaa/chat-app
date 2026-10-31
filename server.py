import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Listening on port 5000...")

clients = []
lock = threading.Lock()

def broadcast(data, sender):
    with lock:
        for client in clients:
            if client!= sender:
                client.sendall(data)

def handle_client(conn, addr):
    print("Connected:", addr)
    with lock:
        clients.append(conn)
        print("Clients online:", len(clients))
    broadcast(b"*** A client joined ***\n", conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data)
            broadcast(data, conn)
    finally:
        with lock:
            clients.remove(conn)
            print("Clients online:", len(clients))
        conn.close()
        print("Disconnected:", addr)
        broadcast(b"*** A client left ***\n", conn)

while True:
    conn, addr = server.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    t.start()