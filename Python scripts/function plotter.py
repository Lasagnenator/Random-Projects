#function grapher

import matplotlib.pyplot as plt
import numpy as np
import scipy.special
import numba as nb

pi = np.pi
e = np.e
tau = pi*2

precision = 1000

#@nb.jit(nb.float64(nb.float64), cache=True)
def f(x):
    return x**2-6*x+5

xlim = [-5, 5]
ylim = [-5, 5]
fig = plt.figure()
ax = fig.gca()
fv = np.vectorize(f)

x = np.linspace(xlim[0], xlim[1], precision, endpoint=True)
y = fv(x)
y[y<ylim[0]]= "nan"
y[y>ylim[1]]= "nan"
ax.plot(x,y, 'b-')
ax.autoscale(enable=False)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.grid(True)
plt.pause(0.05)

while True:
    ax.clear()
    x = np.linspace(xlim[0], xlim[1], precision, endpoint=True)
    y = fv(x)
    x.append(x)
    y[y<ylim[0]]= "nan"
    y[y>ylim[1]]= "nan"
    ax.plot(x,y, 'b-')
    ax.autoscale(enable=False)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(True)
    plt.pause(0.05)
    xold = xlim
    yold = ylim
    xlim = ax.get_xlim() #x
    ylim = ax.get_ylim() #y
