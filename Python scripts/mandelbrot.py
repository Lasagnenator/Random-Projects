#computes the mandelbrot set and atempts to draw it.
import turtle
import math

def iterc(c):
    iters = 0
    z = 0+0j
    while iters < 16 and math.hypot(z.real, z.imag)<2:
        z = z*z+c
        iters += 1
    return iters

def getcolour(pos):
    return 'red'
    x = iterc(pos)
    colour = ''
    if x == 16:
        colour = 'black'
    elif x == 15:
        colour = 'gray93'
    elif x == 14:
        colour = 'gray87'
    elif x == 13:
        colour = 'gray81'
    elif x == 12:
        colour = 'gray75'
    elif x == 11:
        colour = 'gray68'
    elif x == 10:
        colour = 'gray62'
    elif x == 9:
        colour = 'gray56'
    elif x == 8:
        colour = 'gray50'
    elif x == 7:
        colour = 'gray43'
    elif x == 6:
        colour = 'gray37'
    elif x == 5:
        colour = 'gray31'
    elif x == 4:
        colour = 'gray25'
    elif x == 3:
        colour = 'gray18'
    elif x == 2:
        colour = 'gray12'
    elif x == 1:
        colour = 'gray6'
    elif x == 0:
        colour = 'white'
    return colour

def drawpixel(x, y, colour):
    turtle.goto(x, y)
    turtle.dot(1, colour)
    
def main():
    screen = turtle.Screen()
    screen.title('Mandelbrot Set')
    screen.bgcolor('#22ccaa')

    width = int(screen.numinput('Screen size', 'What width?', 600, 100, 20000))
    height = int(screen.numinput('Screen size', 'What height?', 600, 100, 10000))
    screen.setworldcoordinates(-width // 2, -height // 2, width // 2, height // 2)
    screen.tracer(0, 0)

    radius = 2

    turtle.penup()
    turtle.hideturtle()
    turtle.speed('fastest')

    x, y = -width // 2, -height // 2
    turtle.goto(x, y)

    while y < (height // 2):

        while x < (width // 2):

            newx = x / (width // 2) * radius
            newy = y / (width // 2) * radius
            mpos = newx + newy * 1j
            drawpixel(x, y, getcolour(mpos))
            x += 1

        x, y = -width // 2, y + 1
        screen.update()
        
main()
