import pygame

pygame.init()
size = (640, 480)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.display.flip()
