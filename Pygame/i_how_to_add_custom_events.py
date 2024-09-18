import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
timer = pygame.time.Clock()

pygame.display.set_caption('Custom Events')

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

bg_active_color= WHITE
screen.fill(WHITE)

CHANGE_COLOR = pygame.USEREVENT + 1
ON_BOX = pygame.USEREVENT + 2

box = pygame.Rect((255,255,50,50))
grow = True

pygame.time.set_timer(CHANGE_COLOR, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == CHANGE_COLOR:
            if bg_active_color == GREEN:
                screen.fill(GREEN)
                bg_active_color = WHITE
            elif bg_active_color == WHITE:
                screen.fill(WHITE)
                bg_active_color = GREEN

            if event.type == ON_BOX:
                if grow:
                    box.inflate_ip(3,3)
                    grow = box.width < 75
                else:
                    box.inflate_ip(-3,-3)
                    grow = box.width < 50

            if event.type == pygame.QUIT:
                running = False


        if box.collidepoint(pygame.mouse.get_pos()):
            pygame.event.post(pygame.event.Event(ON_BOX))

        pygame.draw.rect(screen, RED, box)
        pygame.display.update()
        timer.tick(30)

pygame.quit()


