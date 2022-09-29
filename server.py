import socket

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 1235
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Conection Established - {address[0]}:{address[1]}")

        message = client.recv(1024)
        message = message.decode("utf-8")
        message = message.upper()
        client.send(bytes(message,"utf-8"))
        #print(message)
        client.close()
