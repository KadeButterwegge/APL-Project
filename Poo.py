#Imports
import pygame
import time
pygame.init()

#Make Screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
FPS = 50

#Make ball
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (14, 14))
ballrect = ball.get_rect()
speed = 5
yspeed = 1



#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

def move(speedx, speedy, slow, window):
    while speedx > 0:
        ballrect.move_ip(1, 0)
        speedx -= slow

   
    
     
ballrect.move_ip(250, 50)


def level1():
    YObj = []
    XObj = []

    screen.fill((0, 0, 150))    
    global speed
    # Border for level 1
    grass = pygame.draw.rect(screen, (0, 160, 0), [100, 25, 300, 425], 0)
    #border = pygame.draw.rect(screen, (0, 0, 0), [96, 21, 304, 429], 6)
    Wall1 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 300, 5], 0)
    YObj.append(Wall1)

    Wall2 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 5, 425], 0)
    XObj.append(Wall2)

    Wall3 = pygame.draw.rect(screen, (0, 0, 0), [100, 450, 300, 5], 0)
    YObj.append(Wall3)

    Wall4 = pygame.draw.rect(screen, (0, 0, 0), [400, 25, 5, 430], 0)
    XObj.append(Wall4)

    if grass.contains(ballrect) == False:
        speed = -speed
    move(5, 0, 5, grass)



    createHole(250, 85)

running = True
while running:
    time.sleep(0.2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.flip()


    level1()
    screen.blit(ball, ballrect)
    
    



#def swing():
    
    

pygame.quit()