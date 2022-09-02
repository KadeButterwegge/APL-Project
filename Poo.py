import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 160, 0))

    # Border for level 1
    pygame.draw.line(screen, (0, 0, 0), (100, 25), (100, 475), 4)
    pygame.draw.line(screen, (0, 0, 0), (100, 25), (400, 25), 4)
    pygame.draw.line(screen, (0, 0, 0), (100, 475), (400, 475), 4)
    pygame.draw.line(screen, (0, 0, 0), (400, 25), (400, 475), 4)

    # Triangle Obstacle for level 1
    pygame.draw.line(screen, (0, 0, 0), (200, 150), (250, 200), 4)
    pygame.draw.line(screen, (0, 0, 0), (250, 200), (300, 150), 4)
    pygame.draw.line(screen, (0, 0, 0), (200, 150), (250, 150), 4)

    pygame.display.flip()

    def level1():
        screen.fill((0, 160, 0))


pygame.quit()