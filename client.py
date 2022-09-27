import socket

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 1235

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,port))

    message = input("Enter message: ")
    server.send(bytes(message, "utf-8"))
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print(f"Server: {buffer}")