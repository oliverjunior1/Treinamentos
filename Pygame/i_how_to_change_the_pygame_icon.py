import pygame

pygame.init()
screen = pygame.display.set_mode([600,400])
img = pygame.image.load('gfglogo.png')
pygame.display.set_icon(img)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,0))
    pygame.draw.circle(screen,(0,0,0),(300,200),75)
    pygame.display.update()

pygame.quit()