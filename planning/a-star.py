# A visual demonstration of A* search algorithm
import pygame
from gridworld import GridWorld
import time
from math import *

"""Define color"""
red = (200, 0, 0)
blue = (0, 0, 255)
green = (0, 155, 0)
yellow = (155, 155, 0)
white = (255, 255, 255)
black = (0, 0, 0)

length = 0
clock = pygame.time.Clock()

screen_size = 1000
cell_width = 20
cell_height = 20
cell_margin = 0
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([screen_size,screen_size])
pygame.display.set_caption("Autonomous Robot")


import pyttsx

engine = pyttsx.init() # "espeak" defines what engine program is running on
engine.setProperty('rate', 100)
# build grid structure
grid = [[0 for col in range(50)] for row in range(50)]
grid[0][1] = 1 # obstacle
grid[1][1] = 1 # obstacle
grid[2][1] = 1 # obstacle
grid[3][1] = 1 # obstacle
grid[4][4] = 1 # obstacle

grid[10][30] = 1 # obstacle
grid[10][31] = 1 # obstacle
grid[10][32] = 1 # obstacle
grid[8][30] = 1 # obstacle
grid[9][30] = 1 # obstacle
grid[7][30] = 1 # obstacle
grid[6][30] = 1 # obstacle
grid[5][30] = 1 # obstacle
grid[4][30] = 1 # obstacle
grid[3][30] = 1 # obstacle
grid[2][30] = 1 # obstacle
grid[1][30] = 1 # obstacle
grid[0][30] = 1 # obstacle


grid[28][15] = 1 # obstacle
grid[29][15] = 1 # obstacle
grid[27][15] = 1 # obstacle
grid[26][15] = 1 # obstacle
grid[25][15] = 1 # obstacle
grid[24][15] = 1 # obstacle
grid[23][15] = 1 # obstacle
grid[22][15] = 1 # obstacle
grid[21][15] = 1 # obstacle
grid[20][15] = 1 # obstacle
grid[8][15] = 1 # obstacle
# grid[18][15] = 1 # obstacle
# grid[19][15] = 1 # obstacle
# grid[17][15] = 1 # obstacle
grid[16][15] = 1 # obstacle
grid[15][15] = 1 # obstacle
grid[14][15] = 1 # obstacle
grid[13][15] = 1 # obstacle
grid[12][15] = 1 # obstacle
grid[11][15] = 1 # obstacle
grid[10][15] = 1 # obstacle
grid[8][15] = 1 # obstacle
grid[9][15] = 1 # obstacle
grid[7][15] = 1 # obstacle
grid[6][15] = 1 # obstacle
grid[5][15] = 1 # obstacle
grid[4][15] = 1 # obstacle
grid[3][15] = 1 # obstacle
grid[2][15] = 1 # obstacle
grid[1][15] = 1 # obstacle
grid[0][15] = 1 # obstacle




grid[38][20] = 1 # obstacle
grid[39][20] = 1 # obstacle
grid[37][20] = 1 # obstacle
grid[36][20] = 1 # obstacle
grid[35][20] = 1 # obstacle
grid[34][20] = 1 # obstacle
grid[33][20] = 1 # obstacle
grid[32][20] = 1 # obstacle
grid[31][20] = 1 # obstacle
grid[30][20] = 1 # obstacle
grid[28][20] = 1 # obstacle
grid[29][20] = 1 # obstacle
grid[27][20] = 1 # obstacle
grid[26][20] = 1 # obstacle
grid[25][20] = 1 # obstacle
grid[24][20] = 1 # obstacle
grid[23][20] = 1 # obstacle
grid[22][20] = 1 # obstacle
grid[21][20] = 1 # obstacle
grid[20][20] = 1 # obstacle
grid[8][20] = 1 # obstacle
grid[18][20] = 1 # obstacle
grid[19][20] = 1 # obstacle
grid[17][20] = 1 # obstacle
grid[16][20] = 1 # obstacle
grid[15][20] = 1 # obstacle
grid[14][20] = 1 # obstacle
grid[13][20] = 1 # obstacle
grid[12][20] = 1 # obstacle
grid[11][20] = 1 # obstacle
# grid[10][20] = 1 # obstacle
# grid[8][20] = 1 # obstacle
# grid[9][20] = 1 # obstacle
# grid[7][20] = 1 # obstacle
grid[6][20] = 1 # obstacle
grid[5][20] = 1 # obstacle
grid[4][20] = 1 # obstacle
grid[3][20] = 1 # obstacle
grid[2][20] = 1 # obstacle
grid[1][20] = 1 # obstacle
grid[0][20] = 1 # obstacle


