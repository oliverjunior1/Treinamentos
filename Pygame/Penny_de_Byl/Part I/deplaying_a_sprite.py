import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Hello sprite')
sprite1 = pygame.image.load('../Images/football.png')
screen.fill((0,0,0))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (384,284))
    pygame.display.update()
pygame.quit()