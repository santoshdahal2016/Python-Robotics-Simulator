import pygame

"""Define color"""
red = (200, 0, 0)
blue = (0, 0, 255)
green = (0, 155, 0)
yellow = (155, 155, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class robot:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.orientation = 0

	def set(self, x, y,orientation):
		self.x = x
		self.y = y
		self.orientation = orientation

	def move(self, turn, x,y):
		self.orientation = self.orientation + turn

		self.x = self.x + x
		self.y = self.y - y


	def draw(self):
		car_img = pygame.image.load("car60_40.png")
		img = pygame.transform.rotate(car_img, self.orientation)
		screen.blit(img, (self.x, self.y))

class Simulator(object):
	def main(self , screen , robot):
		clock = pygame.time.Clock()
		robot.draw()
		x = 0
		y = 0
		orientation = 0
		while 1:
			clock.tick(30)
			screen.fill(white)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x = -1
					elif event.key == pygame.K_RIGHT:
						x = 1
					elif event.key == pygame.K_UP:
						y = 1
					elif event.key == pygame.K_DOWN:
						y = -1
					elif event.key == pygame.K_a:
						orientation = -1
					elif event.key == pygame.K_d:
						orientation = 1
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_DOWN:
						x = 0
						y = 0
						orientation = 0 
			robot.move(orientation , x , y)
			robot.draw()
			pygame.display.flip()



if __name__ == '__main__':
	pygame.init()
	pygame.display.set_caption("Move")
	screen = pygame.display.set_mode((640,480))
	robot = robot()
	Simulator().main(screen , robot)