grid[38][25] = 1 # obstacle
grid[39][25] = 1 # obstacle
grid[37][25] = 1 # obstacle
grid[36][25] = 1 # obstacle
grid[35][25] = 1 # obstacle
grid[34][25] = 1 # obstacle
grid[33][25] = 1 # obstacle
grid[32][25] = 1 # obstacle
grid[31][25] = 1 # obstacle
grid[30][25] = 1 # obstacle
grid[28][25] = 1 # obstacle
grid[29][25] = 1 # obstacle
grid[27][25] = 1 # obstacle
grid[26][25] = 1 # obstacle
grid[25][25] = 1 # obstacle
# grid[24][25] = 1 # obstacle
# grid[23][25] = 1 # obstacle
# grid[22][25] = 1 # obstacle
grid[21][25] = 1 # obstacle
grid[20][25] = 1 # obstacle
grid[8][25] = 1 # obstacle
grid[18][25] = 1 # obstacle
grid[19][25] = 1 # obstacle
grid[17][25] = 1 # obstacle
grid[16][25] = 1 # obstacle
grid[15][25] = 1 # obstacle
grid[14][25] = 1 # obstacle
grid[13][25] = 1 # obstacle
grid[12][25] = 1 # obstacle
grid[11][25] = 1 # obstacle
grid[10][25] = 1 # obstacle
grid[8][25] = 1 # obstacle
grid[9][25] = 1 # obstacle
grid[7][25] = 1 # obstacle
grid[6][25] = 1 # obstacle
grid[5][25] = 1 # obstacle
grid[4][25] = 1 # obstacle
grid[3][25] = 1 # obstacle
grid[2][25] = 1 # obstacle
grid[1][25] = 1 # obstacle
grid[0][25] = 1 # obstacle


cluster_direction = []
spoken_direction = []
coordinate_path = []
path = []


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1]] # go right
delta_name = ['^', '<', 'v', '>']
delta_speech =	{
		"^": "go up",
		"<": "go left",
		"v": "go down",
		">":"go right"
	}
delta_degree =	{
		"^": -90,
		"<": -180,
		"v": -270,
		">":0
	}
# build heuristics grid
heuristics = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]


k = len(grid[0]) - 1

for i in range(len(grid)-1, -1, -1):
	num = (len(grid[0])-1) - k
	for j in range(len(grid[0])-1, -1, -1):
		heuristics[i][j] = num
		num += 1
	k -= 1

def check_valid(node, grid):
    if node[0] >= 0 and node[0] < len(grid) and node[1] >= 0  and node[1] < len(grid[0]) and (grid[node[0]][node[1]] == 0):
        return True
    else:
        return False
