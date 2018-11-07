from decimal import *
#-----------------
#contined fraction
#2 + 1/(a+a/(a1+a1/(a2+...))
#
#
#-----------------
def fraction(a, terms):
    na = terms
    mid = a
    ca = a
    
    for i in range(terms):
        ca = na
        mid = ca + Decimal(ca/mid)
        na = na - 1

    mid = 2 + Decimal(1/mid)
    return mid

x = int(input('How many terms: '))
getcontext().prec = x
y = x + 1
print(fraction(y, x))
input('Press enter to end: ')
