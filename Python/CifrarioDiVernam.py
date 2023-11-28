Alfabeto={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'l':9, 'm':10, 
          'n':11, 'o':12, 'p':13, 'q':14, 'r':15, 's':16, 't':17, 'u':18, 'v':19, 'z':20}

def creaMessaggioCifrato(mex, key):
    mex=mex.lower()
    key=key.lower()
    messaggio_cifrato=[]
    mex_code=[]
    key_code=[]
    for l_mex in mex:
        for let,num in Alfabeto.items():
            if l_mex==let:
                mex_code.append(num)
            
    for l_key in key:
        for let,num in Alfabeto.items():
            if l_key==let:
                    key_code.append(num)
    
    #crazione messaggio cifrato
    for i, n1 in enumerate(mex_code):
        n1=n1+key_code[i]
        n1=n1%21
        #print(n1)
        messaggio_cifrato.append(n1)
    print(mex_code)
    return messaggio_cifrato, key_code


def decifra(key_code, mexCompl_code):
    #list dei numeri del messaggio di partenza
    dec=[]
    for i,n in enumerate(mexCompl_code):
        n=abs(n-key_code[i])
        n=n%21
        print(n)
        dec.append(n)
    parola=""
    for n1 in dec:
        for let,num in Alfabeto.items():
            if n1==num: parola+=let
    return parola

def main():
    mex, key_code= creaMessaggioCifrato("ciao", "itisdelpozzo")
    print(mex)
    mex_decifrato=decifra(key_code, mex)
    print(mex_decifrato)

if __name__ =="__main__": #"__" = Dunder
    main()