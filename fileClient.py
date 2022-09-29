import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    file = open("send.txt", "r")
    data = file.read()

    client.send("send.txt".encode(FORMAT))
    msg = client.recv(1024).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    client.send(data.encode(FORMAT))
    msg =  client.recv(1024).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    file.close()
    client.close()


if __name__ == "__main__":
    main()