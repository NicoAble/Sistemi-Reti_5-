import socket
import random
import math
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",8000)
s.connect(server_address)
print("connesso")

c=int(s.recv(4096).decode())
print(f"chiave pubblica {c}")
n=int(s.recv(4096).decode())
print(f"n = {n}")

while True:
    a = int(input("inserisci un numero: "))
    print(f"messaggio = {a}")
    b= str((a ** c) % n)
    s.sendall(b.encode())
    
s.close()