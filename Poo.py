#Imports
import pygame
pygame.init()

#Make Screen
screen = pygame.display.set_mode([500, 500])

#Make ball
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (14, 14))
ballrect = ball.get_rect()



#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

def move(x, y):
    ballrect.move_ip(x, y)
move(50, 50)
print(ball.get_rect())
print(ballrect)

def level1():
    screen.fill((0, 0, 150))    

    # Border for level 1
    grass = pygame.draw.rect(screen, (0, 160, 0), [100, 25, 300, 425], 0)
    border = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 300, 425], 4)
    #print(ball.get_rect())
    #print(grass.contains(ball.get_rect()))
    #print(border.contains(ballrect))

    # Triangle Obstacle for level 1
    #pygame.draw.line(screen, (0, 0, 0), (175, 150), (250, 200), 4)
    #pygame.draw.line(screen, (0, 0, 0), (250, 200), (325, 150), 4)
    #pygame.draw.line(screen, (0, 0, 0), (175, 150), (325, 150), 4)

    # Left Side Triange for level 1
    #pygame.draw.line(screen, (0, 0, 0), (100, 300), (175, 250), 4)
    #pygame.draw.line(screen, (0, 0, 0), (100, 100), (175, 250), 4)

    # Right Side Triangle for level 1
    #pygame.draw.line(screen, (0, 0, 0), (400, 300), (325, 250), 4)
    #pygame.draw.line(screen, (0, 0, 0), (400, 100), (325, 250), 4)

    createHole(250, 85)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 160, 0))
    level1()
    screen.blit(ball, ballrect)
    
    

    pygame.display.flip()


#def swing():
    
    

pygame.quit()