import pygame
import sys

pygame.init()
display = pygame.display.set_mode((500,500))
image = pygame.image.load('gfglogo.png')
display.blit(image,(100,100))
pygame.time.wait(5000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()