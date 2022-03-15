import pygame
import pygame_gui
import os
import tkinter


WIDTH = 900
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Window, my name is legend")


WHITE = (255, 255, 255)

REDISH_PINK = (230, 49, 80)

FPS = 65

spaceship_width = 55
spaceship_height = 40

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG, (spaceship_width, spaceship_height)), 90)

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, (spaceship_width, spaceship_height)), 270)

clock = pygame.time.Clock()


class Bird:
    pass



def draw_background():
    WIN.fill(WHITE)
    
    WIN.blit(YELLOW_SPACESHIP, (190, 100))

    WIN.blit(RED_SPACESHIP, (700, 100))

    pygame.display.update()


def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_background()

    pygame.quit()


if __name__ ==  "__main__":
    main()

