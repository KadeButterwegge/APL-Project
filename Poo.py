#Imports
import pygame
pygame.init()

#Make Screen
screen = pygame.display.set_mode([500, 500])

#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

def level1():
    screen.fill((0, 160, 0))

    # Border for level 1
    pygame.draw.line(screen, (0, 0, 0), (100, 25), (100, 475), 4)
    pygame.draw.line(screen, (0, 0, 0), (100, 25), (400, 25), 4)
    pygame.draw.line(screen, (0, 0, 0), (100, 475), (400, 475), 4)
    pygame.draw.line(screen, (0, 0, 0), (400, 25), (400, 475), 4)

    # Triangle Obstacle for level 1
    pygame.draw.line(screen, (0, 0, 0), (175, 150), (250, 200), 4)
    pygame.draw.line(screen, (0, 0, 0), (250, 200), (325, 150), 4)
    pygame.draw.line(screen, (0, 0, 0), (175, 150), (325, 150), 4)

    # Left Side Triange for level 1
    pygame.draw.line(screen, (0, 0, 0), (100, 300), (175, 250), 4)
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (175, 250), 4)

    # Right Side Triangle for level 1
    pygame.draw.line(screen, (0, 0, 0), (400, 300), (325, 250), 4)
    pygame.draw.line(screen, (0, 0, 0), (400, 100), (325, 250), 4)

    createHole(250, 85)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 160, 0))
    level1()

    pygame.display.flip()

    

pygame.quit()