# create ball 
# create a booster
	# Create booster class using line as the shape
	# Increase booster along the y-axis
	# To increase booster use spacebar
	# velocity needs to increase when spacebar is held
	# have a max velocity of 10

# GOAL: When spacebar is held and than release ball shoots based on velocity after release

import pygame
from Ball_Object import Ball

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("BOOSTER")

# BALL
ball = Ball(20, 250, 10, "black", 7)

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# DRAW
	ball.draw_ball(screen)

	pygame.display.flip()

pygame.quit()



