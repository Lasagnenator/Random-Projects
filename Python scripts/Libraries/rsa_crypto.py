"""
RSA crypto
Generates key pairs from two numbers
Encrypts integers using a publickey
Decrypts inegers using a private key
Can convert string to int list to be encrypted
Can convert int list to readable string
"""
def genkeypair(p, q):
    """RSA generation of key pairs from two numbers.
MUST USE ONLY PRIME NUMBERS OR KEYS WILL BE INACCURATE"""
    import math
    from datetime import datetime
    start = datetime.now()
    n = p*q
    pubkey = 0
    prvkey = 0
    print('N:', n)
    totient = (p-1)*(q-1)
    for e in range(q, totient):     #computes public key exponent
        if math.gcd(e, totient) == 1:
            pubkey = e
            break

    print('Pubkey computed in:', str(datetime.now()-start))
    print('Public key:', pubkey)
    sqrtn = math.sqrt(n)

    for d in range(int(sqrtn), n):     #computes private key exponent
        if (d*e)%totient == 1%totient:
            prvkey = d
            break

    start1 = datetime.now()
    if (pubkey == 0) or (prvkey == 0):
        raise ValueError('No combinations found.')
    
    print('Prvkey computed in:', str(datetime.now()-start1))
    print('Private key:', prvkey)
    print('Total computation time:', datetime.now()-start)

"""RSA encryption using a public key"""
def encrypt(message, pubkey, n):
    from datetime import datetime
    start = datetime.now()
    m = message
    e = pubkey
    c = (m**e)%n
    #c = (exp(m, e))%n
    print('Encrypted in:', datetime.now()-start)
    return c

"""RSA decryption using a private key"""
def decrypt(encrypted, prvkey, n):
    from datetime import datetime
    start = datetime.now()
    c = int(encrypted)
    d = int(prvkey)
    #m = (c**d)%n
    m = (exp(c,d))%n
    print('Decrypted in:', datetime.now()-start)
    return m

"""Exponential by squaring used in encrypting and decrypting messages"""
def exp(x, n):
    if n<0:
        return exp(1/x, 0-n)
    if n == 0:
        return 1
    if n ==1:
        return x
    if n%2 == 0:
        return exp(x*x, n/2)
    if n%2 == 1:
        return (x*exp(x*x, (n-1)/2))
    """
    if n%2 == 1:
        return int(x*(x*x)**((n-1)/2))
    if n%2 == 0:
        return int((x*x)**(n/2))
    """

def str2int(string):
    """Converts string to int list"""
    s = string
    #x = int(''.join(str(ord(c)) for c in s))
    x = [ord(c) for c in s]
    return x
    
def int2str(integer):
    """Converts int list to string""" 
    i = integer
    x = ''.join(chr(c) for c in i)
    return x
