# create two balls -- DONE
# Have balls collide with each other -- DONE
	# ball1 will have a momentum and when it collides with ball2 the momentum will be transferred to ball2 -- DONE
		# when spacebar is pressed than move ball1 -- DONE

import pygame, math

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
		
		self.activate = False

	def draw_object(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius, self.mass)

	def move_object(self):
		self.center[0] += self.velocity

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Momentum")

# BALL
ball1 = Ball(50, 250, 30, "black", 7, 10) # inital velocity = 5
ball2 = Ball(250, 250, 30, "red", 0, 10) # initial velocity = 0


# COLLISION
def collision(ball1, ball2):
	# print(f"INITAL: Ball 1 p = {ball1.mass*ball1.velocity}, Ball 2 p = {ball2.mass*ball2.velocity}")

	total_x = (ball2.center[0] - ball1.center[0]) ** 2
	total_y = (ball2.center[1] - ball1.center[1]) ** 2

	total_radii = ball2.radius + ball1.radius # total of radii

	d = int(math.sqrt(total_x + total_y)) # distance formula

	if d < total_radii and ball1.velocity != 0: # collsion condition
		ball1_p = ball1.mass * ball1.velocity # Ball 1 momentum

		ball1.velocity = 0 # get ball 1 to stop moving (Ball 1 final velcity is 0)

		ball2.velocity = ball1_p // ball2.mass # Ball 2 final velocity 

		# print(f"COLLISION: Ball 1 p = {ball1.mass*ball1.velocity}, Ball 2 p = {ball2.mass*ball2.velocity}")

		# print(ball1.velocity, ball2.velocity)

	return ball1.velocity, ball2.velocity

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				ball1.activate = True

#		if event.type == pygame.KEYUP:	
#			ball1.activate = False
#			print(False)

	screen.fill("white")

	# COLLISION
	ball1.velocity, ball2.velocity = collision(ball1, ball2)

	if ball2.velocity != 0:
		ball2.move_object()
		# print(f"FINAL: Ball 1 p = {ball1.mass*ball1.velocity}, Ball 2 p = {ball2.mass*ball2.velocity}")


	# MOVEMENT
	if ball1.activate == True:
		ball1.move_object()

	# DRAW
	ball1.draw_object(screen)
	ball2.draw_object(screen)

	pygame.display.update()

	clock.tick(60)

pygame.quit()
