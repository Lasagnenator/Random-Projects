import mpmath
import cmath

ctx = mpmath.fp
#ctx = mpmath.mp

ITERATIONS = 50
POINTS = 1000000
ESCAPE_RADIUS = 2

# Full plot
RE = [-2.5, 1.5]
IM = [-1.5, 1.5]

# A pretty subplot
#RE = [-0.96, -0.80]
#IM = [-0.35, -0.2]

def mandelbrot(z):
    c = z
    for i in range(ITERATIONS):
        zprev = z
        z = z*z + c
        if abs(z) > ESCAPE_RADIUS:
            return ctx.exp(1j*(i + 1 - ctx.log(ctx.log(abs(z)))/ctx.log(2)))
    return 0

ctx.cplot(mandelbrot, RE, IM, points=POINTS, verbose=1)