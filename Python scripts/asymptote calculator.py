#asymptote calculator
#https://en.wikipedia.org/wiki/Asymptote#General_computation_of_oblique_asymptotes_for_functions

"""
This calculator cannot compute vertical asymptotes or curved asymptotes.
It computes oblique asymptotes based on the algorithm given on Wikipedia.
"""

from sympy import *
from sympy.abc import x
import sys
init_printing(use_unicode=False)

def find_asymptote(expr):
    try:
        y = sympify(expr)
        m = limit(y/x, x, oo)
        if not m.is_number:
            return None
        p = limit(y-m*x, x, oo)
        y = Symbol('y')
        ans = simplify(Eq(y, m*x+p))
        if ans ==False:
            y = sympify(expr)
            m = limit(y/x, x, -oo)
            if not m.is_number:
                return None
            p = limit(y-m*x, x, -oo)
            y = Symbol('y')
            ans = simplify(Eq(y, m*x+p))
        return ans
    except NotImplementedError:
        return "Specified function has not been implemented yet."

def main(args):
    expr = args[1]
    print("Asymptote:")
    pprint(find_asymptote(expr))
    return 0

if __name__=="__main__":
    args = sys.argv
    shell = False
    if len(args)==1:
        args.append(input("Equation : y = "))
        shell = True
    main(args)
    if shell:
        input()

