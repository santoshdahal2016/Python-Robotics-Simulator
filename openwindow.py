import 	pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Open Window")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False