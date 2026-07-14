import pygame

# make circle using math formula and vectors

# OBJECT CLASSES
class Ball_Object:
	def __init__(self, x_pos, y_pos, radius, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = (self.x_pos, self.y_pos)
		self.radius = radius
		self.color = color

	def drawObject(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")

# BALL
ball = Ball_Object(100, 100, 10, "black")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	ball.drawObject(screen)

	pygame.display.flip()

pygame.quit()
