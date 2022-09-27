#Imports
import pygame
import time
import random
import math
pygame.init()

#Make Screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
FPS = 50

#Make ball
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (14, 14))
ballrect = ball.get_rect()
friction = 0.93

#Hole setup
hole = pygame.image.load("Golf Hole.png")
hole = pygame.transform.scale(hole, (22, 22))
holerect = hole.get_rect()
holerect.move_ip(100, 100)

#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

#Level layouts
setPos = True
level = 1
levelRects = []
levelMethods = []





        

ballrect.update((250, 350), (14, 14))

def level1():
    global levelRects
    screen.fill((0, 0, 150))
    # Lists for horizontal and vertical rectangles
    Xobj = []
    Yobj = []
    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, (0, 160, 0), [100, 25, 300, 425], 0)
   
    # Border rectangles
    Wall1 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, 300, width], 0)
    Yobj.append(Wall1)

    Wall2 = pygame.draw.rect(screen, (0, 0, 0), [100, 25, width, 425], 0)
    Xobj.append(Wall2)

    Wall3 = pygame.draw.rect(screen, (0, 0, 0), [100, 450, 300, width], 0)
    Yobj.append(Wall3)

    Wall4 = pygame.draw.rect(screen, (0, 0, 0), [400, 25, width, 430], 0)
    Xobj.append(Wall4)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level1Rects = []
        level1Rects.append(Xobj)
        level1Rects.append(Yobj)
        levelRects.append(level1Rects)
    
    # Place hole on screen
    holerect.update((250, 50), (20, 20))
    screen.blit(hole, holerect)

    # Start position for the ball
    screen.blit(ball, ballrect)

def level2():
    global levelRects
    global setPos
    screen.fill((0, 0, 150))
    # Lists for horizontal and vertical rectangles
    Xobj2 = []
    Yobj2 = []
    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, (0, 160, 0), [100, 25, 300, 425], 0)
   
    # Border rectangles

    # 2D array containging vertical and horizontal rectangles lists
    level2Rects = []
    level2Rects.append(Xobj2)
    level2Rects.append(Yobj2)
    levelRects.append(level2Rects)
    
    # Place hole on screen
    holerect.update((250, 50), (20, 20))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((250, 400), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)

levelMethods.append(level1)
levelMethods.append(level2)

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
    levelMethods[level-1]()
    #try:
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            xMouse = event.pos[0]
            yMouse = event.pos[1]
            startPos = [xMouse, yMouse]
    elif event.type == pygame.MOUSEBUTTONUP and ballrect.collidepoint(startPos[0], startPos[1]):
        endPos = [event.pos[0], event.pos[1]]
        xspeed = (startPos[0]-endPos[0])/3
        yspeed = (startPos[1]-endPos[1])/3
        if xspeed > 14:
            xspeed = 14
        if yspeed > 14:
            yspeed = 14
        if xspeed < -14:
            xspeed = -14
        if yspeed < -14:
            yspeed = -14

        while abs(xspeed) > 0 or abs(yspeed) > 0:
            time.sleep(.016)
            #Draw new ball position
            screen.blit(ball, ballrect)
            #Draw level
            levelMethods[level-1]()
            pygame.display.flip()

            #Check for wall collisions
            for rectx in levelRects[level-1][0]:
                if ballrect.colliderect(rectx):
                    xspeed = -xspeed
            for recty in levelRects[level-1][1]:
                if ballrect.colliderect(recty):
                    yspeed = -yspeed
            #Slow down the ball
            if xspeed > 0:
                xspeed *= friction
            if yspeed > 0:
                yspeed *= friction
            if xspeed < 0:
                xspeed *= friction
            if yspeed < 0:
                yspeed *= friction
            if xspeed > -0.5 and xspeed < 0.5:
                xspeed = 0
            if yspeed > -0.5 and yspeed < 0.5:
                yspeed = 0
            #Check for hole collision
            if holerect.contains(ballrect) and abs(xspeed) < 4 and abs(yspeed) < 4:
                xspeed = 0
                yspeed = 0
                setPos = True
                ballrect.update((250, 350), (14, 14))
                level += 1
            elif holerect.contains(ballrect) and abs(xspeed) > 4 and abs(yspeed) > 4:
                xspeed = random.randint(math.floor(-abs(xspeed)), math.floor(abs(xspeed)))
                yspeed = random.randint(math.floor(-abs(yspeed)), math.floor(abs(yspeed)))
            ballrect.move_ip(xspeed, yspeed)

    #except:
        poo = 123123123123123

#
pygame.quit()