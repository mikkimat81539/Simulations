# create two balls 
# Have balls collide with each other
	# ball1 will have a momentum and when it collides with ball2 the momentum will be transferred to ball2
		# when spacebar is pressed than move ball1 when ball2 hits wall stop
			# apply charge when spacebar is held
		# Have different speeds

import pygame

pygame.init()

# OBJECT CLASS
class Ball:
	def __init__(self, x_pos, y_pos, radius, color, velocity, mass):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)	

		self.radius = radius
		self.color = color

		self.velocity = velocity
		self.mass = mass

	def draw_object(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius, self.mass)

	def move_object(self):
		pass

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Momentum")

# BALL
ball1 = Ball(50, 250, 30, "black", 7, 10)
ball2 = Ball(250, 250, 30, "red", 7, 10)


# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# DRAW
	ball1.draw_object(screen)
	ball2.draw_object(screen)

	pygame.display.update()

	clock.tick(40)

pygame.quit()
