#Integral solver

import numpy as np
import math

n = 99999

while True:
    formula = (input('Equation y = ')).lower()
    up = float(input('Upper limit: '))
    down = float(input('lower limit: '))
    steps = n*(abs(up)+abs(down))
    #steps = (up*n)-(down*n)
    step_size = (up-down)/steps
    #nums = np.arange(0, steps, 1)
    assert step_size > 0
    x = np.arange(down, up, step_size)
    y = eval(formula)
    y *= step_size
    y = y.tolist()
    ans = sum(y)
    #print(ans)
    print(round(ans, 4))
