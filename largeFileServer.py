import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 5544
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #AF_INET - > IPV4, SOCK_STREAM -> TCP

    server.bind(ADDR)
    server.listen()
    print("[+] Listening...")

    conn, addr = server.accept()
    print(f"[+] Client connected from {ADDR[0]}:{ADDR[1]}")





