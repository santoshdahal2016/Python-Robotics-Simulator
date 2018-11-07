import pygame
from math import *


"""Define color"""
red = (200, 0, 0)
blue = (0, 0, 255)
green = (0, 155, 0)
yellow = (155, 155, 0)
white = (255, 255, 255)
black = (0, 0, 0)


display_width = 800
display_height = 800
world_size = display_width

def text_objects(text, color, size):
	if size == "small":	
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)

	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size="small"):
	# screen_text = font.render(msg,True, color)
	# gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	textSurface, textRect = text_objects(msg, color, size)
	textRect.center = display_width/2 , display_height/2 + y_displace
	screen.blit(textSurface, textRect)



class robot:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.orientation = 0
		self.control = "manual"
		self.fx = 0
		self.fy = 0

	def set(self, x, y,orientation):
		self.x = x
		self.y = y
		self.orientation = orientation

	def destination(self , x , y):
		self.fx = x
		self.fy = y

	def move(self, turn, forward):
		self.orientation = self.orientation + turn
		#cos value 0degree->1 , 90degree->0, 180degree->-1
		#we must pass degree in radian
		self.x = self.x + forward*cos(-self.orientation*pi/180)
		#sin value 0degree->0 , 90degree->1, 180degree->0
		#we must pass degree in radian
		self.y = self.y - forward*sin(-self.orientation*pi/180)
		
		self.x %= world_size
		self.y %= world_size
		
	def automatic(self, orientation , forward):
		self.orientation = orientation
		#cos value 0degree->1 , 90degree->0, 180degree->-1
		#we must pass degree in radian
		self.x = self.x + forward*cos(-self.orientation*pi/180)
		#sin value 0degree->0 , 90degree->1, 180degree->0
		#we must pass degree in radian
		self.y = self.y - forward*sin(-self.orientation*pi/180)
		
		self.x %= world_size
		self.y %= world_size

	def draw(self):
		car_img = pygame.image.load("car60_40.png")
		img = pygame.transform.rotate(car_img, -self.orientation)
		screen.blit(img, (self.x, self.y))
		if self.control == "manual":
			message_to_screen("Manual",green,200)
		if self.control == "automatic":
			message_to_screen("Automatic",red,200)
			pygame.draw.circle(screen, green, (self.fx , self.fy), 10) 




class Simulator(object):
	def main(self , screen , robot):
		clock = pygame.time.Clock()
		robot.draw()
		delta_orient = 0.0
		delta_forward = 0.0
		while 1:
			clock.tick(50)
			screen.fill(white)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						robot.control = "manual"

					if event.key == pygame.K_a:
						robot.control = "automatic"

					if robot.control == "manual":
						if event.key == pygame.K_LEFT:
							delta_orient = 1
						elif event.key == pygame.K_RIGHT:
							delta_orient = -1
						elif event.key == pygame.K_UP:
							delta_forward = 1
						elif event.key == pygame.K_DOWN:
							delta_forward = -1
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						delta_orient = 0.0
						delta_forward = 0.0

				if robot.control == "automatic":
					if event.type == pygame.MOUSEBUTTONUP:
						pos = pygame.mouse.get_pos()
						robot.destination(pos[0],pos[1])
			if robot.control == "automatic":

				deltax = robot.fx - robot.x
				deltay = robot.fy - robot.y

				angle_rad = atan2(deltay,deltax)
				angle_deg =  angle_rad*180.0/pi

				print "Target"

				print angle_deg
				print "original"


				print robot.orientation 

				delangle = robot.orientation - angle_deg


				print "difference"

				print delangle
				if delangle > -2 and delangle < 2:
					robot.set(robot.x,robot.y,angle_deg)
					passangle = robot.orientation
				else:
					passangle = robot.orientation - 0.08 * delangle


				print "next angle"

				print passangle

				dist = sqrt((robot.fx - robot.x)**2 + ((robot.fy - robot.y)**2))


				if delangle == 0:
				 	robot.automatic(passangle,dist*0.1)
				robot.automatic(passangle,0)
			robot.move(delta_orient, delta_forward)
			robot.draw()
			pygame.display.flip()



if __name__ == '__main__':
	pygame.init()

	smallfont = pygame.font.SysFont("arial", 25)
	medfont = pygame.font.SysFont("arial", 50)
	largefont = pygame.font.SysFont("arial", 80)

	pygame.display.set_caption("Move")
	screen = pygame.display.set_mode((display_width,display_height))
	robot = robot()
	Simulator().main(screen , robot)
