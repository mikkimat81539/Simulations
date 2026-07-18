# GOAL: create two balls that consist of mass and velocity -- DONE
	# Determine the kinetic energy -- DONE
	# Display which has more kinetic energy -- DONE

	# Apply movement to balls -- DONE

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

	def kinetic_energy(self):
		KE = 0.5*(self.mass * (self.velocity)**2)
		return KE

	def move_object(self):
		self.center[0] += self.velocity
		
		if self.center[0] + self.radius >= 500:
			self.velocity = 0

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))

# BALL
green_ball = Ball(50, 20, 10, 0.05, 4, "green")
red_ball = Ball(50, 100, 20, 0.1, 2, "red")


KE_green = green_ball.kinetic_energy()
KE_red = red_ball.kinetic_energy()

print(f"""\nThe green ball has a kinetic energy of {KE_green}J and the red ball has a kinetic energy of {KE_red}J\n""")

if KE_green > KE_red:
	print("The green ball has more kinetic energy")

elif KE_green == KE_red:
	print("The green ball and red ball have the same kinetic energy")

else:
	print("The red ball has more kinetic energy")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# MOVEMENT
	green_ball.move_object()
	red_ball.move_object()

	# DRAW
	green_ball.draw_object(screen)
	red_ball.draw_object(screen)

	pygame.display.update()
	
	clock.tick(40)

pygame.quit()