#A heuristic technique, often called simply a heuristic, is any approach to problem solving, learning, or discovery that employs a practical method, not guaranteed to be optimal, perfect, logical, or rational, but instead sufficient for reaching an immediate goal.
def heuristic(a, b):
	return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def run_a_star(grid, heuristics, init, goal, cost):


	action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
	policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	expanded = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

	visited = []
	opened = []

	# [f, g, [x, y]] 
	# f = g + heuristics[x][y]
	# opened.append([0+heuristics[init[0]][init[1]], 0, init[0], init[1]])
	opened.append([heuristic(goal, init), 0, init[0], init[1]])

	visited.append([init[0], init[1]])
	next = opened.pop()
	count = 0
	
	while [next[2],next[3]] != goal:

		if len(opened) > 0:
			opened.sort()
			print opened
			opened.reverse()
			next = opened.pop()

		x = next[2]
		y = next[3]
		g = next[1]
		f = next[0]
		gridworld.draw_cell([[f, [x, y]]])
		# gridworld.show()
		# time.sleep(0)
		expanded[next[2]][next[3]] = count
		count += 1
		for a in range(len(delta)):
			x2 = x + delta[a][0]
			y2 = y + delta[a][1]
			if check_valid([x2, y2], grid):
				g2 = g + cost
				if [x2, y2] not in visited:
					#f = g2 + heuristics[x2][y2]
					f = g2 + heuristic(goal, [x2, y2])
					opened.append([f,g2,x2, y2])
					visited.append([x2, y2])
					action[x2][y2] = a
		
	print expanded
	# policy search
	x = goal[0]
	y = goal[1]
	policy[x][y] = '*'
	del path[:]

	direction = []
	path.append([x, y])
	while([x, y] != init):
		x1 = x - delta[action[x][y]][0]
		y1 = y - delta[action[x][y]][1]
		policy[x1][y1] = delta_name[action[x][y]]
		x = x1
		y = y1
		path.append([x, y])
		direction.append(delta_name[action[x][y]])
	# for i in range(len(policy)):
	# 	print (policy[i])
	# exit()

	path.reverse()
	direction.pop()
	direction.reverse()
	old_direction = ' '
	count = 0

	del cluster_direction[:]
	del spoken_direction[:]

	for i in range(len(direction)):
		if direction[i] != old_direction :
			if i != 0:
				cluster_direction.append(temp_direction)
				spoken_direction.append(delta_speech[old_direction]+" "+ str(count) +" block")
				count = 0
			temp_direction = []
			temp_direction.append(direction[i])
			count += 1
			old_direction = direction[i]
		else:
			temp_direction.append(direction[i])
			count += 1
			old_direction = direction[i]
		if i == (len(direction)-1):
			cluster_direction.append(temp_direction)
			spoken_direction.append(delta_speech[old_direction]+" "+ str(count) +" block")


	
	# print cluster_direction
	# print spoken_direction
	smooth_path = gridworld.smooth_path(path)

	origin = [0+1*cell_margin+(cell_width/2),0+1*cell_margin+(cell_height/2)]
	col = cell_margin + cell_width
	row = cell_margin + cell_height
	del coordinate_path[:]
	for i in path:
		coordinate_path.append([origin[0]+col*i[1], origin[1]+row*i[0]])

	# print coordinate_path

	speech = ' ,'.join(spoken_direction)
	# print speech

	gridworld.draw_path(smooth_path)
	engine.say(speech)



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
		
		self.x %= screen_size
		self.y %= screen_size
		# self.fx = self.x
		# self.fy = self.y
	def automatic(self, orientation , forward):
		self.orientation = orientation
		#cos value 0degree->1 , 90degree->0, 180degree->-1
		#we must pass degree in radian
		self.x = self.x + forward*cos(-self.orientation*pi/180)
		#sin value 0degree->0 , 90degree->1, 180degree->0
		#we must pass degree in radian
		self.y = self.y - forward*sin(-self.orientation*pi/180)
		
		self.x %= screen_size
		self.y %= screen_size

	def draw(self):
		car_img = pygame.image.load("car60_40.png")
		img = pygame.transform.rotate(car_img, -self.orientation)
		# img = pygame.transform.scale(img, (40, 60))
		screen.blit(img, (self.x, self.y))


init = [1, 40]
goal = [5, 0]
delta_orient = 0.0
delta_forward = 0.0
robot = robot()
gridworld = GridWorld(screen,robot,cell_width, cell_height, cell_margin,init, goal, grid)
gridworld.show()
# run_a_star(grid, heuristics, init, goal, cost=1)


# engine.runAndWait()
# robot.draw()

