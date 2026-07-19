# create two balls that collide with each other
# ball1 will have a momentum and when it collides with ball2 the momentum will be transferred to ball2
	# when spacebar is pressed than move ball1 when ball2 hits wall stop
		# apply charge when spacebar is held
	# Have different speeds

import pygame

pygame.init()

# OBJECT CLASS

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Momentum")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	pygame.display.update()

	clock.tick(40)

pygame.quit()
