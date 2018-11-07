#fairy bread setup wizard.py (to be exe)
#C:\Users\Matthew\Desktop\Python\Python scripts\Pygame\Fairy bread; python setup.py build

import pygame
from pygame.locals import *
import os
import webbrowser
import time

pygame.init()

width = 300
height = 200

b1_x = width//2 - 64
b2_x = b1_x + 28
b3_x = b2_x + 30
b3_x_edge = b3_x + 70
b_y = height//2
b_y_edge = b_y + 20
p1_y = height//30
p2_y = p1_y+20
p_x = width//2-91

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('FairyBread Setup Wizard.exe')

bgcolour = (175, 175, 175)

clock = pygame.time.Clock()
p1 = pygame.image.load('p1.png')
p2 = pygame.image.load('p2.png')
b1 = pygame.image.load('b1.png') #Okay
b2 = pygame.image.load('b2.png') #Yes
b3 = pygame.image.load('b3.png') #Run Antivirus
game_display.fill(bgcolour)
game_display.blit(p1, (p_x, p1_y))
game_display.blit(b1, (b1_x, b_y))
game_display.blit(b3, (b3_x, b_y))
part2 = False

while True:
    mouse_down = pygame.mouse.get_pressed()[0]
    m_x, m_y = pygame.mouse.get_pos()
    on_button1 = (not part2) and (m_x>b1_x and m_x<b2_x) and (m_y>b_y and m_y < b_y_edge)
    #Okay
    on_button2 = part2 and (m_y>b_y and m_y < b_y_edge) and (m_x>b2_x and m_x<b3_x)
    #Yes
    on_button3 = (not part2) and (m_x>b3_x and m_x<b3_x_edge) and (m_y>b_y and m_y < b_y_edge)
    #Run Antivirus
    if mouse_down and on_button1:
        game_display.fill(bgcolour)
        game_display.blit(p2, (p_x, p2_y))
        game_display.blit(b2, (b2_x, b_y))
        part2 = True
    elif mouse_down and on_button2:
        os.system('start; C:\\\"Program Files\"\\\"Windows Defender\"\\\"MSASCui.exe\"')
        pygame.quit()
        #quit()
    elif mouse_down and on_button3:
        webbrowser.open('https://www.lingscars.com')
        time.sleep(0.5)
        os.system('start; C:\\\"Program Files\"\\\"Windows Defender\"\\\"MSASCui.exe\"')
        pygame.quit()
        #quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.quit()
            #quit()
            pygame.display.set_caption('No closing a virus!')
    
    pygame.event.clear()
    pygame.display.update()
    clock.tick(60)
    
