import pygame
from math import sin,cos,pi
screen_width=800
screen_height=600
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
running = True
x=200
y=100

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    screen.fill((255, 255, 255))
    for i in range(int(2*pi)):
        x+=cos(i)
        y+=sin(i)
        pygame.draw.circle(screen, (0, 0, 255), (x,y), 75)
        x+=0.00001
        y+=0.00001
    pygame.display.flip()
pygame.quit()