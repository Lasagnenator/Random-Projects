#Polynomial solver of arbitrary order
#Created by Matthew Richards

import math
import cmath
import sys

def sqrt(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return cmath.sqrt(x)

def factorise(x, y):
    a = gcd(x, y)
    x /= a
    y /= a
    return a, int(x), int(y)

def ismonic(a):
    if a == 1:
        return True
    else:
        return False

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def root(x, r):
    return x**(1/r)

def power(x, n):
    if x<0:
        return -(abs(x)**n)
    elif x>0:
        return x**n
    else:
        return 0

def derivative(poly):
    #poly must be: 'ax^n+bx^'
    poly = poly.split('+')
    a_list = []
    n_list = []
    deriv = []
    for item in poly: #ax^n
        try:
            a = int(item[:1])
        except ValueError:
            a = int(item[0])
        try:
            n = int(item[1:])
        except ValueError:
            n = int(item[-1])
        a_list.append(a)
        n_list.append(n)
    i = 0
    for item_a in a_list:
        item_n = n_list[i]
        deriv.append(str(item_a)+'*'+str(item_n)+'*(x**('+str(item_n)+'-1))')
        i += 1
    result = "+".join(deriv)
    return result

def Newton(func, deriv, xn):
    x = xn
    f = eval(func)
    d = eval(deriv)
    xn1 = xn+(f/d)
    return xn1

def findroot(func, guess):
    """Func is a string, guess is a number"""
    deriv = derivative(func)
    prev = Newton(func, deriv, guess)
    new = Newton(func, deriv, prev)
    while not math.isclose(prev, new, rel_tol=1e-11):
        prev = new
        new = Newton(func, deriv, prev)
    return new
        

print('DOES NOT FACTORISE, ONLY SOLVES EQUATIONS TO 10 SIGNIFICANT FIGURES')
try:
    while True:
        order = int(input('Order (1-4): '))
        if order == 1:
            print('Form: ax+b=0')
            a = float(input('a = '))
            b = float(input('b = '))
            r1 = (-b)/a
            print('Equation: {}x+{}=0'.format(a, b))
            print('Root: {}\n'.format(r1))
        elif order == 2:
            print('Form: ax^2+bx+c=0')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            p1 = sqrt((b*b)-(4*a*c))
            r1 = (-b+p1)/(2*a)
            r2 = (-b-p1)/(2*a)
            print('Equation: {}x^2+{}x+{}=0'.format(a, b, c))
            print('Roots: {}, {}\n'.format(r1, r2))
        elif order == 3:
            print('Form: ax^3+bx^2+cx+d=0')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            d = float(input('d = '))
            p1 = (((-b*b*b)/(27*a*a*a))+((b*c)/(6*a*a))-((d)/(2*a)))
            p2 = sqrt(p1**2+((c/(3*a))-((b*b)/(9*a*a)))**3)
            p3 = b/(3*a)
            r1 = root(p1+p2, 3)+root(p1-p2, 3) - p3
            r2 = root(p1+p2, 3)+root(p1+p1, 3) - p3
            r3 = root(p1-p2, 3)+root(p1-p2, 3) - p3
            print('Equation: {}x^3+{}x^2+{}x+{}=0'.format(a, b, c, d))
            print('Roots: {}, {}, {}\n'.format(r1, r2, r3))
        elif order == 4:
            print('Form: ax^4+bx^3+cx^2+dx+e=0')
            div = float(input('a = '))
            a1 = float(input('b = '))
            b1 = float(input('c = '))
            c1 = float(input('d = '))
            d1 = float(input('e = '))
            a = a1/div
            b = b1/div
            c = c1/div
            d = d1/div
            a4 = (-a)/4
            cube_2 = 1.25992104989487*(b*b-(3*a*c)+(12*d))
            b2cube = (2*b**3-(9*a*b*c)+(27*c*c)+(27*a*a*d)-(72*b*d)+sqrt(-4*(b*b-(3*a*c)+(12*d))**3+(2*b**3-(9*a*b*c)+(27*c*c)+(27*a*a*d)-(72*b*d))**2))
            p1 = ((sqrt(((a*a)/4)-(2*b/3)+(cube_2/3*root(b2cube, 3)))+root((b2cube/(54)), 3))/2)
            p2 = (((a*a)/2)-((4*b)/3)-(cube_2/(3*root(b2cube, 3)))-root((b2cube)/54, 3))
            p3 = (-(a*a*a)+(4*a*b)-(8*c))/(4*sqrt(((a*a)/4)-(2*b/3)+(cube_2/3*root(b2cube, 3)))+root((b2cube/54), 3))
            r1 = a4 - p1 - (sqrt(p2 - p3)/2)
            r2 = a4 - p1 + (sqrt(p2 - p3)/2)
            r3 = a4 + p1 - (sqrt(p2 + p3)/2)
            r4 = a4 + p1 + (sqrt(p2 + p3)/2)
            print('Equation: {}x^4+{}x^3+{}x^2+{}x+{}'.format(div,a1,b1,c1,d1))
            print('Roots: {}, {}, {}, {}\n'.format(r1, r2, r3, r4))
        elif order == 5:
            print('Form: ax^5+bx^4+cx^3+dx^2+ex+f=0')
            div = int(input('a = '))
            a = int(input('b = '))/div
            b = int(input('c = '))/div
            c = int(input('d = '))/div
            d = int(input('e = '))/div
            e = int(input('f = '))/div
            if a==0 and b==0 and c==0 and d==0:
                r1 = root(-e, 5)
                r2 = -root(e, 5)
                r3 = -((-1)**(2/5)*root(e, 5))
                r4 = ((-1)**(3/5)*root(e, 5))
                r5 = -((-1)**(4/5)*root(e, 5))
                print('Equation: x^5+{} = 0'.format(e))
                print('Roots: {}, {}, {}, {}, {}'.format(r1,r2,r3,r4,r5))
            elif True:
                deriv = derivative('0x^5+{}x^4+{}x^3+{}x^2+{}x^1+{}x^0'.format(a,b,c,d,e))
            else:
                print('Polynomial not solvable by algebraic means')
except KeyboardInterrupt:
    input('Keyboard Interrupt\n')
except:
    input('Caught exception: {}\n'.format(sys.exc_info()[1]))
finally:
    print('Ending program. Written by Matthew Richards')
