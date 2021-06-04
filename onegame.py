import pygame
screen_width=800
screen_height=600
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
running = True
x=250
y=250
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (x,y), 75)
    while x<250:
        x+=0.003
    y-=0.02
    pygame.display.flip()
pygame.quit()