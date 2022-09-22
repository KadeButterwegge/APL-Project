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
xspeed = 0
yspeed = 0

YObj = []
XObj = []

#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

def move(speedx, speedy, slow, window):
    ballrect.move_ip(speedx, speedy)
    pygame.display.update()

    





ballrect.move_ip(250, 50)
     



def level1():
    global xspeed
    global yspeed
    global XObj
    global YObj


    screen.fill((0, 0, 150))
    # Border for level 1
    grass = pygame.draw.rect(screen, (0, 160, 0), [100, 25, 300, 425], 0)
   
    Wall1 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 300, 5], 0)
    YObj.append(Wall1)

    Wall2 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 5, 425], 0)
    XObj.append(Wall2)

    Wall3 = pygame.draw.rect(screen, (0, 0, 0), [100, 450, 300, 5], 0)
    YObj.append(Wall3)

    Wall4 = pygame.draw.rect(screen, (0, 0, 0), [400, 25, 5, 430], 0)
    XObj.append(Wall4)

    createHole(250, 85)

running = True
while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.flip()

    level1()
    screen.blit(ball, ballrect)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            xMouse = event.pos[0]
            yMouse = event.pos[1]
            startPos = [xMouse, yMouse]
    elif event.type == pygame.MOUSEBUTTONUP and ballrect.collidepoint(startPos[0], startPos[1]):
        print("released")
        endPos = [event.pos[0], event.pos[1]]
        xspeed = startPos[0]-endPos[0]/10
        yspeed = startPos[1]-endPos[1]/10
        if xspeed > 10:
            xspeed = 10
        if yspeed > 10:
            yspeed = 10

        for thing in YObj:
            if ballrect.colliderect(thing):
                yspeed = -yspeed

        for thing in XObj:
            if ballrect.colliderect(thing):
                xspeed = -xspeed
        
        #move(xspeed, yspeed, 0.1, screen)
        #while xspeed > 0 or yspeed > 0:
            #xspeed -= .1
            #yspeed -= .1
            #time.sleep(.05)
            #move(xspeed, yspeed, .1, screen)



            



#def swing():
    
    

pygame.quit()