#Tetris
import pygame
from pygame.locals import *

pygame.init()
font = pygame.font.SysFont('consolas', 16)
bg_colour = (175, 175, 175)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
#falling area = 300x500 with 10 pixel padding
#falling rect = ((200, 50), (200, 550), (500, 50), (500, 550)) #tl, bl, tr, br
#text area = 150
#text rect = ((), (), (), ())#tl, bl, tr, br
pygame.display.set_caption('Tetris by Matthew Richards', 'Tetris.exe')

gameisplaying = 1
screen.fill(bg_colour)

def show_text(pos, text, colour):
    textimg = font.render(text, 1, colour, bg_colour)
    screen.blit(textimg, pos)
def draw_block(pos, colour):
    #Block = 30x30
    block = pygme.Rect((pos[0]-15, pos[1]+15), (pos[0]-15, pos[1]-15), (pos[0]+15, pos[1]+15), (pos[0]+15, pos[1]-15)) #topleft, bottomleft, topright, bottomeright
    pygame.draw.rect(screen, colour, block)
    return block
def game_end():
    fill_area = pygame.Rect((200, 50), (200, 550), (500, 50), (500, 550)) #topleft, bottomleft, topright, bottomeright
    while tuple(screen.get_at((200, 50))) != (0,0,0,255):
        screen.fill((0,0,0), fill_area, pygame.BLEND_ADD)


###CONTROLS###
print('Left arrow   Move current block left')
print('Right arrow  Move current block right')
print('Up arrow     Rotate current block')
print('Down arrow   Move current block down')
print('Space        Drop current block')

while gameisplaying:
    clock.tick(10) #limits the while loop to 10 times a second
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_SPACE:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
        elif event.type = pygame.QUIT:
            gameisplaying = False
            
