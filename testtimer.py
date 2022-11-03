import pygame
import sys
 
pygame.init() #initialize all imported pygame modules
 
# set window size
windowX = 500
windowY = 300
# initialize screen object
screen = pygame.display.set_mode((windowX, windowY))
 
# set window title (optional)
pygame.display.set_caption("My cool program!")
time_delay = 1000 # 1 second
timer_event = pygame.USEREVENT + 1 #assign unique ID to this event
pygame.time.set_timer(timer_event , time_delay )
is_moving = True 
# set window background color (optional)
bColor = "green"
screen.fill(bColor)
xspeed = 5
yspeed = 5
xcor = 150
ycor = 100 
 
running = True
# event loop - basically a "Forever" loop that runs around 60 times per second
while running:
    # get all current events: keyboard, mouse, timer, buttons
    events = pygame.event.get()
    # process each event
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == timer_event:
            print("tick tock!")
            if xcor > 200:
                is_moving = False
            if is_moving:
                xcor += xspeed
                ycor += yspeed

 
    # re-draw all graphics
    screen.fill(bColor)
    # draw stuff on top of the background here
    #..
    #..
    pygame.draw.rect(screen, "orange", (xcor, ycor, 50, 50))
    pygame.display.update() # must be called in order to see any changes on screen
