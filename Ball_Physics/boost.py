# create ball -- DONE 
# create a booster
	# Create booster class using line as the shape -- DONE
	# Increase booster along the y-axis -- DONE
	# To increase booster use spacebar -- DONE
	# velocity needs to increase when spacebar is held -- DONE
	# have a max velocity of 10

# GOAL: When spacebar is held and than release ball shoots based on velocity after release

import pygame
from Ball_Object import Ball

pygame.init()

# BOOSTER CLASS
class Booster:
	def __init__(self, x_pos, y_pos, color, thickness):
		self.x_pos = x_pos
		self.y_pos = y_pos

		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.end_pos = pygame.math.Vector2(self.x_pos, self.y_pos + 5)

		self.color = color
		self.thickness = thickness

		self.activate = False

		self.increase = 3 # This moves the line

	def draw_line(self, surface):
		pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.thickness)
		
	def move_line(self, ball):
		self.start_pos[1] -= self.increase # Display line movement along the y axis	
		ball.velocity += 1 # increase the ball velocity	
		# print(f"VELOCITY: {ball.velocity}")
		# print(f"Y POS: {self.start_pos[1]}")

		if self.start_pos[1] < 10:
			self.activate = False
			return
			

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("BOOSTER")

# BALL
ball = Ball(20, 120, 10, "black", 0)

# BOOSTER
booster = Booster(480, 300, "red", 5)

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

			if event.key == pygame.K_SPACE:
				booster.activate = True

		if event.type == pygame.KEYUP: # When space is release go back to original position
			booster.activate = False
			booster.start_pos[1] = booster.y_pos
			
			ball.activate = True

	screen.fill("white")

	# MOVEMENT
	if booster.activate == True:
		booster.move_line(ball)

	if ball.activate == True:
		ball.move_ball()
		# print(f"Ball Speed: {ball.velocity}")
		print(f"Ball X_Pos{ball.center[0]}")

		if ball.center[0] >= screen.get_width()-ball.radius:
			ball.center[0] -= ball.velocity

	# DRAW
	ball.draw_ball(screen)

	booster.draw_line(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()



