import threading
from typing import Any
import socket 
import random
import math

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_address=("0.0.0.0",8002)
s.bind(my_address)
s.listen()
connessione,address=s.accept()


def main():
    N = 97
    G = 44

    b = random.randint(2, N)
    print(f"b = {b}")

    B = (G**b) % N
    connessione.sendall(str(B).encode())
    A= int(connessione.recv(4096).decode())
    print(f"chiave = {(A**b) % N}")
s.close()


if __name__ == "__main__":
    main()