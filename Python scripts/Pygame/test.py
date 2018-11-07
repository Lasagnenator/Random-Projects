import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
black = (0,0,0)
white = (255,255,255)
while True:
    screen.fill(white)
    pygame.draw.circle(screen, (255, 0, 0), (100, 200), 10, 0)
    pygame.display.update()
    screen.fill(black)
    pygame.draw.circle(screen, (255, 0, 0), (100, 200), 10, 0)
    pygame.display.update()
