import pygame

class Simulator(object):
    def main(self , screen):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            

              

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Structure")
    screen = pygame.display.set_mode((640,480))
    Simulator().main(screen)
