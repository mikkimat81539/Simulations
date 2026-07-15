import pygame


class Ball_Object:
	def __init__(self, x_pos, y_pos, color, radius):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.color = color
		self.radius = radius

	def drawObject(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

	def moveObject(self):
		pass

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


# Ball Object
ball = Ball_Object(250, 250, "white", 10)

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("#c296ff")


	# DRAW
	ball.drawObject(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
