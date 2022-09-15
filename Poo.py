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
xspeed = 13
yspeed = 13



#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

def move(speedx, speedy, slow, window):
    global xspeed
    global yspeed
    ballrect.move_ip(xspeed, yspeed)
    if xspeed>0:
        xspeed -= slow
    if xspeed<0:
        xspeed += slow
    if yspeed>0:
        yspeed -= slow
    if yspeed<0:
        yspeed += slow




   
    
     
ballrect.move_ip(250, 50)


def level1():
    global xspeed
    global yspeed
    YObj = []
    XObj = []

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

    for thing in YObj:
        if ballrect.colliderect(thing):
            yspeed = -yspeed
    
    for thing in XObj:
        if ballrect.colliderect(thing):
            xspeed = -xspeed

    


    createHole(250, 85)

running = True
while running:
    doodoo = True
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.flip()

    level1()
    #move(xspeed, yspeed, 0.05, screen)
    
    clickBall = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            xMouse = event.pos[0]
            yMouse = event.pos[1]
            if ballrect.collidepoint(xMouse, yMouse):
                print("clicked ball")
                startPos = [xMouse, yMouse]
                clickBall = True
    if event.type == pygame.MOUSEBUTTONUP and doodoo == True:
        print("up")
        doodoo = False
        #endPos = [event.pos[0], event.pos[1]]
        #move(abs(startPos[0]-endPos[0]), abs(startPos[1]-endPos[1]), 0.05, screen)
            


    screen.blit(ball, ballrect)

#def swing():
    
    

pygame.quit()