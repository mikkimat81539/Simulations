import pygame, random

# GOAL: Each time there is collision randomly pick number for speed [1, 10, 20, 19]


class Ball_Object:
	def __init__(self, x_pos, y_pos, color, radius):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.color = color
		self.radius = radius

		self.vel_x = random.randint(1, 20)
		self.vel_y = random.randint(1, 20)

	def drawObject(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

	def moveObject(self, surface_width, surface_height):
		self.center[0] += self.vel_x # x-axis movement
		self.center[1] += self.vel_y # y-axis movement

		self.collision(surface_width, surface_height)

	def collision(self, surface_width, surface_height):
		boundary_x, boundary_y = (surface_width - self.radius), (surface_height - self.radius)
		
		# condition for x-axis collison
		if self.center[0] >= boundary_x or self.center[0] <= 5:
			self.vel_x = -self.vel_x

		# condition for y-axis collision
		if self.center[1] >= boundary_y or self.center[1] <= 5:
			self.vel_y = -self.vel_y

pygame.init()

screen_width = 500
screen_height = 200

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Ball Object
ball = Ball_Object(random.randint(10, 420), random.randint(10, 120), "white", 10)

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("#c296ff")

	# MOVEMENT
	ball.moveObject(screen_width, screen_height)

	# DRAW
	ball.drawObject(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
