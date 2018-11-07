import pygame

"""Define color"""
red = (200, 0, 0)
blue = (0, 0, 255)
green = (0, 155, 0)
yellow = (155, 155, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class Simulator(object):
	def main(self , screen):
		clock = pygame.time.Clock()
		robot = pygame.image.load("car60_40.png")
		while 1:
			clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return
			screen.fill(white)
			screen.blit(robot,(320,240))
			pygame.display.flip()






if __name__ == '__main__':
	pygame.init()
	pygame.display.set_caption("Draw")
	screen = pygame.display.set_mode((640,480))
	Simulator().main(screen)