pygame.display.flip()
# gridworld.show()s
# gridworld.loop()
while 1:
	# screen.fill(white)
	clock.tick(50)
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			next_goal = [((pos[1]-cell_margin)/(cell_height+cell_margin)),((pos[0]-cell_margin)/(cell_width+cell_margin))]
			init = goal
			goal = next_goal
			gridworld = GridWorld(screen,robot,cell_width, cell_height, cell_margin,init, goal, grid)
			run_a_star(grid, heuristics, init, goal, cost=1)
			engine.runAndWait()

			# print cluster_direction
			# print coordinate_path
			cluster_direction.reverse()
			


			gridworld.show()
			# engine.runAndWait()
		elif event.type == pygame.KEYDOWN:
			# if robot.control == "manual":

			if event.key == pygame.K_LEFT:
				delta_orient = 1
			elif event.key == pygame.K_RIGHT:
				delta_orient = -1
			elif event.key == pygame.K_UP:
				delta_forward = 1
			elif event.key == pygame.K_DOWN:
				delta_forward = -1
		elif event.type == pygame.KEYUP:
			init = [int(round(((robot.y-cell_margin)/(cell_height+cell_margin)))),int(round(((robot.x-cell_margin)/(cell_width+cell_margin))))]
			goal = init
			print goal
			gridworld = GridWorld(screen,robot,cell_width, cell_height, cell_margin,init, goal, grid)

			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				delta_orient = 0.0
				delta_forward = 0.0
	deltax = int(robot.fx - robot.x)
	deltay = int(robot.fy - robot.y)
	print robot.fx , robot.fy , robot.x , robot.y
	print deltax , deltay
	print cluster_direction
	if deltax == 0 and deltay == 0 :
		if len(cluster_direction) > 0 :
			step = cluster_direction[len(cluster_direction)-1]
			cluster_direction.pop()
			angle = delta_degree[step[i][0]]
			old_length = length
			length += len(step)
			# print coordinate_path[length]
			gridworld = GridWorld(screen,robot,cell_width, cell_height, cell_margin,init, goal, grid)
			smooth_path = gridworld.smooth_path(path)
			gridworld.draw_path(smooth_path)


			robot.set(coordinate_path[old_length][0],coordinate_path[old_length][1],angle)
			pygame.draw.circle(screen, yellow, [coordinate_path[old_length][0],coordinate_path[old_length][1]], 5)

			
			robot.destination(coordinate_path[length][0],coordinate_path[length][1])

			pygame.draw.circle(screen, green, [coordinate_path[length][0],coordinate_path[length][1]], 5)
			gridworld.show()
			print angle , length
		else:
			robot.destination(robot.x,robot.y)
			robot.move(delta_orient, delta_forward)
			length = 0

	else:
			# angle_rad = atan2(deltay,deltax)
			# angle_deg =  angle_rad*180.0/pi
			# print "Target"
			# print angle_deg
			# print "original"
			# print robot.orientation 
			# delangle = robot.orientation - angle_deg
			# print "difference"
			# print delangle
			# if delangle > -2 and delangle < 2:
			# 	robot.set(robot.x,robot.y,angle_deg)
			# 	passangle = robot.orientation
			# else:
			# 	passangle = robot.orientation - 0.08 * delangle
			# print "next angle"
			# print passangle
			dist = sqrt((robot.fx - robot.x)**2 + ((robot.fy - robot.y)**2))
			#if delangle == 0:
			# 	robot.automatic(passangle,dist*0.1)
			robot.automatic(robot.orientation,dist*0.09)
		
	robot.draw()
	pygame.display.flip()

# while 1:
# 	clock.tick(50)
# 	screen.fill(white)
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			exit()
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_m:
# 				robot.control = "manual"

# 			if event.key == pygame.K_a:
# 				robot.control = "automatic"

# 			if robot.control == "manual":
# 				if event.key == pygame.K_LEFT:
# 					delta_orient = 1
# 				elif event.key == pygame.K_RIGHT:
# 					delta_orient = -1
# 				elif event.key == pygame.K_UP:
# 					delta_forward = 1
# 				elif event.key == pygame.K_DOWN:
# 					delta_forward = -1
# 		elif event.type == pygame.KEYUP:
# 			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
# 				delta_orient = 0.0
# 				delta_forward = 0.0

# 		if robot.control == "automatic":
# 			if event.type == pygame.MOUSEBUTTONUP:
# 				pos = pygame.mouse.get_pos()
# 				robot.destination(pos[0],pos[1])
# 	if robot.control == "automatic":
# 		deltax = robot.fx - robot.x
# 		deltay = robot.fy - robot.y

# 		angle_rad = atan2(deltay,deltax)
# 		angle_deg =  angle_rad*180.0/pi

# 		print "Target"

# 		print angle_deg
# 		print "original"


# 		print robot.orientation 

# 		delangle = robot.orientation - angle_deg


# 		print "difference"

# 		print delangle
# 		if delangle > -2 and delangle < 2:
# 			robot.set(robot.x,robot.y,angle_deg)
# 			passangle = robot.orientation
# 		else:
# 			passangle = robot.orientation - 0.08 * delangle


# 		print "next angle"

# 		print passangle

# 		dist = sqrt((robot.fx - robot.x)**2 + ((robot.fy - robot.y)**2))


# 			#if delangle == 0:
# 			# 	robot.automatic(passangle,dist*0.1)
# 		robot.automatic(passangle,dist*0.03)
# 	robot.move(delta_orient, delta_forward)
# 	robot.draw()
# 	pygame.display.flip()