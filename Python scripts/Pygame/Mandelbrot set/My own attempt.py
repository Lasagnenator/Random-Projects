import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp
import os

cwd = os.path.abspath(os.path.curdir)
config = open(os.path.join(cwd,"config.txt"), 'r')
exec(config.read())
mp.dps = precision

def mandelbrot(z):
    c=z
    for i in range(0,90):
        z = z*z+c
        if z.real>mp.mpf(2.0):
            return colourise(i)

def colourise(i):
    var = float(mp.sin(mp.radians(i)))
    return (var,var,var)

def plot(colours):
    plt.plot(REAL,IMAG,c=colours)

real = np.arange(mp.mpf(-2.0),mp.mpf(1.0),1/mp.mpf(precision))
imag = np.arange(mp.mpf(-1.0),mp.mpf(1.0),1/mp.mpf(precision))
REAL,IMAG = np.meshgrid(real,imag)
all_nums = REAL+(IMAG*1j)

colours = np.array(list(map(lambda x:np.array(list(map(lambda x:mandelbrot(mp.mpc(x)), x))), all_nums)))
plot(colours)
