# GOAL: create two balls that consist of mass and velocity
	# Determine the kinetic energy
	# Display which has more kinetic energy

import pygame

pygame.init()

# BALL CLASS
class Ball:
	def __init__(self, x_pos, y_pos, radius, mass, velocity, color):
		self.x_pos = x_pos
		self.y_pos = y_pos

		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)

		self.radius = radius
		self.mass = mass
		self.velocity = velocity
		self.color = color

	def draw_object(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

	def move_object(self):
		pass

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))

# BALL
green_ball = Ball(20, 20, 10, 2, 1, "green")
red_ball = Ball(100, 100, 20, 5, 1, "red")


# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	green_ball.draw_object(screen)
	red_ball.draw_object(screen)


	pygame.display.update()

pygame.quit()



