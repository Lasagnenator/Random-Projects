#Block cipher
#Feistel cipher
import sys
import hashlib as h

def f(R, K):
    #Irreversible function
    #R is integer
    #K is character
    K = ord(K)
    size = len(bin(R)[2:])
    #must return of the same size (bits) as input
    var = str(K)+str(R)
    return int(h.sha512(var.encode()).hexdigest(),16)^int('1'*size,2)

def xor(x, y):
    return x^y


def Feistel_enc(L0, R0, K):
    for i in range(0,len(K)):
        L_next = R0
        R_next = xor(L0, f(R0, K[i]))
        L0 = L_next
        R0 = R_next
    return R0,L0

def Feistel_dec(R0, L0, K):
    "K is the same as enc"
    K = K[::-1]
    for i in range(0,len(K)):
        R_next = L0
        L_next = xor(R0, f(L0, K[i]))
        R0 = R_next
        L0 = L_next
    return L0,R0

def split(string):
    half = len(string)//2
    return string[:half], string[half:]

def message2int(message):
    fin = []
    for char in message:
        value = str(ord(char))
        adjust = 3-len(value)
        fin.append(('0'*adjust)+value)
    fins = "".join(fin)
    fini = int(fins)
    return fini

def int2message(integer):
    s = str(integer)
    temp = ''
    fin = []
    counter = 0
    finl = [s[i:i+3] for i in range(0, len(s), 3)]
    if len(finl[-1])<3:
        s = len(finl)*"0" + s
        finl = [s[i:i+3] for i in range(0, len(s), 3)]
    finl = list(map(int,finl))
    fin = list(map(chr,finl))
    return "".join(fin)

def testingmain(args):
    if 'enc' in args:
        enc = True
        dec=False
    elif 'dec' in args:
        dec = True
        enc=False

    K = args[2]
    if enc:
        message = args[1]
        m1,m2 = split(message)
        m1i = message2int(m1)
        m2i = message2int(m2)
        l,r = Feistel_enc(m1i,m2i,K)
        #cipher = int2message(int(str(l)+str(r)))
        cipher = str(l)+str(r)
        print("Ciphertext: {}".format(cipher))
    elif dec:
        cipher = args[1]
        c1,c2 = split(cipher)
        #c1i = message2int(c1)
        #c2i = message2int(c2)
        c1i = int(c1)
        c2i = int(c2)
        l,r = Feistel_dec(c1i,c2i,K)
        plain = int2message(int(str(l)+str(r)))
        print("Plaintext: {}".format(plain))
    else:
        print("Something went wrong. got {}".format(args))

def main(args):
    if 'enc' in args:
        enc = True
        dec=False
    elif 'dec' in args:
        dec = True
        enc=False

    K = args[2]
    if enc:
        message = args[1]
        m1,m2 = split(message)
        m1i = message2int(m1)
        m2i = message2int(m2)
        l,r = Feistel_enc(m1i,m2i,K)
        #cipher = int2message(int(str(l)+str(r)))
        cipher = str(l)+str(r)
        print("Ciphertext:\n\n{}".format(cipher))
    elif dec:
        cipher = args[1]
        c1,c2 = split(cipher)
        #c1i = message2int(c1)
        #c2i = message2int(c2)
        c1i = int(c1)
        c2i = int(c2)
        l,r = Feistel_dec(c1i,c2i,K)
        plain = int2message(int(str(l)+str(r)))
        print("Plaintext:\n\n{}".format(plain))
    else:
        print("Something went wrong. got {}".format(args))

def helping():
    print("Please use command line instead")
    print("""
Syntax:
python <path> enc PLAINTEXT KEY
    Encryption
python <path> dec CIPHERTEXT KEY
    Decryption
""")
    input()
        
if __name__ == "__main__":
    args = sys.argv
    if len(args)<3:
        helping()
        sys.exit()
    #print(args)
    args = args[1:]
    main(args)
    sys.exit()
