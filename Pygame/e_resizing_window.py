# import pygame
#
# screen = pygame.display.set_mode((400,400))
# pygame.display.set_caption('Not resizable')
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# pygame.quit()
######################################################################
import pygame

screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption('Resizable')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
