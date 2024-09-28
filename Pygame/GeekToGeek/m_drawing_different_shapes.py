import pygame

pygame.init()

white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)
black = (0,0,0)
red = (255,0,0)

x = 400
y = 400

display_surface = pygame.display.set_mode((x, y))
pygame.display.set_caption('Drawing')
display_surface.fill(white)

pygame.draw.polygon(display_surface. blue)