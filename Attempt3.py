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

#asdf

#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

#Level layouts
level = 1
levelRects = []
levelMethods = []


def createHole(x, y):
    pygame.draw.circle(screen, (10, 10, 10), (x, y), 10)

        

ballrect.move_ip(250, 50)

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
    level1Rects = []
    level1Rects.append(Xobj)
    level1Rects.append(Yobj)
    levelRects.append(level1Rects)

    # Start position for the ball
    screen.blit(ball, ballrect)
    
    # 
    createHole(250, 85)

levelMethods.append(level1)

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

        friction = 0.5

        while abs(xspeed) > 0 or abs(yspeed) > 0:

            time.sleep(0.05)
            ballrect.move_ip(xspeed, yspeed)
            print(pygame.display.update())
            #print("dung")

            ballrect.move_ip(xspeed, yspeed)
            time.sleep(.016)
            screen.blit(ball, ballrect)
            levelMethods[level-1]()
            pygame.display.flip()
            for rectx in levelRects[level-1][0]:
                if ballrect.colliderect(rectx):
                    xspeed = -xspeed
            for recty in levelRects[level-1][1]:
                if ballrect.colliderect(recty):
                    yspeed = -yspeed

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



pygame.quit()