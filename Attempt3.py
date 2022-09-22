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


#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

#Level layouts
level = 1
levelRects = []

def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

def move(xspeed, yspeed, friction, window):
    global level
    global levelRects
    moveX = xspeed
    moveY = yspeed
    for rectx in levelRects[level-1][0]:
        if ballrect.colliderect(rectx):
            moveY = -moveY
    for recty in levelRects[level-1][1]:
        if ballrect.colliderect(recty):
            moveX = -moveX
    while xspeed > 0 or yspeed > 0:
        ballrect.move_ip(moveX, moveY)
        pygame.display.update()
        if xspeed > 0:
            xspeed -= friction
        if yspeed > 0:
            yspeed -= friction
        if xspeed < 0:
            xspeed += friction
        if yspeed < 0:
            yspeed += friction
        if xspeed > -0.5 and xspeed < 0.5:
            xspeed = 0
        if yspeed > -0.5 and yspeed < 0.5:
            yspeed = 0
        

ballrect.move_ip(250, 50)

def level1():
    global levelRects
    screen.fill((0, 0, 150))
    # Border for level 1
    Xobj = []
    Yobj = []
    
    grass = pygame.draw.rect(screen, (0, 160, 0), [100, 25, 300, 425], 0)
   
    Wall1 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 300, 5], 0)
    Yobj.append(Wall1)

    Wall2 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 5, 425], 0)
    Xobj.append(Wall2)

    Wall3 = pygame.draw.rect(screen, (0, 0, 0), [100, 450, 300, 5], 0)
    Yobj.append(Wall3)

    Wall4 = pygame.draw.rect(screen, (0, 0, 0), [400, 25, 5, 430], 0)
    Xobj.append(Wall4)

    level1Rects = []
    level1Rects.append(Xobj)
    level1Rects.append(Yobj)
    levelRects.append(level1Rects)

    screen.blit(ball, ballrect)
    
    createHole(250, 85)

running = True
doodoo = True
while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.flip()

    level1()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            xMouse = event.pos[0]
            yMouse = event.pos[1]
            startPos = [xMouse, yMouse]
            print(startPos)
    elif event.type == pygame.MOUSEBUTTONUP and ballrect.collidepoint(startPos[0], startPos[1]):
        endPos = [event.pos[0], event.pos[1]]
        print(endPos)
        xspeed = (startPos[0]-endPos[0])/1.5
        yspeed = (startPos[1]-endPos[1])/1.5
        print(xspeed)
        print(yspeed)
        if xspeed > 14:
            xspeed = 14
        if yspeed > 14:
            yspeed = 14
        if xspeed < -14:
            xspeed = -14
        if yspeed < -14:
            yspeed = -14

        move(xspeed, yspeed, 0.5, screen)
    #screen.blit(ball, ballrect)



pygame.quit()