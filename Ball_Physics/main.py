import pygame

# make circle using math formula and vectors

# OBJECT CLASSES
class Ball_Object:
	def __init__(self, x_pos, y_pos, radius, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.radius = radius
		self.color = color
		self.speed = 5
		self.gravity = 0.8
		self.speed_drop = 1

	def drawObject(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

	def moveObject(self):
		# When spacebar is pressed ball needs to go up in the y_pos
		key = pygame.key.get_pressed()

		if key[pygame.K_SPACE]:
			self.center[1] -= self.y_pos

# INITIALIZE
pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

# BALL
ball = Ball_Object(250, 350, 10, "black")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	
	screen.fill("white")

	# MOVEMENT
	ball.moveObject()

	# DRAW
	ball.drawObject(screen)

	pygame.display.flip()

	clock.tick(40)

pygame.quit()
