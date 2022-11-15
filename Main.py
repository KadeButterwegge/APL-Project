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
ballrect.update((250, 350), (14, 14))
maxSpeed = 15
strokes = 0


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
level = 6
levelRects = []
levelMethods = []
levelStrokes = []

#Level colors
borderCol = (0, 0, 0)
grassCol = (0, 150, 0)
boostCol = (90, 0, 90)
slowCol = (160, 10, 15)
bounceCol = (240, 120, 240)
iceCol = (105, 205, 220)
bridgeCol = (120, 80, 40)
tpCol = (245, 255, 45)

#Terrain frictions
grassFric = 0.93
boostFric = 1.05
slowFric = 0.89
iceFric = .9899999
bounceFric = -1.5

#Wall bounce
borBounce = 1
pinkBounce = 5

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

    Wall4 = pygame.draw.rect(screen, borderCol, [400, 25, width, 431], 0)
    Xobj.append(Wall4)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level1Rects = []
        level1Rects.append(Xobj)
        level1Rects.append(Yobj)
        level1Rects.append(terrain)
        level1Rects.append(terFric)
        levelRects.append(level1Rects)
    
    # Stroke counter
    font = pygame.font.SysFont('arial', 20)
    text = font.render(str("Strokes: " + str(strokes)), True, (255, 255, 255))
    screen.blit(text, (10, 0))

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
    
    # Stroke counter
    font = pygame.font.SysFont('arial', 20)
    text = font.render(str("Strokes: " + str(strokes)), True, (255, 255, 255))
    screen.blit(text, (10, 0))

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
    grass = pygame.draw.rect(screen, grassCol, [50, 130, 400, 250])
    terrain.append(grass)
    terFric.append(grassFric)

    water = pygame.draw.rect(screen, (0, 0, 150), [127, 200, 255, 115])

    # Border rectangles
    top = pygame.draw.rect(screen, borderCol, [50, 130, 400, width])
    Yobj.append(top)

    topL = pygame.draw.rect(screen, borderCol, [50, 130, width, 250])
    Xobj.append(topL)

    topR = pygame.draw.rect(screen, borderCol, [450, 130, width, 250])
    Xobj.append(topR)

    bot = pygame.draw.rect(screen, borderCol, [50, 380, 406, width])
    Yobj.append(bot)

    #Obstacle rectangles
    obsT = pygame.draw.rect(screen, borderCol, [122, 195, 260, width])
    Yobj.append(obsT)

    obsL = pygame.draw.rect(screen, borderCol, [122, 195, width, 120])
    Xobj.append(obsL)

    obsR = pygame.draw.rect(screen, borderCol, [382, 195, width, 120])
    Xobj.append(obsR)

    obsB = pygame.draw.rect(screen, borderCol, [122, 315, 266, width])
    Yobj.append(obsB)

    boost1 = pygame.draw.rect(screen, boostCol, [165, 136, 185, 59])
    terrain.append(boost1)
    terFric.append(boostFric)

    boost2 = pygame.draw.rect(screen, boostCol, [388, 200, 62, 115])
    terrain.append(boost2)
    terFric.append(boostFric)

    slow1 = pygame.draw.rect(screen, slowCol, [56, 215, 66, 85])
    terrain.append(slow1)
    terFric.append(slowFric)

    slow2 = pygame.draw.rect(screen, slowCol, [150, 321, 80, 59])
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
    
    # Stroke counter
    font = pygame.font.SysFont('arial', 20)
    text = font.render(str("Strokes: " + str(strokes)), True, (255, 255, 255))
    screen.blit(text, (10, 0))

    # Place hole on screen
    holerect.update((75, 150), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((270, 342), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)

def level4():
    global levelRects
    global setPos
    screen.fill((0, 0, 150))
    #Ball starting position


    # Lists for horizontal and vertical rectangles
    Xobj = []
    Yobj = []
    XBounce = []
    YBounce = []
    terrain = []
    terFric = []

    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, grassCol, [25, 25, 100, 405], 0)
    terrain.append(grass)
    terFric.append(grassFric)

    ice = pygame.draw.rect(screen, iceCol, [25, 81, 94, 175], 0)
    terrain.append(ice)
    terFric.append(iceFric)

    grass2 = pygame.draw.rect(screen, grassCol, [125, 75, 350, 100])
    terrain.append(grass2)
    terFric.append(grassFric)

    ice2 = pygame.draw.rect(screen, iceCol, [275, 75, 150, 100], 0)
    terrain.append(ice2)
    terFric.append(iceFric)

    grass3 = pygame.draw.rect(screen, grassCol, [325, 175, 100, 300])
    terrain.append(grass3)
    terFric.append(grassFric)

    ice3 = pygame.draw.rect(screen, iceCol, [300, 300, 125, 100])
    terrain.append(ice3)
    terFric.append(iceFric)

    grass4 = pygame.draw.rect(screen, grassCol, [175, 300, 150, 100])
    terrain.append(grass4)
    terFric.append(grassFric)
   
    # Border rectangles
    left = pygame.draw.rect(screen, borderCol, [25, 25, width, 405])
    Xobj.append(left)
    XBounce.append(borBounce)

    top = pygame.draw.rect(screen, bounceCol, [31, 25, 88, width])
    Yobj.append(top)
    YBounce.append(pinkBounce)

    botL = pygame.draw.rect(screen, borderCol, [25, 430, 100, width])
    Yobj.append(botL)
    YBounce.append(borBounce)

    midL = pygame.draw.rect(screen, borderCol, [119, 175, width, 255])
    Xobj.append(midL)
    XBounce.append(borBounce)

    midLT = pygame.draw.rect(screen, borderCol, [119, 25, width, 56])
    Xobj.append(midLT)
    XBounce.append(borBounce)

    topR = pygame.draw.rect(screen, borderCol, [125, 75, 350, width])
    Yobj.append(topR)
    YBounce.append(borBounce)

    right = pygame.draw.rect(screen, bounceCol, [469, 81, width, 94])
    Xobj.append(right)
    XBounce.append(pinkBounce)

    midTL = pygame.draw.rect(screen, borderCol, [125, 175, 200, width])
    Yobj.append(midTL)
    XBounce.append(borBounce)

    midTR = pygame.draw.rect(screen, borderCol, [425, 175, 50, width])
    Yobj.append(midTR)
    YBounce.append(borBounce)

    midRT = pygame.draw.rect(screen, borderCol, [319, 181, width, 119])
    Xobj.append(midRT)
    XBounce.append(borBounce)

    mid3 = pygame.draw.rect(screen, borderCol, [175, 294, 150, width])
    Yobj.append(mid3)
    YBounce.append(borBounce)

    mid = pygame.draw.rect(screen, borderCol, [169, 294, width, 106])
    Xobj.append(mid)
    XBounce.append(borBounce)

    midB = pygame.draw.rect(screen, borderCol, [169, 400, 156, width])
    Yobj.append(midB)
    YBounce.append(borBounce)

    bot = pygame.draw.rect(screen, bounceCol, [319, 475, 106, width])
    Yobj.append(bot)
    YBounce.append(pinkBounce)

    midR = pygame.draw.rect(screen, borderCol, [319, 400, width, 81])
    Xobj.append(midR)
    XBounce.append(borBounce)

    right = pygame.draw.rect(screen, borderCol, [425, 175, width, 306])
    Xobj.append(right)
    XBounce.append(borBounce)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level4Rects = []
        level4Rects.append(Xobj)
        level4Rects.append(Yobj)
        level4Rects.append(terrain)
        level4Rects.append(terFric)
        level4Rects.append(XBounce)
        level4Rects.append(YBounce)
        levelRects.append(level4Rects)
    
    # Stroke counter
    font = pygame.font.SysFont('arial', 20)
    text = font.render(str("Strokes: " + str(strokes)), True, (255, 255, 255))
    screen.blit(text, (10, 0))

    # Place hole on screen
    holerect.update((213, 337), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((68, 370), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)

def level5():
    global levelRects
    global setPos
    global strokes
    screen.fill((0, 0, 150))

    # Lists for horizontal and vertical rectangles
    Xobj = []
    Yobj = []
    XBounce = []
    YBounce = []
    terrain = []
    terFric = []

    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, grassCol, [50, 326, 125, 125])
    terrain.append(grass)
    terFric.append(grassFric)

    grass3 = pygame.draw.rect(screen, grassCol, [60, 346, 370, 85])
    terrain.append(grass3)
    terFric.append(grassFric)

    bridge = pygame.draw.rect(screen, bridgeCol, [175, 346, 150, 85])
    terrain.append(bridge)
    terFric.append(grassFric)

    bridge2 = pygame.draw.rect(screen, bridgeCol, [345, 124, 85, 250])
    terrain.append(bridge2)
    terFric.append(grassFric)

    grass2 = pygame.draw.rect(screen, grassCol, [325, 326, 125, 125])
    terrain.append(grass2)
    terFric.append(grassFric)

    bridge3 = pygame.draw.rect(screen, bridgeCol, [125, 69, 250, 85])
    terrain.append(bridge3)
    terFric.append(grassFric)

    grass4 = pygame.draw.rect(screen, grassCol, [325, 49, 125, 125])
    terrain.append(grass4)
    terFric.append(grassFric)

    grass5 = pygame.draw.rect(screen, grassCol, [50, 49, 125, 125])
    terrain.append(grass5)
    terFric.append(grassFric)

   
    # Border rectangles
    top1 = pygame.draw.rect(screen, borderCol, [44, 320, 137, width])
    Yobj.append(top1)
    YBounce.append(borBounce)

    top3 = pygame.draw.rect(screen, borderCol, [319, 43, 137, width])
    Yobj.append(top3)
    YBounce.append(borBounce)

    top4 = pygame.draw.rect(screen, borderCol, [44, 43, 137, width])
    Yobj.append(top4)
    YBounce.append(borBounce)

    left = pygame.draw.rect(screen, borderCol, [44, 320, width, 137])
    Xobj.append(left)
    XBounce.append(borBounce)

    left2 = pygame.draw.rect(screen, borderCol, [44, 43, width, 137])
    Xobj.append(left2)
    XBounce.append(borBounce)

    right = pygame.draw.rect(screen, borderCol, [450, 320, width, 137])
    Xobj.append(right)
    XBounce.append(borBounce)

    right2 = pygame.draw.rect(screen, borderCol, [450, 44, width, 135])
    Xobj.append(right)
    XBounce.append(borBounce)

    topr = pygame.draw.rect(screen, borderCol, [175, 320, width, 25])
    Xobj.append(topr)
    XBounce.append(borBounce)

    topl = pygame.draw.rect(screen, borderCol, [319, 320, width, 25])
    Xobj.append(topl)
    XBounce.append(borBounce)

    botr = pygame.draw.rect(screen, borderCol, [175, 431, width, 25])
    Xobj.append(botr)
    XBounce.append(borBounce)

    botl = pygame.draw.rect(screen, borderCol, [319, 431, width, 25])
    Xobj.append(botl)
    XBounce.append(borBounce)

    topr2 = pygame.draw.rect(screen, borderCol, [175, 44, width, 25])
    Xobj.append(topr2)
    XBounce.append(borBounce)

    topl2 = pygame.draw.rect(screen, borderCol, [319, 44, width, 25])
    Xobj.append(topl2)
    XBounce.append(borBounce)

    botr2 = pygame.draw.rect(screen, borderCol, [175, 154, width, 25])
    Xobj.append(botr2)
    XBounce.append(borBounce)

    botl2 = pygame.draw.rect(screen, borderCol, [319, 154, width, 25])
    Xobj.append(botl2)
    XBounce.append(borBounce)

    mtr = pygame.draw.rect(screen, borderCol, [319, 174, 26, width])
    Yobj.append(mtr)
    YBounce.append(borBounce)

    mtl = pygame.draw.rect(screen, borderCol, [430, 174, 26, width])
    Yobj.append(mtl)
    YBounce.append(borBounce)

    mbr = pygame.draw.rect(screen, borderCol, [319, 320, 26, width])
    Yobj.append(mbr)
    YBounce.append(borBounce)

    mbl = pygame.draw.rect(screen, borderCol, [430, 320, 26, width])
    Yobj.append(mbl)
    YBounce.append(borBounce)

    toprcap = pygame.draw.rect(screen, borderCol, [175, 345, 6, 1])
    Yobj.append(toprcap)
    YBounce.append(toprcap)

    toplcap = pygame.draw.rect(screen, borderCol, [319, 345, 6, 1])
    Yobj.append(toplcap)
    YBounce.append(toprcap)

    bot = pygame.draw.rect(screen, borderCol, [44, 451, 137, width])
    Yobj.append(bot)
    YBounce.append(borBounce)

    bot2 = pygame.draw.rect(screen, borderCol, [319, 451, 137, width])
    Yobj.append(bot2)
    YBounce.append(borBounce)

    bot3 = pygame.draw.rect(screen, borderCol, [44, 174, 137, width])
    Yobj.append(bot3)
    YBounce.append(borBounce)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level5Rects = []
        level5Rects.append(Xobj)
        level5Rects.append(Yobj)
        level5Rects.append(terrain)
        level5Rects.append(terFric)
        level5Rects.append(XBounce)
        level5Rects.append(YBounce)
        levelRects.append(level5Rects)
    
    # Stroke counter
    font = pygame.font.SysFont('arial', 20)
    text = font.render(str("Strokes: " + str(strokes)), True, (255, 255, 255))
    screen.blit(text, (10, 0))

    # Place hole on screen
    holerect.update((80, 96), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((88, 380), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)

def level6():
    global levelRects
    global setPos
    screen.fill((0, 0, 150))
    #Ball starting position


    # Lists for horizontal and vertical rectangles
    Xobj = []
    Yobj = []
    XBounce = []
    YBounce = []
    terrain = []
    terFric = []
    tprects = []
    tpcords = []

    # Width for the border
    width = 6
    
    # Ground
    grass = pygame.draw.rect(screen, grassCol, [50, 75, 400, 100])
    terrain.append(grass)
    terFric.append(grassFric)

    grass2 = pygame.draw.rect(screen, grassCol, [50, 325, 400, 100])
    terrain.append(grass2)
    terFric.append(grassFric)

    tp = pygame.draw.rect(screen, tpCol, [390, 362, 25, 25])
    tprects.append(tp)
    tpcords.append((395, 117))

    receive = pygame.draw.rect(screen, tpCol, [390, 112, 25, 25])

    # Border Walls
    top = pygame.draw.rect(screen, borderCol, [44, 69, 412, width])
    Yobj.append(top)
    YBounce.append(borBounce)

    top2 = pygame.draw.rect(screen, borderCol, [44, 319, 412, width])
    Yobj.append(top2)
    YBounce.append(borBounce)

    bot = pygame.draw.rect(screen, borderCol, [44, 175, 412, width])
    Yobj.append(bot)
    YBounce.append(borBounce)

    bot2 = pygame.draw.rect(screen, borderCol, [44, 425, 412, width])
    Yobj.append(bot2)
    YBounce.append(borBounce)

    left = pygame.draw.rect(screen, borderCol, [44, 69, width, 112])
    Xobj.append(left)
    XBounce.append(borBounce)

    left2 = pygame.draw.rect(screen, borderCol, [44, 319, width, 112])
    Xobj.append(left2)
    XBounce.append(borBounce)

    right = pygame.draw.rect(screen, borderCol, [450, 69, width, 112])
    Xobj.append(right)
    XBounce.append(borBounce)

    right2 = pygame.draw.rect(screen, borderCol, [450, 319, width, 112])
    Xobj.append(right2)
    XBounce.append(borBounce)

    # 2D array containging vertical and horizontal rectangles lists
    if len(levelRects) <= level-1:
        level6Rects = []
        level6Rects.append(Xobj)
        level6Rects.append(Yobj)
        level6Rects.append(terrain)
        level6Rects.append(terFric)
        level6Rects.append(XBounce)
        level6Rects.append(YBounce)
        level6Rects.append(tprects)
        level6Rects.append(tpcords)
        levelRects.append(level6Rects)
    
    # Stroke counter
    font = pygame.font.SysFont('arial', 20)
    text = font.render(str("Strokes: " + str(strokes)), True, (255, 255, 255))
    screen.blit(text, (10, 0))

    # Place hole on screen
    holerect.update((70, 112), (30, 30))
    screen.blit(hole, holerect)

    # Start position for the ball
    if setPos:
        ballrect.update((73, 370), (14, 14))
        setPos = False
    screen.blit(ball, ballrect)

# Add all levels to a list
levelMethods.append(level1)
levelMethods.append(level2)
levelMethods.append(level3)
levelMethods.append(level4)
levelMethods.append(level5)
levelMethods.append(level6)

running = True
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
                # Store start position
                startPos = [event.pos[0], event.pos[1]]

        # Check if the mouse is clicking on the ball, and the mouse button was released
        elif event.type == pygame.MOUSEBUTTONUP and ballrect.collidepoint(startPos[0], startPos[1]):
            #Store end position
            endPos = [event.pos[0], event.pos[1]]

            #Set x and y starting speed for current stroke
            xspeed = (startPos[0]-endPos[0])/3
            yspeed = (startPos[1]-endPos[1])/3
            
            #Add stroke
            strokes += 1

            #While loop to move ball
            while abs(xspeed) > 0 or abs(yspeed) > 0:

                time.sleep(.016)
                #Draw new ball position
                screen.blit(ball, ballrect)

                #Draw level
                levelMethods[level-1]()
                pygame.display.flip()
                friction = 0.93
                
                # Teleport introduced in level 6
                if level > 5:
                    for rect in levelRects[level-1][6]:
                        if rect.contains(ballrect):
                            ballrect.update((levelRects[level-1][7][levelRects[level-1][6].index(rect)]), (14, 14))
                            xspeed = 0
                            yspeed = 0
                
                #Check for wall collisions
                inMap = False

                #Vertical rectangle collisions
                for rectx in levelRects[level-1][0]:
                    if ballrect.colliderect(rectx):
                        xspeed = -xspeed
                        ballrect.move_ip(xspeed, 0)
                        # Changes friction, different frictions are introduced in level 3
                        if level > 3:
                            xspeed *= levelRects[level-1][4][levelRects[level-1][0].index(rectx)]

                #Horizontal rectangle collisions
                for recty in levelRects[level-1][1]:
                    if ballrect.colliderect(recty):
                        yspeed = -yspeed
                        ballrect.move_ip(0, yspeed)
                        # Changes friction, different frictions are introduced in level 3
                        if level > 3:
                            yspeed *= levelRects[level-1][5][levelRects[level-1][1].index(recty)]

                #Determines friction, and makes sure ball is in map
                for rect in levelRects[level-1][2]:
                    if rect.contains(ballrect):
                        inMap = True
                        friction = levelRects[level-1][3][levelRects[level-1][2].index(rect)]
                
                # Teleport to prior position if ball goes outside of map
                if inMap == False:
                    friction = 0
                    xspeed = 0
                    yspeed = 0
                    ballrect.update((startPos[0]-7, startPos[1]-7), (14, 14))
                    startPos = (0, 0)
                    strokes += 1

                #Slow down the ball
                if abs(xspeed) > 0:
                    xspeed *= friction
                if abs(yspeed) > 0:
                    yspeed *= friction

                #Stops ball
                if xspeed > -0.1 and xspeed < 0.1:
                    xspeed = 0
                if yspeed > -0.1 and yspeed < 0.1:
                    yspeed = 0
                
                #Caps out the speed
                if xspeed > maxSpeed:
                    xspeed = maxSpeed
                if yspeed > maxSpeed:
                    yspeed = maxSpeed
                if xspeed < -maxSpeed:
                    xspeed = -maxSpeed
                if yspeed < -maxSpeed:
                    yspeed = -maxSpeed
                
                #Check for hole collision
                if holerect.contains(ballrect) and abs(xspeed) < 4 and abs(yspeed) < 4:
                    xspeed = 0
                    yspeed = 0
                    setPos = True
                    if level < len(levelMethods):
                        level += 1
                        levelStrokes.append(strokes)
                        strokes = 0
                elif holerect.contains(ballrect) and abs(xspeed) > 4 and abs(yspeed) > 4:
                    xspeed = random.randint(math.floor(-abs(xspeed)), math.floor(abs(xspeed)))
                    yspeed = random.randint(math.floor(-abs(yspeed)), math.floor(abs(yspeed)))
                #Move the ball
                ballrect.move_ip(xspeed, yspeed)

    except:
        pass
    
pygame.quit()   