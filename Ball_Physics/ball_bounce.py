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
		self.gravity = 0.8
		self.velocity = 10
		self.activate = False

	def drawObject(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

		print(self.center[1])

	def moveObject(self):
		self.velocity += self.gravity
		self.center[1] += self.velocity

		if self.center[1] >= (480 - self.radius):
			self.velocity = -self.velocity

# INITIALIZE
pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

# BALL
ball = Ball_Object(250, 250, 10, "black")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				ball.activate = True
		
	
	screen.fill("white")

	# MOVEMENT
	if ball.activate == True:
		ball.moveObject()

	# DRAW
	ball.drawObject(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
