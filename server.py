import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Listening on port 5000...")

clients = {}
lock = threading.Lock()

def broadcast(data, sender_name):
    with lock:
        for name, client in clients.items():
            if name != sender_name:
                try:
                    client.sendall(data)
                except OSError:
                    pass
                

def handle_client(conn, addr):
    print("Connected:", addr)
    while True:
        conn.sendall(b"Enter your name: ")
        raw = conn.recv(1024)
        if not raw:
            conn.close()
            return
        name = raw.decode().strip()
        if not name:
            conn.sendall(b"Name cannot be empty.\n")
            continue
        with lock:
            taken = name in clients
            if not taken:
                clients[name] = conn
                print("Clients online: ", len(clients))
        if not taken:
            break
        conn.sendall(b"Name exists, try another.\n")

   
    broadcast(f"*** {name} joined ***\n".encode(), name)
    try:
        buffer = b""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            buffer += chunk
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                line = line.strip()
                if not line:
                    continue
                if line == b"/quit":
                    conn.sendall(b"Goodbye!\n")
                    return
                print("Received:", line)
                broadcast(f"[{name}]".encode() + line + b"\n", name)

    except OSError:
        pass
    finally:
        with lock:
            del clients[name]
            print("Clients online:", len(clients))
        conn.close()
        print("Disconnected:", addr)
        broadcast(f"*** {name} left ***\n".encode(), name)

while True:
    conn, addr = server.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    t.start()