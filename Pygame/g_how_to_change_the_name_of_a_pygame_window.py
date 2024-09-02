import pygame
pygame.init()

pygame.display.set_mode((400,500))
pygame.display.set_caption('GeeksforGeeks')
Icon = pygame.image.load('gfglogo.png')
pygame.display.set_icon(Icon)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
