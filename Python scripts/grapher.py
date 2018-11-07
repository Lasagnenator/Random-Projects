import numpy as np  
import matplotlib.pyplot as plt
import math
import cmath
import sys
import traceback

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()

while True:
    try:
        while True:
            formula = input('What equation? y = ')
            x_min = int(input('Minimum X: '))
            x_max = int(input('Largest X: '))
            step = input('Step size: ')
            graph(formula, range(x_min, x_max, step))
    except:
        input(sys.exc_info()[1])
