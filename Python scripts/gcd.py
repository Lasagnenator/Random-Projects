#GCD
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

while True:
    a = int(input('A = '))
    b = int(input('B = '))
    print('GCD = {}'.format(gcd(a, b)))
