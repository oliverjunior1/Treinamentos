# import pygame
#
# (numpass, numfail) = pygame.init()
#
# print('Number of modules initialized successfully:', numpass)
#
################################################
import pygame

pygame.init()

is_initialized = pygame.get_init()

print('Is pygame modules initialized:', is_initialized)

