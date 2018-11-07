#Symbolab in Python
from __future__ import division
from sympy import *
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pygame
import os

global helper

pygame.init()
screen = pygame.display.set_mode((0,0))
bg_colour = (175,175,175)
screen.fill(bg_colour)
pygame.display.set_caption('Symbolab by Matthew Richards', 'Symbolab.exe')
init_printing(use_unicode=True)
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 16)

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

def showtext(pos, text, colour):
    textimg = font.render(text, 1, colour, bg_colour)
    screen.blit(textimg, pos)

def drawmath(latex, pos):
    plt.figtext(0.5, 0.5, r'${}$'.format(latex), size='xx-large')
    plt.savefig('math.png')
    math = pygame.image.load('math.png')
    screen.blit(math, pos)
    os.remove('math.png')

font_colour = (0,0,0)
def multiLineSurface(string, rect, justification=0):
    finalLines = []
    requestedLines = string.splitlines()
    for requestedLine in requestedLines:
        if font.size(requestedLine)[0] > rect.width:
            words = requestedLine.split(' ')
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise Exception("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulatedLine = ""
            for word in words:
                testLine = accumulatedLine + word + " "
                # Build the line while the words fit.
                if font.size(testLine)[0] < rect.width:
                    accumulatedLine = testLine
                else:
                    finalLines.append(accumulatedLine)
                    accumulatedLine = word + " "
            finalLines.append(accumulatedLine)
        else:
            finalLines.append(requestedLine)

    # Let's try to write the text out on the surface.
    surface = pygame.Surface(rect.size)
    surface.fill(bg_colour)
    accumulatedHeight = 0
    for line in finalLines:
        if accumulatedHeight + font.size(line)[1] >= rect.height:
            raise Exception("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempSurface = font.render(line, 1, font_colour)
        if justification == 0:
            surface.blit(tempSurface, (0, accumulatedHeight))
        elif justification == 1:
            surface.blit(tempSurface, ((rect.width - tempSurface.get_width()) / 2, accumulatedHeight))
        elif justification == 2:
            surface.blit(tempSurface, (rect.width - tempSurface.get_width(), accumulatedHeight))
        else:
            raise Exception("Invalid justification argument: " + str(justification))
        accumulatedHeight += font.size(line)[1]
    return surface

def handle_key(key):
    global helper
    keys = pygame.key.get_pressed()
    if key != None:
        print(key)
        #print(type(key))
        #key = ('{}'.format(pygame.key.name(key))).lower()
        key = key.unicode
        print(key)
    if key == 'h':
        helper = 1
    elif key == '\x1b': #Escape
        pygame.quit()
        sys.exit()
    elif key == '\x1b' and helper == 1:
        helper = 0
    elif key == '(':
        pass
    elif key == ')':
        pass
    elif key == pygame.K_RETURN:
        pass
    elif key == pygame.K_h:
        helper = 1

try:
    while True:
        clock.tick(10)
        if pygame.key.get_focused():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key_pressed = event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                else:
                    key_pressed = None
                #print(type(key_pressed))
                handle_key(key_pressed)
            if pygame.mouse.get_pressed()[0]:
                (cur_x, cur_y) = pygame.mouse.get_pos()
            pygame.event.clear()
        helper = 0
        simp = 1
        if helper == 1:
            rect = pygame.Rect(1000, 800, 1000, 800)
            rect.center = (500,400)
            surface = multiLineSurface("""All variables are assumed to be complex to handle everything.
pi: pi
tau: tau
infinity = oo
exp(x) = exp(x)
sin(x) = sin(x)
cos(x) = cos(x)
...
log(x) = log(x, base)
Instead of doing x=y you must do Eq(x ,y) or x-y
Matrix() = Matrix([[a,b,c,..], [], ...], [], [], ...)
    The outermost square brackets are collumns, then inside is the next dimension
Derivative(f) = diff(f, variable, order)
Summation(f, lower, upper) = Sum(f, (variable, lower, upper))
Integrate(f) = integrate(f, variable, lower, upper)
    You can omit lower and upper for an indefinite integral
Limit notation: limit(f, variable, a, sign)
    e.g as variable approaches a, what is the value of f? sign is sign of a e.g. sign = + or -""", rect)
            screen.blit(surface, (0,0))
        elif simp == 10:
            to_simp = (input('Input equation: '))
            pprint(S(to_simp))
            simped = simplify(cancel(factor(to_simp)))
            print('{} = {}'.format(to_simp, simped))
            pprint(simped, use_unicode=False)
            #print('{}'.format(simped))
        elif not(simp<=10 and simp>=1):
            input('Did not understand input. Make sure that input is between 1 and 10')
        pygame.display.update()
except Exception as e:
    print('Caught exception: {}'.format(e))
except BaseException as e:
    print('Caught base exception: {}'.format(e))
finally:
    input('Exiting')
    pygame.quit()
    print('Written by Matthew Richards')
    sys.exit()
