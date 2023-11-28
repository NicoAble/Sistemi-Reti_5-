import threading
from typing import Any
import socket 
import random
import math

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_address=("0.0.0.0",8000)
s.bind(my_address)
s.listen()
connessione,address=s.accept()

#creo valori per rsa
p = random.choice((307, 499, 929))
q = random.choice((173, 569, 997))
n = p * q

MCD = math.gcd(p-1, q-1)
m = int((p-1) * (q-1) / MCD)

for i in range (2, m-1):
    if(math.gcd(i, m)==1):
         c = i

for j in range (0, m-1):
    if( (c * j) % m == 1):
        d = j

print(f"p= {p}, q= {q}, m= {m}")

print(f"chiave privata = {d}")
print(f"chiave pubblica = {c}, n = {n}")

connessione.sendall(str(c).encode())
connessione.sendall(str(n).encode())

while True:
        data= connessione.recv(4096).decode()
        print(f"messaggio: {(int(data)**d)%n}")
        #c.sendall("ciao belo")