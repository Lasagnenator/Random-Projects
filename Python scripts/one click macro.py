#one-click macro

import pygame
import ctypes
import time
import sys

user32 = ctypes.windll.user32
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([200,200])
screen.fill([255,250,240])

def keytap(keycode):
    keycode = int(keycode)
    user32.keybd_event(keycode, 0, 0, 0)
    time.sleep(0.1)
    user32.keybd_event(keycode, 0, 2, 0)
def keydown(keycode):
    keycode = int(keycode)
    user32.keybd_event(keycode, 0, 0, 0)
def keyup(keycode):
    keycode = int(keycode)
    user32.keybd_event(keycode, 0, 2, 0)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
        elif event.type==pygame.MOUSEBUTTONDOWN:
            keydown(0x12)
            keytap(0x09)
            keyup(0x12)
            keydown(0x11)
            keytap(0x5a)
            time.sleep(0.1)
            keyup(0x11)
            #print('button clicked')
    clock.tick(30)
