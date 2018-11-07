#Cubic Equation solver

import math
import cmath

def factors(x):
    nums = []
    for i in range(1, x+1):
        if i%x==0:
            nums.append(i)
    return nums

while True:
    print("\nForm: ax³+bx²+cx+d=0")
    a = int(input('a = '))
    b = int(input('a = '))
    c = int(input('a = '))
    d = int(input('a = '))
    pass
