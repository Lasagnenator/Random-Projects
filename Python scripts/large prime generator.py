#large prime generator

from decimal import *

k = int(input('k = '))
offset = int(input('Offset = '))
while True:
    k2 = 2**k
    h = k2-offset
    n = h*(k2)+1
    a = 1
    z = 0.1
    if int((n-1)/Decimal(2))==(n-1)/Decimal(2):
        n1 = (n-1)//2
        
        while (not int(z)==z) and a<1000000:
            a += 1
            z = a**(n1)
            #print(z)
        if not a == 1000000:
            print('{}*2^{}+1'.format(h, k))
    
    k += 1
    
    
