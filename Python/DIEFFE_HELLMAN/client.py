#192.168.1.130
import time
import socket #nativa
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #costruttore --> con questa riga ho istanziato il socket (creazione del socket)
server_address=("127.0.0.1",8002)
s.connect(server_address)
print("connesso")

def main():
    N = 97
    G = 44
    a = random.randint(2, N)
    print(f"a = {a}")

    B=int(s.recv(4096).decode())
    A = (G**a) % N
    s.sendall(str(A).encode(), server_address)
    print(f"chiave = {(B**a) % N}")
    
s.close()


if __name__ == "__main__":
    main()