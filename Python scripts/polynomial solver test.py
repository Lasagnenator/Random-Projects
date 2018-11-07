#Polynomial solver

import math
from sympy import solve, symbols, Eq, init_printing
import sys

#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
x = symbols('x')
init_printing(use_unicode=False)

letter_dict = {1:'a',
               2:'b',
               3:'c',
               4:'d',
               5:'e',
               6:'f',
               7:'g',
               8:'h',
               9:'i',
               10:'j',
               11:'k',
               12:'l',
               13:'m',
               14:'n',
               15:'o',
               16:'p',
               17:'q',
               18:'r',
               19:'s',
               20:'t',
               21:'u',
               22:'v',
               23:'w',
               24:'x',
               25:'y',
               26:'z'}
print('a*(x^0)+b*(x^1)+c*(x^2)... = 0')
order = (abs(int(input('Order (max=26): ')))%26)+1
for i in range(0,order):
    equation = 0
    exec("{} = int(input('{} = '))".format(letter_dict[i+1], letter_dict[i+1]))
    exec("equation += {}*(x**{})".format(letter_dict[i+1], i))

solutions = solve(Eq(equation, 0))
print("Number of solutions: {}".format(len(solutions)))
print("solutions:")
for solution in solutions:
    print(str(solution))
input('End.')
    
