#Imports
import pygame
import time
pygame.init()

#Screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
FPS = 50

#Ball
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (14, 14))
ballrect = ball.get_rect()

def hit()

#Run Game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    time.sleep(0.2)
    clock.tick(FPS)
    screen.blit(ball, ballrect)