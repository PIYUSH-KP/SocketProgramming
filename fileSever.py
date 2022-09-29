import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)

def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server is listening...")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        filename = conn.recv(1024).decode("utf-8")
        print(f"[RECV] {filename} received.")
        file = open(filename,"w")
        conn.send(f"{filename} received.".encode("utf-8"))

        data = conn.recv(1024).decode("utf-8")
        print(f"[REC] File data received")
        file.write(data)
        conn.send("File data received. ".encode("utf-8"))

        file.close()
        conn.close()

        print(f"[DISCONNECTED] This {addr} disconnected")




if __name__ == "__main__":
    main()