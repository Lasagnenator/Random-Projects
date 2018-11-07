#Chemical equation balancer
import pygame_textinput as textinput
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

bg = (255,255,255)
clock = pygame.time.Clock()

def main():
    equation_input = textinput.TextInput(font_family="consolas")
    second_input = textinput.TextInput(font_family="consolas")
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                print('clicked')
                pos = pygame.mouse.get_pos()
                if equation_input.get_surface().get_bounding_rect().collidepoint(pos):
                    equation_input.toggle_active()
                    print('toggled')
        equation_input.update(events)
        second_input.update(events)
        screen.fill(bg)
        screen.blit(equation_input.get_surface(), (10,10))
        screen.blit(second_input.get_surface(), (10,40))
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
