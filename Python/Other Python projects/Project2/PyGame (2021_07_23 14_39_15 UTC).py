import pygame

pygame.init()


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Screen")

x = 250
y = 250
vel = 10
width = 50
length = 50

run = True
while run:
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, length))
    pygame.display.update()


pygame.quit()





