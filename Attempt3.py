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


#Icon and Caption
pygame.display.set_caption("Mini Golf")
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

#Level layouts
setPos = True
level = 3
levelRects = []
levelMethods = []

#Level colors
borderCol = (0, 0, 0)
grassCol = (0, 150, 0)
boostCol = (90, 0, 90)
slowCol = (160, 10, 15)

#Terrain frictions
grassFric = 0.93
boostFric = 1.05
slowFric = 0.89
iceFric = .999999

        

ballrect.update((250, 350), (14, 14))

def level1():
    global levelRects
    screen.fill((0, 0, 150))
    #Ball starting position


    # Lists for horizontal and vertical rectangles
    Xobj = []
    Yobj = []
    terrain = []
    terFric = []

    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, grassCol, [100, 25, 300, 425], 0)
    terrain.append(grass)
    terFric.append(grassFric)
   
    # Border rectangles
    Wall1 = pygame.draw.rect(screen, borderCol, [100, 25, 300, width], 0)
    Yobj.append(Wall1)

    Wall2 = pygame.draw.rect(screen, borderCol, [100, 25, width, 425], 0)
    Xobj.append(Wall2)

    Wall3 = pygame.draw.rect(screen, borderCol, [100, 450, 300, width], 0)
    Yobj.append(Wall3)

    Wall4 = pygame.draw.rect(screen, borderCol, [400, 25, width, 430], 0)
    Xobj.append(Wall4)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level1Rects = []
        level1Rects.append(Xobj)
        level1Rects.append(Yobj)
        level1Rects.append(terrain)
        level1Rects.append(terFric)
        levelRects.append(level1Rects)
    
    # Place hole on screen
    holerect.update((250, 50), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    screen.blit(ball, ballrect)

def level2():
    global levelRects
    global setPos
    screen.fill((0, 0, 150))
    #Ball starting position

    # Lists for horizontal and vertical rectangles
    Xobj = []
    Yobj = []
    terrain = []
    terFric = []

    # Ground
    grass = pygame.draw.rect(screen, grassCol, [50, 25, 400, 180], 0)
    terrain.append(grass)
    terFric.append(grassFric)

    grass2 = pygame.draw.rect(screen, grassCol, [188, 175, 133, 300])
    water = pygame.draw.rect(screen, (0, 0, 150), [130, 80, 245, 70], 0)
    terrain.append(grass)
    terFric.append(grassFric)

    # Width for the border
    width = 6

    # Border rectangles
    top_wall = pygame.draw.rect(screen, borderCol, [50, 25, 400, width], 0)
    Yobj.append(top_wall)

    top_left = pygame.draw.rect(screen, borderCol, [50, 25, width, 180], 0)
    Xobj.append(top_left)

    mid_left = pygame.draw.rect(screen, borderCol, [50, 205, 138, width], 0)
    Yobj.append(mid_left)

    top_right = pygame.draw.rect(screen, borderCol, [450, 25, width, 180], 0)
    Xobj.append(top_right)

    mid_right = pygame.draw.rect(screen, borderCol, [326, 205, 130, width], 0)
    Yobj.append(mid_right)

    bot_left = pygame.draw.rect(screen, borderCol, [188, 205, width, 270], 0)
    Xobj.append(bot_left)

    bot_right = pygame.draw.rect(screen, borderCol, [321, 205, width, 270], 0)
    Xobj.append(bot_right)

    bot_wall = pygame.draw.rect(screen, borderCol, [188, 475, 139, width], 0)
    Yobj.append(bot_wall)

    top_obs = pygame.draw.rect(screen, borderCol, [125, 75, 250, width], 0)
    Yobj.append(top_obs)

    bot_obs = pygame.draw.rect(screen, borderCol, [125, 150, 250, width], 0)
    Yobj.append(bot_obs)

    left_obs = pygame.draw.rect(screen, borderCol, [125, 75, width, 75], 0)
    Xobj.append(left_obs)
    
    right_obs = pygame.draw.rect(screen, borderCol, [375, 75, width, 81], 0)
    Xobj.append(right_obs)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level2Rects = []
        level2Rects.append(Xobj)
        level2Rects.append(Yobj)
        level2Rects.append(terrain)
        level2Rects.append(terFric)
        levelRects.append(level2Rects)
    
    # Place hole on screen
    holerect.update((250, 40), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((250, 400), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)

def level3():
    global levelRects
    global setPos
    screen.fill((0, 0, 150))

    # Lists for horizontal rectangles, vertical rectangles, and terrain
    Xobj = []
    Yobj = []
    terrain = []
    terFric = [] #Contains the friction multiplier for each terrain rectangle

    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, grassCol, [50, 50, 400, 250])
    terrain.append(grass)
    terFric.append(grassFric)

    water = pygame.draw.rect(screen, (0, 0, 150), [127, 120, 255, 115])

    # Border rectangles
    top = pygame.draw.rect(screen, borderCol, [50, 50, 400, width])
    Yobj.append(top)

    topL = pygame.draw.rect(screen, borderCol, [50, 50, width, 250])
    Xobj.append(topL)

    topR = pygame.draw.rect(screen, borderCol, [450, 50, width, 250])
    Xobj.append(topR)

    bot = pygame.draw.rect(screen, borderCol, [50, 300, 406, width])
    Yobj.append(bot)

    #Obstacle rectangles
    obsT = pygame.draw.rect(screen, borderCol, [122, 115, 260, width])
    Yobj.append(obsT)

    obsL = pygame.draw.rect(screen, borderCol, [122, 115, width, 120])
    Xobj.append(obsL)

    obsR = pygame.draw.rect(screen, borderCol, [382, 115, width, 120])
    Xobj.append(obsR)

    obsB = pygame.draw.rect(screen, borderCol, [122, 235, 266, width])
    Yobj.append(obsB)

    boost1 = pygame.draw.rect(screen, boostCol, [165, 56, 185, 59])
    terrain.append(boost1)
    terFric.append(boostFric)

    boost2 = pygame.draw.rect(screen, boostCol, [388, 120, 62, 115])
    terrain.append(boost2)
    terFric.append(boostFric)

    slow1 = pygame.draw.rect(screen, slowCol, [56, 135, 66, 85])
    terrain.append(slow1)
    terFric.append(slowFric)

    slow2 = pygame.draw.rect(screen, slowCol, [150, 241, 80, 59])
    terrain.append(slow2)
    terFric.append(slowFric)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level3Rects = []
        level3Rects.append(Xobj)
        level3Rects.append(Yobj)
        level3Rects.append(terrain)
        level3Rects.append(terFric)
        levelRects.append(level3Rects)
    
    # Place hole on screen
    holerect.update((75, 70), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((270, 262), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)


levelMethods.append(level1)
levelMethods.append(level2)
levelMethods.append(level3)

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
    try:
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
                friction = 0.93
                #Check for wall collisions
                for rectx in levelRects[level-1][0]:
                    if ballrect.colliderect(rectx):
                        xspeed = -xspeed
                for recty in levelRects[level-1][1]:
                    if ballrect.colliderect(recty):
                        yspeed = -yspeed
                for rect in levelRects[level-1][2]:
                    if rect.contains(ballrect):
                        friction = levelRects[level-1][3][levelRects[level-1][2].index(rect)]
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
                if xspeed > 14:
                    xspeed = 14
                if yspeed > 14:
                    yspeed = 14
                if xspeed < -14:
                    xspeed = -14
                if yspeed < -14:
                    yspeed = -14
                
                #Check for hole collision
                if holerect.contains(ballrect) and abs(xspeed) < 4 and abs(yspeed) < 4:
                    xspeed = 0
                    yspeed = 0
                    setPos = True
                    if level < len(levelMethods):
                        level += 1
                elif holerect.contains(ballrect) and abs(xspeed) > 4 and abs(yspeed) > 4:
                    xspeed = random.randint(math.floor(-abs(xspeed)), math.floor(abs(xspeed)))
                    yspeed = random.randint(math.floor(-abs(yspeed)), math.floor(abs(yspeed)))
                ballrect.move_ip(xspeed, yspeed)

    except:
        poo = 123123123123123

#
pygame.quit()   