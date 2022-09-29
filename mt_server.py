import socket
import threading
import wikipedia

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
disconnectMessage = "!DISC"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == disconnectMessage:
            connected = False

        print(f"[{ADDR}] {msg}")
        #msg = f"Message Received: {msg}"
        msg = wikipedia.summary(msg, sentences = 1)
        conn.send(msg.encode(FORMAT))

    conn.close()


def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is Listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS] {threading.activeCount()-1}")


if __name__ == "__main__":
    main()
